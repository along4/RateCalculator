from scipy.optimize import fmin
import ROOT
import numpy as np
import matplotlib.pyplot as pyplot


colors_a = ['#ECA949','#ECDB60','#A1CD73','#3F9A82','#427676','#3B596A']
colors_b = ['#00145A','#00305A','#004B8D','#0074D9','#4192D9','#7ABAF2']

#########################################################################################
#	Some Utility functions 
#########################################################################################
def guasDistribution(x,mu,sigma):
	return (0.398942280401432678/sigma)*np.exp(-0.5*(x-mu)**2/sigma**2)

def spinDistribution(Ex,J,A,gamma,aTilde,detlaW,Sn,discreteSigma,Ed):

	U = Ex - 12.0/np.sqrt(A) + 0.90090 

	a = aTilde*(1+detlaW*((1-np.exp(-gamma*U))/U))
	
	spinCut2F = 0.01389*A**(5.0/3.0)/aTilde*np.sqrt(a*U)

	spinCut2 = np.sqrt(discreteSigma**2.0 + (Ex-Ed)/(Sn-Ed)*(spinCut2F - discreteSigma**2.0))

	#print 'a: %.3f \t Sigma: %.3f' % (a,spinCut2)

	rDist = (2*J+1)/(2*spinCut2)*np.exp(-(J+0.5)**2.0/(2*spinCut2))

	return rDist




#########################################################################################
#	Setting some global variables.  
#########################################################################################
sigma = 1
mu = 0
A = 37.976318 				# Mass of 38Ca in amu
gamma = 0.12204				# Damping parameter
aTilde = 4.95218			# Asymptotic level density value
detlaW = 0.13433			# Shell correction energy
NeutronSepEn = 16.99376		# Neutron Separation energy
discreteSigma = 1.58114 	# Discrete spin cut off parameter
energyMiddle = 0.5*(5.6980+4.748000)


dEx = 0.001
exEnergy = np.arange(5,15,dEx);
energyDist0 = spinDistribution(exEnergy, 0, A, gamma, aTilde, detlaW, NeutronSepEn, discreteSigma, energyMiddle)
energyDist1 = spinDistribution(exEnergy, 1, A, gamma, aTilde, detlaW, NeutronSepEn, discreteSigma, energyMiddle)
energyDist2 = spinDistribution(exEnergy, 2, A, gamma, aTilde, detlaW, NeutronSepEn, discreteSigma, energyMiddle)
energyDist3 = spinDistribution(exEnergy, 3, A, gamma, aTilde, detlaW, NeutronSepEn, discreteSigma, energyMiddle)
energyDist4 = spinDistribution(exEnergy, 4, A, gamma, aTilde, detlaW, NeutronSepEn, discreteSigma, energyMiddle)


spinRange = np.arange(0,6,1)
spinDist0 = spinDistribution(7.0, spinRange, A, gamma, aTilde, detlaW,NeutronSepEn, discreteSigma, energyMiddle)
spinDist1 = spinDistribution(9.0, spinRange, A, gamma, aTilde, detlaW,NeutronSepEn, discreteSigma, energyMiddle)
spinDist2 = spinDistribution(11.0, spinRange, A, gamma, aTilde, detlaW,NeutronSepEn, discreteSigma, energyMiddle)
spinDist3 = spinDistribution(13.0, spinRange, A, gamma, aTilde, detlaW,NeutronSepEn, discreteSigma, energyMiddle)
spinDist4 = spinDistribution(15.0, spinRange, A, gamma, aTilde, detlaW,NeutronSepEn, discreteSigma, energyMiddle)

print 

acceptedList = []

i = 0
while i < 1000:
	xi = np.random.uniform(0,6)
	yi = np.random.uniform(0,0.5)
	if yi <= spinDistribution(7.0, xi, A, gamma, aTilde, detlaW,NeutronSepEn, discreteSigma, energyMiddle):
		acceptedList.append(xi)
		i = i + 1

print i

figure = pyplot.figure()
axis1 = pyplot.subplot2grid((4,2), (0,0), colspan=2,rowspan=2)
axis2 = pyplot.subplot2grid((4,2), (2,0), colspan=2, rowspan=2)
pyplot.subplots_adjust(hspace=1.0)

axis1.bar(exEnergy,energyDist0,dEx,label="J = 0",color=colors_a[0],edgecolor=colors_a[0])
axis1.bar(exEnergy,energyDist1,dEx,bottom=energyDist0,color=colors_a[1],edgecolor=colors_a[1],label="J = 1")
axis1.bar(exEnergy,energyDist2,dEx,bottom=energyDist0+energyDist1,color=colors_a[2],edgecolor=colors_a[2],label="J = 2")
axis1.bar(exEnergy,energyDist3,dEx,bottom=energyDist0+energyDist1+energyDist2,color=colors_a[3],edgecolor=colors_a[3],label="J = 2")
axis1.bar(exEnergy,energyDist4,dEx,bottom=energyDist0+energyDist1+energyDist2+energyDist3,color=colors_a[4],edgecolor=colors_a[4],label="J = 2")
#energyDistPlot1, = axis1.bar(exEnergy,energyDist1,0.5,label="J = 1")
#energyDistPlot2, = axis1.bar(exEnergy,energyDist2,0.5,label="J = 2")
#energyDistPlot3, = axis1.bar(exEnergy,energyDist3,0.5,label="J = 3")
#energyDistPlot4, = axis1.bar(exEnergy,energyDist4,0.5,label="J = 4")
axis1.set_ylabel('Probability')
axis1.set_xlabel('Excitation Energy [MeV]')
axis1.set_xlim([6.0,14.0])
axis1.set_ylim([0,1.0])
#axis1.legend([energyDistPlot0,energyDistPlot1,energyDistPlot2,energyDistPlot3,energyDistPlot4],["J = 0","J = 1", "J = 2", "J = 3", "J = 4 "],loc=1,frameon = True,framealpha=0.5)


spinDistPlot0, = axis2.plot(spinRange,spinDist0,label="Ex = 7.0 MeV",color=colors_b[0])
spinDistPlot1, = axis2.plot(spinRange,spinDist1,label="Ex = 9.0 MeV",color=colors_b[1])
spinDistPlot2, = axis2.plot(spinRange,spinDist2,label="Ex = 11.0 MeV",color=colors_b[2])
spinDistPlot3, = axis2.plot(spinRange,spinDist3,label="Ex = 13.0 MeV",color=colors_b[3])
spinDistPlot4, = axis2.plot(spinRange,spinDist4,label="Ex = 15.0 MeV",color=colors_b[4])

axis2.set_ylabel('Probability')
axis2.set_xlabel('Spin')
axis2.set_ylim([0,.50])
figure.set_size_inches(6, 9)


pyplot.legend(frameon=False)
figure.savefig('spinDists.png', dpi=100)
#pyplot.show()

























































