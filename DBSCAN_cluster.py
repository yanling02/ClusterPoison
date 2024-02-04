# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 18:02:12 2023

@author: yanliwang7
"""

import numpy as np 
import sklearn.cluster as skc  
from sklearn import metrics 



f = open('5_padding_Sports_t_SNE_to_2axis.txt','r')
file = open('5_padding_Sports_t_SNE_to_2axis111.txt','a') 
while(True):
    line = f.readline()
    line = line.replace('[','')
    line = line.replace(']','')
    file.write(line)
    if not line:
        break
f.close()
file.close()  




data = []
f = open('5_padding_Sports_t_SNE_to_2axis111.txt','r')
while(True):
    line = f.readline()
    data_line = line.strip("\n").split()
    data.append([float(i) for i in data_line])
    if not line:
        break
f.close()

data = np.concatenate(data,axis = 0)
data = data.reshape((35598,2))

X = np.array(data)

db = skc.DBSCAN(eps=0.0021, min_samples=2).fit(X)

labels = db.labels_  




f = open('DBSCAN_Sports_label.txt','a') 
for i in range (0,len(labels)):
    f.write(str(labels[i]))
    f.write("\n")
f.close()
 
