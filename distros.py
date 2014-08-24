!#/usr/bin/env python

#distros.py
#Test-Case using the SSL protocol, which may be assigned to any port.
#Algorithm for Targeted Probabilistic Reordering of Ports
#For the purpose of finding the assigned SSL ports

#imports
#************************************************************************************

import sys
import matplotlib.pyplot as plt
import scipy as sip
import numpy as np
import scipy.stats as sat
import math

#************************************************************************************

#Prompt for file
#************************************************************************************

if len(sys.argv) != 2:
    fName = raw_input("filename: ")
else:
    fName = sys.argv[1]

#************************************************************************************

#Read and Organize file into dictionary format
#************************************************************************************

portFreqMap = {}

with open(fName, 'r') as f:
    for line in f:
    line = line.split(',')
    portFreqMao[int(line[0])]=int(line[1])


pfm = portFreqMap

#************************************************************************************

#Plot Preliminary Plot and Check Distribution (manually for now, will automate to check against a list of discrete distributions, run goodness of fit test, and then pick the best distribution

plt.title('Frequency of {0}:'.format(fName))
plt.bar(range(len(pfm)), pfm.values(), align = 'center')
plt.xticks(range(len(pfm)), pfm.keys())

plt.show()

#************************************************************************************

#Insert the distro, this part is chosen manually (for now): A random distribution is generated over the correct range and scale for each Subsection of ports
#************************************************************************************

#For SystemPortsAll use the distribution (Oh Crap its in THAT notebook, fuck)

#For Sub_1 of RegisteredPortsSub1 use the distribution (Same Oh Shit Statement)

#For Sub_2 of RegisteredPortsSub2 use the distribution (Same Oh Shit Statement)

#For DynamicPortsAll use the distribution (Same Oh Shit Statement)

#For SeedPortsAll use the distribution (Same Oh Shit Statement)

#************************************************************************************

#MLE Fitting: This part fits the model to the data
#************************************************************************************

#MLE for SystemPortsAll random distribution

#MLE for Sub_1 of RegisteredPortsSub1

#MLE for Sub_2 of RegisteredPortsSub2

#MLE for DynamicPortsAll

#MLE for SeedPortsAll

#************************************************************************************

#Complete Fitted Model
#************************************************************************************

#Fitted Model for SystemPortsAll

#Fitted Model for Sub_1 of RegisteredPortsSub1

#Fitted Model for Sub_2 of RegisteredPortsSub2

#Fitted Model for DynamicPortsAll

#Fitted Model for SeedPortsAll

#************************************************************************************

#Port Reordering by SubSection
#************************************************************************************

#SystemPortsAll Reordering

#RegisteredPortsSub1 Reordering

#RegisteredPortsSub2 Reordering

#DynamicPortsAll Reordering

#SeedPortsAll Reordering

#************************************************************************************

#Total Reordering by Probability
#************************************************************************************

#Ordered from most probable to least probable


#************************************************************************************

#Conclusion Result Plots
#************************************************************************************

#Plot SystemPortsAll with Distro

#Plot Sub_1 of RegisteredPortsSub1 with Distro

#Plot Sub_2 of RegisteredPortsSub2 with Distro

#Plot DynamicPortsAll with Distro

#Plot SeedPortsAll with Distro

#Composite Plot of reordering with Distros

#************************************************************************************

