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
#	Files to read in and read out to.
#........................................................................................................
resInfoFile = '../34Ar+a/ResonanceInfo.dat'


outputRootFile = "../34Ar+a/calcRate/"+ sys.argv[1] + ".root"

#	Creating a dictionary to read resonance parameters into.
#........................................................................................................
resonances = defaultdict(list)

#	Creating a list of temps to evaluate the reaction rate at.
#........................................................................................................
temps = np.array([.1,.15,.2,.3,.4,.5,.6,.7,.8,.9,1,1.5,2,2.5,3,3.5,4,5,6,7,8,9,10]) # 23 Temperatures

#	Other Globals
#........................................................................................................
n = int(sys.argv[2])	# NUMBER OF TIME TO CALCULATE THE REACTION RATE
reactionRateSamples = []	# list to store reaction rate calculations.



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
def calcResonacneEnergy(exState,Thres):
	res = exState - Thres
	return res

#	
#........................................................................................................
def calcResonanceStrength(jRes,resonances,exState,protonStrength,alphaStrength):

	alphaW = alphaStrength*resonances[exState][jRes]['alpha']
	protonW = protonStrength*resonances[exState][jRes]['proton']
	gammaW = resonances[exState][jRes]['gamma']/1E6
	resStrength = (2*jRes+1)*alphaW*protonW/(alphaW+protonW+gammaW)
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
	resonanceEnergies = [calcResonacneEnergy(exState,Thres) for exState in sorted(resonances, key=resonances.get, reverse=False)]
	resonanceStrengths = [calcResonanceStrength(getFGasSpin(exState),resonances,exState,protonStrength,alphaStrength) for exState in sorted(resonances, key=resonances.get, reverse=False)]
	#resonanceStrengths = [calcResonanceStrength(random.randrange(0,5),resonances,exState,protonStrength,alphaStrength) for exState in sorted(resonances, key=resonances.get, reverse=False)]
	
	#Creating one posibble alpha cluster state
	#.........................................
	#i = random.randint(0,4)
	#resonanceStrengths[i] = resonanceStrengths[i]*10

	# A testing print statement
	# .........................
	#for i in range(len(resonanceEnergies)):
	#	print '%e\t%e' % (resonanceEnergies[i],resonanceStrengths[i])

	reactionRate = [calcRateAtTemp(resonanceEnergies,resonanceStrengths,temperature,reducedMass) for temperature in temps]
	return reactionRate

#	
#........................................................................................................
def getFGasSpin(exEnergy):
	A = 37.976318 				# Mass of 38Ca in amu
	gamma = 0.12204				# Damping parameter
	aTilde = 4.95218			# Asymptotic level density value
	detlaW = 0.13433			# Shell correction energy
	NeutronSepEn = 16.99376		# Neutron Separation energy
	discreteSigma = 1.58114 	# Discrete spin cut off parameter
	energyMiddle = 0.5*(5.6980+4.748000)

	U = exEnergy - 12.0/np.sqrt(A) + 0.90090 
	a = aTilde*(1+detlaW*((1-np.exp(-gamma*U))/U))
	spinCut2F = 0.01389*A**(5.0/3.0)/aTilde*np.sqrt(a*U)
	spinCut2 = np.sqrt(discreteSigma**2.0 + (exEnergy-energyMiddle)/(NeutronSepEn-energyMiddle)*(spinCut2F - discreteSigma**2.0))
	

	flag = True
	while (flag == True):
		J = np.random.randint(0,4)
		yi = np.random.uniform(0,0.5)
		spinProb = (2*J+1)/(2*spinCut2)*np.exp(-(J+0.5)**2.0/(2*spinCut2))
		# testing print statement
		#print exEnergy, spinProb, yi
		if yi <= spinProb:
			spin = int(J)
			flag = False

	return spin



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
outputfile = ROOT.TFile(outputRootFile,"recreate")
tempTree = ROOT.TTree("temps", "Reaction rate of 30S(a,p) at various temps")

