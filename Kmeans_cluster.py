# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:36:52 2023

@author: yanliwang7
"""

from sklearn.cluster import KMeans
import numpy as np
 



data = []
f = open('5_padding_Beauty.txt','r')
while(True):
    line = f.readline()
    data_line = line.strip("\n").split()
    data.append([int(i) for i in data_line])
    if not line:
        break
f.close()

data = np.concatenate(data,axis = 0)
data = data.reshape((22363,5))
#print(data)


x = data


clf = KMeans(n_clusters=12)
clf.fit(x)  
 
centers = clf.cluster_centers_ 
labels = clf.labels_  
print(centers)
print(labels)

f = open('Kmeans_Beauty_label_12.txt','a')
for i in range (0,len(labels)):
    f.write(str(labels[i]))
    f.write("\n")
f.close()
 



