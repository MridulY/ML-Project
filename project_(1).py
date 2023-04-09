# -*- coding: utf-8 -*-
"""Project (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Etu-8mP_6L_Wrb7ZQ6wEDevJX4C-MDBp
"""

import numpy as np
import pandas as pd
dataset1 = pd.read_csv("dataTraining1.csv")

dataset1.head() #first 5 column

dataset1.tail()#last 5 columns

dataset1.isnull().sum()

df=dataset1.drop(['Column1','_1','_2','_3','_4','Spatial Distribution','Temporal Distribution'],axis=1)  #removing useless column to minimize dataset

df.shape

df.dtypes

df.info() #count and datatype of dataset

from sklearn.impute import SimpleImputer
si=SimpleImputer(strategy='most_frequent')
df_im=si.fit_transform(df)

df_im=pd.DataFrame(df_im)

data=df_im

target=df_im[0]

df.head()

import matplotlib.pyplot as plot
from sklearn import linear_model

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(data,target,test_size=0.3)

x_train.shape

x_test.shape

from sklearn.linear_model import Perceptron

p1=Perceptron(penalty='l1')

df

p1.fit(x_train,y_train)

from sklearn.metrics import accuracy_score

train_pred=p1.predict(x_train)

train_pred=p1.predict(x_test)

X=df
y=df['T/R']
from sklearn.linear_model import LogisticRegression

from sklearn import preprocessing
from sklearn import utils

#convert y values to categorical values
lab = preprocessing.LabelEncoder()
y = lab.fit_transform(y)

#split the dataset in the Training and testing 
from sklearn.model_selection import train_test_split
X_train , X_test ,y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)
print(np.shape(X))
print(np.shape(X_test))
print(np.shape(X_train))

#Create the object of StandardScaler class for independent variables or features
from sklearn.preprocessing import StandardScaler 
sc=StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

### SVM (Support Vector Machine)
from sklearn.svm import SVC
svm = SVC(kernel='linear', C=1,random_state=0)
svm.fit(X_train_std,y_train)
y_pred=svm.predict(X_test_std)
print('misclassified samples: %d'%(y_test!=y_pred).sum())
from sklearn.metrics import accuracy_score
print('Accuracy:%.2f'%accuracy_score(y_test,y_pred))

### KNN (K-Nearest Neighbors)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
knn1=KNeighborsClassifier(n_neighbors=3)
knn1.fit(X_train_std,y_train)
y_pred=knn1.predict(X_test_std)
print('misclassified samples: %d'%(y_test!=y_pred).sum())
from sklearn.metrics import accuracy_score
print('Accuracy:%.2f'%accuracy_score(y_test,y_pred))

### Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(X,y)
model = LogisticRegression(solver='liblinear', random_state=0).fit(X, y)
model.predict_proba(X)
model.predict(X)
model.score(X,y)
print(classification_report(y, model.predict(X)))
model.score(X,y)

from sklearn.ensemble import RandomForestClassifier #algorithm of hyperparameter tuning
from sklearn.model_selection import GridSearchCV #Cv: Cross Validation
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)

# Define the hyperparameters to tune
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10]
}
# Create a random forest classifier object
rfc = RandomForestClassifier()

# Perform a grid search with cross-validation to find the best hyperparameters
grid_search = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Print the best hyperparameters and their corresponding accuracy score on the validation set
print("Best hyperparameters:", grid_search.best_params_)
y_pred = grid_search.predict(X_val)
print("Validation accuracy score:", accuracy_score(y_val, y_pred))