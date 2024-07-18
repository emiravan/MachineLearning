# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:50:13 2020

@author: sadievrenseker
"""

#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")
#test
print(veriler)

x = veriler.iloc[:,1:4].values #bağımsız değişkenler
y = veriler.iloc[:,4:].values #bağımlı değişken
print(y)

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train) # fit eğitmek demek
X_test = sc.transform(x_test) # transform ise o eğitimi kullanmak demek

from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred = logr.predict(X_test)
print(y_pred)
print(y_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

from sklearn.neighbors import KNeighborsClassifier

knn =KNeighborsClassifier(n_neighbors=1,metric='minkowski')
knn.fit(X_train,y_train)

y_pred=knn.predict(X_test)

cm=confusion_matrix(y_test,y_pred)
print(cm)

# SVC
# Kernel = linear
from sklearn.svm import SVC
svc =SVC(kernel='linear')
svc.fit(X_train,y_train) # X_train den y_train'i öğren demek

y_pred =svc.predict(X_test)

cm=confusion_matrix(y_test,y_pred)
print('----------------------------SVC LINEAR----------------------------')
print(cm)

# Kernel = poly
from sklearn.svm import SVC
svc =SVC(kernel='poly')
svc.fit(X_train,y_train) # X_train den y_train'i öğren demek

y_pred =svc.predict(X_test)

cm=confusion_matrix(y_test,y_pred)
print('----------------------------SVC POLY----------------------------')
print(cm)

# Kernel = rbf
from sklearn.svm import SVC
svc =SVC(kernel='rbf')
svc.fit(X_train,y_train) # X_train den y_train'i öğren demek

y_pred =svc.predict(X_test)

cm=confusion_matrix(y_test,y_pred)
print('----------------------------SVC RBF----------------------------')
print(cm)

# Kernel = sigmoid
from sklearn.svm import SVC
svc =SVC(kernel='sigmoid')
svc.fit(X_train,y_train) # X_train den y_train'i öğren demek

y_pred =svc.predict(X_test)

cm=confusion_matrix(y_test,y_pred)
print('----------------------------SVC SIGMOID----------------------------')
print(cm)