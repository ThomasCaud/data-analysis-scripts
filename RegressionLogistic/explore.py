import numpy as np
from numpy import exp, log
# import scipy as scipy
# from scipy import optimize

data = np.loadtxt('data.txt')
hasSucceeded = data[:,0]
isNotGI = data[:,1]
semesterNumber = data[:,2]
n, = hasSucceeded.shape

# Question 3 - Calcul de la vraisemblance
def probX(alpha):
	return (exp(alpha))/(1+exp(alpha))

def probXi(alpha,Yi):
	return (probX(alpha)**(Yi))*((1-probX(alpha))**(1-Yi))

def vraisemblance(theta):
	a,b,c = theta
	# todo: vérifier l'intégrité de l'utilisation de semesterNumber, qui n'est pas une variable booléenne !
	alpha = a + b*isNotGI + c*semesterNumber
	return np.prod(probXi(alpha, hasSucceeded))

# Ebauche question 4 - logvraisemblance
def logvraisemblance(theta):
	a,b,c = theta
	# todo: vérifier l'intégrité de l'utilisation de semesterNumber, qui n'est pas une variable booléenne !
	alpha = a + b*isNotGI + c*semesterNumber
	return np.sum(hasSucceeded*(alpha) + log(1-(1/(1+exp(-(alpha))))))

# scipy.optimize.minize(-1 * logvraisemblance, (0,0,0))

