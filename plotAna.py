#!/usr/bin/env python

#imports
#************************************************************************************

import sys
import matplotlib.pyplot as plt
import scipy as si
import numpy as np
import scipy.stats as sit
import math

#************************************************************************************

#Prompt for file
#************************************************************************************

if len(sys.argv) != 2:
    fName = raw_input("filename: ")
else:
    fName = sys.argv[1]

#************************************************************************************


#Read and organize imported file into dictionary
#************************************************************************************

portFreakMap = {}

with open(fName, 'r') as f:
    for line in f:
        line = line.split(',')
        portFreakMap[int(line[0])] = int(line[1]) 


#pfm = (portFreakMap[int(line[0])]=int(line[1]))
pfm = portFreakMap      
#************************************************************************************


#Plot 
#************************************************************************************

plt.grid(True)
plt.title('Frequency of {0}:'.format(fName))

plt.bar(range(len(pfm)), pfm.values(), align='center')
plt.xticks(range(len(pfm)), pfm.keys())

plt.show()

#************************************************************************************
