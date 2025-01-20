from sklearn import datasets

#Load dataset
wine = datasets.load_wine()
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3) # 70% training and 30% test

from sklearn.neighbors import KNeighborsClassifier

#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=5)

#Train the model using the training sets
knn.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = knn.predict(X_test)
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
##Accuracy: 0.7037037037037037
# k=7 : Accuracy: 0.777777777778
# Accuracy(k=7) > Accuracy(k=5) : le modèle k=7 est meilleur que k=5 
# Accuracy(k=8) : 0.6851851851851852 => on garde le modèle k=7
