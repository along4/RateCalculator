#########################################################################################################
#	Importing the needed libraries and declaring global objects
#########################################################################################################

#	Importing user Defined Classes
#........................................................................................................
import os, sys
lib_path = os.path.abspath('/afs/crc.nd.edu/user/a/along4/Programs/KiND')
sys.path.append(lib_path)
import KiND

#	Importing other standard Classes
#........................................................................................................
from collections import defaultdict
import numpy as np
import random
from scipy import stats


import ROOT

#........................................................................................................
#	Resonance file to read in.
#........................................................................................................
resInfoFile = '../34Ar+a/ResonanceInfo.dat'

#	Creating a dictionary to read resonance parameters into.
#........................................................................................................
resonances = defaultdict(list)

#	Creating a list of temps to evaluate the reaction rate at.
#........................................................................................................
temps = np.array([.1,.15,.2,.3,.4,.5,.6,.7,.8,.9,1,1.5,2,2.5,3,3.5,4,5,6,7,8,9,10]) # 23 Temperatures

#	Other Globals
#........................................................................................................




#########################################################################################################
#						Auxilary Functions
#########################################################################################################

#	
#........................................................................................................
def getReactionParticipants(reactionString):
	'''
	Function: getReactionParticipants
	Summary: Takes a reaction string, strips the parenthesis, and gets the mass of all constituents 
	Examples: 12C(4He,1H)15N
	Attributes: 
		@param (reactionString): string in the format '12C(4He,1H)15N'
	Returns: a list of masses in amu for the reaction constituents, [target,projectile,ejectile,recoil]
	'''
	target= KiND.mass(reactionString[0:reactionString.index('(')])[0]/931.494061
	projectile = KiND.mass(reactionString[reactionString.index('(')+1:reactionString.index(',')])[0]/931.494061
	ejectile = KiND.mass(reactionString[reactionString.index(',')+1:reactionString.index(')')])[0]/931.494061
	recoil = KiND.mass(reactionString[reactionString.index(')')+1:])[0]/931.494061
	return target,projectile,ejectile,recoil

#	
#........................................................................................................
def calcResonacneEnergy(resonance,exState,Thres):
	res = exState - Thres
	return res

#	
#........................................................................................................
def calcResonanceStrength(jRes,resonances,exState,protonStrength,alphaStrength):

	alphaW = alphaStrength*resonances[exState][jRes]['alpha']
	protonW = protonStrength*resonances[exState][jRes]['proton']
	gammaW = resonances[exState][jRes]['gamma']/1E6
	resStrength = (2*jRes+1)*alphaW*protonW/(alphaW+protonW+gammaW)
	print '%f \t %d \t %e \t %e' % (exState,jRes,alphaW,protonW)
	return resStrength

#	
#........................................................................................................
def calcRateAtTemp(resonanceEnergies,resonanceStrengths,temperature,reducedMass):
	product = 0 
	frontStuff = 1.5399E11/((reducedMass*temperature)**(3.0/2.0))

	for i in range(len(resonanceEnergies)):
			product = product + frontStuff*resonanceStrengths[i]*np.exp(-11.605*resonanceEnergies[i]/temperature)

	return product

#	
#........................................................................................................
def calcReactionRate(resonances,temps,Thres,masses):
	alphaStrength =  0.01
	protonStrength = 0.01
	reducedMass = masses[0]*masses[1]/(masses[0]+masses[1])
	resonanceEnergies = [calcResonacneEnergy(resonances,exState,Thres) for exState in sorted(resonances, key=resonances.get, reverse=False)]
	print "jRes \t Alpha W \t Proton W "
	print "----------------------------"
	resonanceStrengths = [calcResonanceStrength(random.randrange(0,5),resonances,exState,protonStrength,alphaStrength) for exState in sorted(resonances, key=resonances.get, reverse=False)]
	
	# Creating one posibble alpha cluster state
	#i = random.randint(0,4)
	#resonanceStrengths[i] = resonanceStrengths[i]*10

	
	reactionRate = [calcRateAtTemp(resonanceEnergies,resonanceStrengths,temperature,reducedMass) for temperature in temps]
	return reactionRate





#########################################################################################################
#						Main part of program
#########################################################################################################

#	
#........................................................................................................
with open(resInfoFile,'r') as resInfoFile:
	commentData = resInfoFile.readline().split()
	masses = getReactionParticipants(commentData[0])
	alphaThres = float(commentData[2].strip('athres=(MeV)'))
	protonThres = float(commentData[4].strip('pthres=(MeV)'))
	commentline2 = resInfoFile.readline()

	for line in resInfoFile:

		data = line.split()
		res0Parameters = {'alpha':float(data[2]),'proton':float(data[7]),'gamma':float(data[12])}
		res1Parameters = {'alpha':float(data[3]),'proton':float(data[8]),'gamma':float(data[13])}
		res2Parameters = {'alpha':float(data[4]),'proton':float(data[9]),'gamma':float(data[14])}
		res3Parameters = {'alpha':float(data[5]),'proton':float(data[10]),'gamma':float(data[15])}
		res4Parameters = {'alpha':float(data[6]),'proton':float(data[11]),'gamma':float(data[16])}

		resonances.update({float(data[0]):{'error':float(data[1]),0:res0Parameters,1:res1Parameters,2:res2Parameters,3:res3Parameters,4:res4Parameters}})

#
#........................................................................................................
numRate = calcReactionRate(resonances,temps,alphaThres,masses)

print "temps \t Rate "
print "--------------"
for i in range(len(temps)):
	print "%f \t %e" % (temps[i],numRate[i])























