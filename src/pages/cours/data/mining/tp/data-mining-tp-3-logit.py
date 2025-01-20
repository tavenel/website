# --- partie I ---

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

students = pd.read_csv('students_hours_exam.csv')

# Scatter plot of exam passage vs number of hours studied
plt.scatter(x = 'hours_studied', y = 'passed_exam', data = students, color='black')
plt.ylabel('Succès/Échec')
plt.xlabel("Heures de révision")

# Fit a linear model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(students[['hours_studied']],students[['passed_exam']])


# Get predictions from the linear model
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1,1)
predictions = model.predict(sample_x)

# Plot the data
plt.scatter(x = 'hours_studied', y = 'passed_exam', data = students, color='black')

# Plot the line
plt.plot(sample_x, predictions, color='red')

# Customization for readability
plt.axhline(y=0, color='k', linestyle='--')
plt.axhline(y=1, color='k', linestyle='--')

# Label plot and set limits
plt.ylabel('Résultat (1=succès, 0=échec)')
plt.xlabel('Heures de révision')
plt.xlim(-1, 25)

pred_0_hr = -0.25
pred_10_hr = 0.5
pred_30_hr = 1.75

plt.show()



# --- partie II ---

# Fit the logistic regression model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(students[['hours_studied']],students[['passed_exam']])

# Plug sample data into fitted model
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1,1)
probability = model.predict_proba(sample_x)[:,1]

# Plot exam data
plt.scatter(students[['hours_studied']], students[['passed_exam']], color='black', s=100)

# Plot logistic curve
plt.plot(sample_x, probability, color='red', linewidth=3)

# Customization for readability
plt.axhline(y=0, color='k', linestyle='--')
plt.axhline(y=1, color='k', linestyle='--')

# Label plot and set limits
plt.ylabel('Probabilité de réussite')
plt.xlabel('Heures de révision')
plt.xlim(-1, 25)

# Show the plot
plt.show()

pred_5_hr_graph = 0.1

log_odds = model.intercept_ + model.coef_ * students[['hours_studied']]

def sigmoid(ll):
    return np.exp(ll)/(1+ np.exp(ll))

pred_proba_reussite = sigmoid(log_odds)

plt.plot(students[['hours_studied']], pred_proba_reussite)
plt.show()

pred_5_hr_model = sigmoid(model.intercept_ + model.coef_ * 5)
print(pred_5_hr_model)

# --- partie III ---

# Séparation de X et Y
X = students[['hours_studied', 'practice_test']]
y = students.passed_exam

# Normalisation de X
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Séparation données d'apprentissage et de test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 27)

# Régression logistique
from sklearn.linear_model import LogisticRegression
cc_lr = LogisticRegression()
cc_lr.fit(X_train, y_train)

# Étude des coefficients
print(cc_lr.intercept_)
print(cc_lr.coef_)

# Prédiction sur les données de test
print(cc_lr.predict(X_test))
print(cc_lr.predict_proba(X_test))
# ou simplement les positifs :
# print(cc_lr.predict_proba(X_test)[:,1])

# Comparaison
print(y_test)

# Threshold 0.6
print((cc_lr.predict_proba(X_test)[:,1]>=0.6).astype(int)) #astype(int) transforme les booléens en entiers
