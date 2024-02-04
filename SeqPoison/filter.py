# -*- coding: utf-8 -*-
"""

"""

import numpy as np
from collections import Counter
import operator
from functools import reduce
import random

temp = 0

data = []
f = open('Beauty_poison_only1perline_0.03.txt','r')
while(True):
    line = f.readline()
    data_line = line.strip("\n").split()
    data.append([int(i) for i in data_line])
    if not line:
        break
f.close()


data1 = []
f1 = open('generate_epoch80_data_0.2.txt','r')
while(True):
    line = f1.readline()
    data_line = line.strip("\n").split()
    data1.append([int(i) for i in data_line])
    if not line:
        break
f1.close()


f2 = open('111generate_epoch80_data_0.2.txt','a') 
for i in range (0,len(data1)-1): 
    if len(data1[i]) < 6: 
        f2.write("")
    else:
        count = 0
        for j in range (1,len(data1[i])):
            if data1[i][j] == 8887:
                count = count + 1
        if count == 1:
            for j in range (1,len(data1[i])):
                f2.write(str(data1[i][j]))
                f2.write(" ")
            f2.write("\n")
        else:
            f2.write("")
f2.close()


data2 = []
f3 = open('111generate_epoch80_data_0.2.txt','r')
while(True):
    line = f3.readline()
    data_line = line.strip("\n").split()
    data2.append([int(i) for i in data_line])
    if not line:
        break
f3.close()


file = open('111Beauty_poison_only1perline_0.03.txt','a') 
for i in range (0,len(data)-1): 
    count = 0
    for j in range (1,len(data[i])):
        if data[i][j] == 8887:
            count = count + 1
    if len(data[i]) < 6 or count > 1:
        temp = temp + 1
        file.write(str(data[i][0]))
        file.write(" ")
        for k in range (0,len(data2[temp])):
            file.write(str(data2[temp][k]))
            file.write(" ")
        file.write("\n")
    else:
        for j in range (0,len(data[i])):
            file.write(str(data[i][j]))
            file.write(" ")
        file.write("\n")
file.close()

        