#	
#........................................................................................................
t0010 = np.zeros(1, dtype=float)
t0015 = np.zeros(1, dtype=float)
t0020 = np.zeros(1, dtype=float)
t0030 = np.zeros(1, dtype=float)
t0040 = np.zeros(1, dtype=float)
t0050 = np.zeros(1, dtype=float)
t0060 = np.zeros(1, dtype=float)
t0070 = np.zeros(1, dtype=float)
t0080 = np.zeros(1, dtype=float)
t0090 = np.zeros(1, dtype=float)
t0100 = np.zeros(1, dtype=float)
t0150 = np.zeros(1, dtype=float)
t0200 = np.zeros(1, dtype=float)
t0250 = np.zeros(1, dtype=float)
t0300 = np.zeros(1, dtype=float)
t0350 = np.zeros(1, dtype=float)
t0400 = np.zeros(1, dtype=float)
t0500 = np.zeros(1, dtype=float)
t0600 = np.zeros(1, dtype=float)
t0700 = np.zeros(1, dtype=float)
t0800 = np.zeros(1, dtype=float)
t0900 = np.zeros(1, dtype=float)
t1000 = np.zeros(1, dtype=float)

#	
#........................................................................................................
tempTree.Branch('temp_0010', t0010, 't9_0010/D')
tempTree.Branch('temp_0015', t0015, 't9_0015/D')
tempTree.Branch('temp_0020', t0020, 't9_0020/D')
tempTree.Branch('temp_0030', t0030, 't9_0030/D')
tempTree.Branch('temp_0040', t0040, 't9_0040/D')
tempTree.Branch('temp_0050', t0050, 't9_0050/D')
tempTree.Branch('temp_0060', t0060, 't9_0060/D')
tempTree.Branch('temp_0070', t0070, 't9_0070/D')
tempTree.Branch('temp_0080', t0080, 't9_0080/D')
tempTree.Branch('temp_0090', t0090, 't9_0090/D')
tempTree.Branch('temp_0100', t0100, 't9_0100/D')
tempTree.Branch('temp_0150', t0150, 't9_0150/D')
tempTree.Branch('temp_0200', t0200, 't9_0200/D')
tempTree.Branch('temp_0250', t0250, 't9_0250/D')
tempTree.Branch('temp_0300', t0300, 't9_0300/D')
tempTree.Branch('temp_0350', t0350, 't9_0350/D')
tempTree.Branch('temp_0400', t0400, 't9_0400/D')
tempTree.Branch('temp_0500', t0500, 't9_0500/D')
tempTree.Branch('temp_0600', t0600, 't9_0600/D')
tempTree.Branch('temp_0700', t0700, 't9_0700/D')
tempTree.Branch('temp_0800', t0800, 't9_0800/D')
tempTree.Branch('temp_0900', t0900, 't9_0900/D')
tempTree.Branch('temp_1000', t1000, 't9_1000/D')

#	Calculation the reaction rate and filling TTree branches in the .root file
#........................................................................................................
for i in range(n):
	numRate = calcReactionRate(resonances,temps,alphaThres,masses)
	
	#	Setting reaction rates at various temps to each branch
	#......................
	t0010[0] = numRate[0]
	t0015[0] = numRate[1]
	t0020[0] = numRate[2]
	t0030[0] = numRate[3]
	t0040[0] = numRate[4]
	t0050[0] = numRate[5]
	t0060[0] = numRate[6]
	t0070[0] = numRate[7]
	t0080[0] = numRate[8]
	t0090[0] = numRate[9]
	t0100[0] = numRate[10]
	t0150[0] = numRate[11]
	t0200[0] = numRate[12]
	t0250[0] = numRate[13]
	t0300[0] = numRate[14]
	t0350[0] = numRate[15]
	t0400[0] = numRate[16]
	t0500[0] = numRate[17]
	t0600[0] = numRate[18]
	t0700[0] = numRate[19]
	t0800[0] = numRate[20]
	t0900[0] = numRate[21]
	t1000[0] = numRate[22]

	# Filling tree
	#.............
	tempTree.Fill()

#	
#........................................................................................................
outputfile.Write()
outputfile.Close()






















