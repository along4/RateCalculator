#####################################################################################
#		
#
#
#####################################################################################
import math
import numpy as np
import collections


#	Calculating reduced Mass given to masses (in AMU) of the nuclei involed.
m0 = 33.9802
m1 = 4.00260
reducedMass = math.sqrt((m1+m0)/(m1*m0))

#	Ordered Dictionary to store XC and Ecm in.
crossSecDict = collections.OrderedDict()

#	Output file from AZURE2 
azureFile = "../34Ar+a/RmatrixRate/Output/AZURE2_34Ar+a.dat"

#	setting the constant used in eq. 3.10 in Iliadis. 
constant = 3.7318E10

#	setting up a lists of temperatures [in T9] to calculate the rate at. 
temperatures = np.array([.1,.15,.2,.3,.4,.5,.6,.7,.8,.9,1,1.5,2,2.5,3,3.5,4,5,6,7,8,9,10]) # 23 Temperatures




#####################################################################################
#	utility functions.
#####################################################################################

def calcReacRateAtTemp(temp,cXDict,numPoints):

	deltaE = (crossSecDict.keys()[-1]-crossSecDict.keys()[0])/numPoints

	frontStuff = constant*reducedMass/(temp**(3.0/2.0))
	intergral = 0
	for energyCM,crossSec in crossSecDict.items():
		intergrand = energyCM*crossSec*math.exp(-11.605*energyCM/temp)*deltaE
		intergral = intergral+intergrand


	return frontStuff*intergral


#####################################################################################
#	Main function.
#####################################################################################

#	Opening and reading in cross section data from AZURE2
numPoints = 0
with open(azureFile) as azureXCFile:
	for line in azureXCFile:
		numPoints = numPoints + 1
		data = line.split()
		crossSecDict.update({float(data[0]):float(data[3])})


#	Calculating reaction rates at each temp in temp list.
for temps in temperatures:
	rate = calcReacRateAtTemp(temps, crossSecDict,numPoints)
	print "%.2f\t%e" % (temps, rate)

print (crossSecDict.keys()[-1]-crossSecDict.keys()[0])


















































