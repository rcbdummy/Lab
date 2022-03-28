# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:31:43 2022

@author: intel
"""

import pandas as pd
PlayTennis = pd.read_csv("new.csv")
print("given data set is :\n",PlayTennis,"\n")
from sklearn.preprocessing import LabelEncoder
Le=LabelEncoder()
PlayTennis['outlook']=Le.fit_transform(PlayTennis['outlook'])
PlayTennis['temp']=Le.fit_transform(PlayTennis['temp'])
PlayTennis['humidity']=Le.fit_transform(PlayTennis['humidity'])
PlayTennis['wind']=Le.fit_transform(PlayTennis['wind'])
PlayTennis['play']=Le.fit_transform(PlayTennis['play'])

print("the encoded dataset is:\n",PlayTennis,"\n")
x=PlayTennis.drop(['play'],axis=1)
y=PlayTennis['play']

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
print("\n x_train:\n",x_train)
print("\n y_train:\n",y_train)
print("\n x_test \n:",x_test)
print("\n  y_test\n:",y_test)
Classifier=GaussianNB()
Classifier.fit(x_train,y_train)
accuracy=accuracy_score(Classifier.predict(x_test),y_test)
print("\n Accuracy is :",accuracy)
