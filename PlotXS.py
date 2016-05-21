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


azureOutput = "../34Ar+a/RmatrixRate/Output/test.dat"
colors = ['#2c7bb6','#abcae9','#d7191c','#fdae61','#ffffbf','#4110B2']



with open(azureOutput) as inputFile:
	comments = inputFile.readline()
	for line in inputFile:
		data = line.split()
		energyCM.append(float(data[0]))
		energyEx.append(float(data[1]))
		crossSection.append(float(data[3]))
		sFactor.append(float(data[4]))



figure = pyplot.figure(figsize=(8, 10))
axis1 = pyplot.subplot2grid((3,2), (0,0), colspan=2,rowspan=2)
axis2 = pyplot.subplot2grid((3,2), (2,0), colspan=2, sharex=axis1)
pyplot.subplots_adjust(hspace=0.0)
pyplot.setp(axis1.get_xticklabels(), visible=False)
pyplot.setp(axis2.get_xticklabels(), visible=False)
axis1.set_yscale('log')
#axis1.set_xscale('log')
axis2.set_yscale('log')
#axis2.set_xscale('log')
axis1.set_xlim([-5,11.0])

axis1.set_ylim([5E-32,1E2])

axis2.set_ylim([1E-10,5E2])



axis2.set_xlabel('Energy Center-of-Mass [MeV]',fontsize=20)
axis1.set_ylabel('Cross Section [b]',fontsize=20)
axis2.set_ylabel('S-Factor [MeV b]',fontsize=20)

#pyplot.xticks( fontsize = 20)
#pyplot.yticks( fontsize = 20)

sFactorCM, = axis1.plot(energyCM,crossSection, color="#457F75", linewidth=3,linestyle="-", label = '34Ar(a,p) Cross-Section')

sFactorCM, = axis2.plot(energyCM,sFactor, color="#457F75", linewidth=3,linestyle="-", label = '34Ar(a,p) Cross-Section')



#pyplot.show()
pyplot.savefig("sampleSFactor.pdf")