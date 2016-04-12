import os, sys

from collections import defaultdict
import numpy as np

from matplotlib import pyplot
#import matplotlib.colors as cl
from matplotlib.ticker import LogLocator, FormatStrFormatter, MaxNLocator
from matplotlib import gridspec




energyCM = []
energyEx = []
crossSection = []
sFactor = []


azureOutput = "../34Ar+a/RmatrixRate/Output/AZURE2_34Ar+a.dat"
colors = ['#2c7bb6','#abcae9','#d7191c','#fdae61','#ffffbf','#4110B2']



with open(azureOutput) as inputFile:
	comments = inputFile.readline()
	for line in inputFile:
		data = line.split()
		energyCM.append(float(data[0]))
		energyEx.append(float(data[1]))
		crossSection.append(float(data[3]))
		sFactor.append(float(data[4]))



figure = pyplot.figure()
axis1 = pyplot.subplot()
axis1.set_yscale('log')
axis1.set_xlabel('Energy Center-of-Mass [MeV]',fontsize=20)
axis1.set_ylabel('S-Factor [MeV b]',fontsize=20)
pyplot.xticks( fontsize = 20)
pyplot.yticks( fontsize = 20)

sFactorCM, = axis1.plot(energyCM,sFactor, color=colors[2], linewidth=1.5,linestyle="-", label = '34Ar(a,p) Cross-Section')



pyplot.show()