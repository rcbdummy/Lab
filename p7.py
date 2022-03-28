#7) Kmeans Program:

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
data=pd.read_csv('7.csv')
print("input data and shape")
print(data.shape)
data.head()
f1=data['V1'].values 
f2=data['V2'].values 
X=np.array(list (zip(f1,f2)))

print("X",X)
print("graph for whole data")
plt.scatter(f1,f2,c='black',s=7)
plt.show()
kmeans=KMeans(20,random_state=0)
lables=kmeans.fit(X).predict(X)
print("lables",lables)

centroids=kmeans.cluster_centers_
print("centroids", centroids)
plt.scatter(X[:,0],X[:,1],c=lables,s=40,cmap='viridis');
print("graph using kmeans algoritm")

plt.scatter(centroids[:,0],centroids[:,1],marker='*',s=200,c='#050505')
plt.show()

gmm=GaussianMixture(n_components=3).fit(X)
lables=gmm.predict(X)
probs=gmm.predict_proba(X)
size=10*probs.max(1)**3
print("graph using em")
plt.scatter(X[:,0],X[:,1],c=lables,s=size,cmap='viridis')
plt.show()

