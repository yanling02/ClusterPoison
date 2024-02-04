# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:14:08 2023


@author: yanliwang7
"""

import numpy as np


from pyclustering.cluster.clique import clique

from pyclustering.cluster.clique import clique_visualizer


data = []
f = open('10_padding_Sports_and_Outdoors.txt','r')
while(True):
    line = f.readline()
    data_line = line.strip("\n").split()
    data.append([int(i) for i in data_line])
    if not line:
        break
f.close()

data = np.concatenate(data,axis = 0)
data = data.reshape((35598,10))   ##22363 for Beauty  35598 for Sports
#print(data)


data_M = data

intervals = 5

threshold = 
clique_instance = clique(data_M, intervals, threshold)

clique_instance.process()
clique_cluster = clique_instance.get_clusters()  # allocated clusters


noise = clique_instance.get_noise()

cells = clique_instance.get_cells() 

print("Amount of clusters:", len(clique_cluster))
print(clique_cluster)

f = open('Clique_Sports_padding-10_interval-5.txt','a')
for i in range (0,len(clique_cluster)):
    for j in range (0,len(clique_cluster[i])):
        f.write(str(clique_cluster[i][j]))
        f.write(" ")
    f.write("\n")
f.close()
