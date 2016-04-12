from scipy.optimize import fmin
import numpy as np
import matplotlib.pyplot as plt




#########################################################################################
#	Some Utility functions 
#########################################################################################
def guasDistribution(x,mu,sigma):
	return (0.398942280401432678/sigma)*np.exp(-0.5*(x-mu)**2/sigma**2)

def spinDistribution(Ex,J,A,gamma,aTilde,detlaW):

	U = Ex - 2*12.0/np.sqrt(A)

	a = aTilde*(1+detlaW*((1-np.exp(-gamma*U))/U))
	
	spinCut2 = 0.01389*A**(5/3)/aTilde*np.sqrt(a*U)

	print 'a: %.3f \t Sigma: %.3f' % (a,spinCut2**0.25)

	rDist = (2*J+1)/(2*spinCut2)*np.exp(-(J+0.5)**2/(2*spinCut2))

	return rDist




#########################################################################################
#	Setting some global variables.  
#########################################################################################
sigma = 1
mu = 0
A = 38
gamma = 0.12204
aTilde = 4.95218
detlaW = 0.13433
x = np.arange(0,5,.1);
y1 = spinDistribution(4.8600, x, A, gamma, aTilde, detlaW)
y2 = spinDistribution(4.8990, x, A, gamma, aTilde, detlaW)
y3 = spinDistribution(5.1590, x, A, gamma, aTilde, detlaW)
y4 = spinDistribution(9.5263, x, A, gamma, aTilde, detlaW)




acceptedList = []

#for i in range(100000):
#	xi = np.random.uniform(-5,5)
#	yi = np.random.uniform(0,0.5*guasDistribution(mu, mu, sigma))
#	if yi <= guasDistribution(xi, mu, sigma):
#		acceptedList.append(xi)



plt.semilogy(x,y1,label="Ex = 6 MeV")
plt.ylabel('Probability')
plt.xlabel('Spin')
plt.semilogy(x,y2,label="Ex = 8 MeV")
plt.semilogy(x,y3,label="Ex = 10 MeV")
plt.semilogy(x,y4,label="Ex = 12 MeV")
plt.legend()
#plt.show()

























































