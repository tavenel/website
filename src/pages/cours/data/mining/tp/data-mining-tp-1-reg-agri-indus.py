import numpy as np
import matplotlib.pyplot as plt

## --- Saisie des données et tracé des courbes ---

agri = [100, 60, 76, 74, 90, 93, 102, 98, 103, 110, 117, 118, 112, 115, 116, 121, 134, 130]
indus = [100, 50, 84, 99, 113, 122, 128, 143, 145, 146, 159, 172, 188, 204, 213, 220, 242, 254]
n = len(agri)
x = np.arange(start=1944, stop=1962, step=1)

fig, ax = plt.subplots(2, 1, figsize=(8, 10))
fig.tight_layout()

ax[0].plot(x, agri, label='production agricole', color='orange')
ax[0].plot(x, indus, label='production industrielle', color='blue')
ax[0].set(title='Production agricole et production industrielle de 1945 à 1961')
ax[0].legend()

## --- Nuage de points son centre de gravité ---

centre = {'x': sum(agri)/n, 'y': sum(indus)/n}
# ou : 
centre2 = {'x': np.average(agri), 'y': np.average(indus)}
print(f'Centre de gravité : {centre} ou {centre2}')

ax[1].scatter(agri, indus)
ax[1].scatter(centre['x'], centre['y'], color='red', label='Centre de gravité')
ax[1].set(title='Nuage de points : production agricole en fonction de la production industrielle')
ax[1].legend()

#plt.show()

## --- Régression linéaire de la production industrielle sur la production agricole ---

#a = Cov(X,Y)/Var(X)
#b = mean(Y) - a * mean(X)
cov = {'cov_agri_indus': [], 'var_agri': [], 'var_indus': []}
for i in range(18):
    cov['cov_agri_indus'].append( (agri[i] - centre['x']) * (indus[i] - centre['y']) )
    cov['var_agri'].append( (agri[i] - centre['x']) ** 2 )
    cov['var_indus'].append( (indus[i] - centre['y']) ** 2 )

def b(a):
    return centre['y'] - a * centre['x']

a_hat_biais = sum(cov['cov_agri_indus']) / sum(cov['var_agri'])
b_hat_biais = b(a_hat_biais)
print(f'Estimation des paramètres de la régression linéaire (manuellement - avec biais) : a={a_hat_biais} et b={b_hat_biais}')

def reg_lin(a, b):
    return lambda x : a * x + b
reg_indus_agri = reg_lin(a_hat_biais, b_hat_biais)

ax[1].plot(
        agri,
        reg_indus_agri(np.array(agri)),
        color='blue', 
        label='Régression linéaire production industrielle sur production agricole (avec biais)'
        )

## --- Utilisation de la librairie numpy ---

cov_matrix = np.cov(agri, indus)
#cov_matrix = np.cov(agri, indus, bias=True)
# matrice :
# ( var(x)   |  cov(x,y) )
# ( cov(x,y) |  var(y)   )
print('covar matrix :', cov_matrix)
print('var agri', cov_matrix[0][0])
print('covar agri,indus', cov_matrix[0][1])

a_hat2 = cov_matrix[0][1] / cov_matrix[0][0]
b_hat2 = b(a_hat2)
print(f'Estimation des paramètres de la régression linéaire (numpy) : a={a_hat2} et b={b_hat2}')
# Les valeurs sont différentes - par défaut numpy.cov() utilise un estimateur sans biais.
# Pour avoir les mêmes valeurs, on aurait pu utiliser : np.cov(agri, indus, bias=True)
# Mais on préfère utiliser un estimateur non biaisé (ici : E[X] = Sigma^2*(n-1)/n != Sigma^2)
# Il faut donc rectifier cet estimateur par un facteur n/(n-1)
# Voir : https://en.wikipedia.org/wiki/Bias_of_an_estimator


## --- Correction de l'estimateur ---

a_hat = a_hat_biais * n/(n-1)
b_hat = b(a_hat)
print(f'Estimation des paramètres de la régression linéaire (manuellement - sans biais) : a={a_hat} et b={b_hat}')

reg_indus_agri2 = reg_lin(a_hat, b_hat)

ax[1].plot(
        agri,
        reg_indus_agri2(np.array(agri)),
        color='cyan', 
        label='Régression linéaire idus ~ agri (sans biais)'
        )

## --- Régression linéaire de la production agricole sur la production industrielle ---

# Calcul et ajout de la régression agri sur indus :
a2_hat = cov_matrix[0][1] / cov_matrix[1][1] # Cov(indus,agri) / Var(indus)
b2_hat = centre['x'] - a2_hat * centre['y']
print(f'Estimation des paramètres de la régression linéaire (numpy) de agri sur indus : a={a2_hat} et b={b2_hat}')
reg_agri_indus = reg_lin(a2_hat, b2_hat)
ax[1].plot(
        reg_agri_indus(np.array(indus)),
        indus,
        color='orange',
        label='Régression linéaire agri ~ indus'
        )
ax[1].legend()
plt.show()

## --- Étude des résidus ---

pred_indus = [ reg_indus_agri(agri[i]) for i in range(n) ]
pred_agri = [ reg_agri_indus(indus[i]) for i in range(n) ]
resid_indus = [ y - y_ for (y, y_) in zip(indus, pred_indus) ]
resid_agri = [ y - y_ for (y, y_) in zip(agri, pred_agri) ]

fig, ax = plt.subplots(2, 2, figsize=(8, 10))
fig.tight_layout()

ax[0][0].plot(pred_indus, [0 for _ in range(n)], label='y=0', color='green')
ax[0][0].scatter(pred_indus, resid_indus, label='Résidus de indus ~ agri', color='blue')
ax[0][0].set(title='Dispersion des résidus indus ~ agri')
ax[0][0].legend()

ax[0][1].hist(resid_indus, label='Résidus de indus ~ agri', color='blue')
ax[0][1].set(title='Histogrammes des résidus indus ~ agri')
ax[0][1].legend()

ax[1][0].plot(pred_agri, [0 for _ in range(n)], label='y=0', color='green')
ax[1][0].scatter(pred_agri, resid_agri, label='Résidus de agri ~ indus', color='orange')
ax[1][0].set(title='Dispersion des résidus agri ~ indus')
ax[1][0].legend()

ax[1][1].hist(resid_agri, label='Résidus de agri ~ indus', color='orange')
ax[1][1].set(title='Histogrammes des résidus agri ~ indus')
ax[1][1].legend()
plt.show()

print(np.mean(resid_indus)) # ~= 0
print(np.mean(resid_agri)) # ~= 0

## --- Niveau de corrélation linéaire du nuage ---

rau = sum(cov['cov_agri_indus']) / ( (sum(cov['var_agri']) * sum(cov['var_indus'])) ** 0.5)
# ou :
#rau = cov_matrix[0][1] / ((cov_matrix[0][0] * cov_matrix[1][1]) ** 0.5)
print('Rau2', rau ** 2)

## --- Etude de la dispersion du nuage ---

R2 = sum([ (reg_agri_indus(indus_i) - centre['x']) ** 2 for indus_i in indus ]) / sum([ (agri_i - centre['x']) **2 for agri_i in agri ])
print('R2', R2)

## --- Valeurs observées/valeurs prédites ---

print('Production industrielle estimée en 1947 :', reg_indus_agri(agri[3]))
print('Production industrielle réelle en 1947 :', indus[3])
print('Rapport :', reg_indus_agri(agri[3]) / indus[3])

print('Production industrielle estimée en 1950 :', reg_indus_agri(agri[6]))
print('Production industrielle réelle en 1950 :', indus[6])
print('Rapport :', reg_indus_agri(agri[6]) / indus[6])


## --- Sensibilité aux valeurs extrêmes ---
#changer indus[3] à 999 et observer la détérioration du modèle


## --- Utilisation d'un modèle d'apprentissage ---

import statsmodels.api as sm

# Create the model here:
model = sm.OLS.from_formula('indus ~ agri', data = {'agri': agri, 'indus': indus})
# Fit the model here:
results = model.fit()
# Print the coefficients here:
print(results.params)

# Prédiction de la production industrielle en 1947 et 1950
newdata = {'agri':[74,102]}
pred_indus_1947, pred_indus_1950 = results.predict(newdata)
print(f'Productions industrielles estimées en 1947 : {pred_indus_1947} et 1950 : {pred_indus_1950}')
