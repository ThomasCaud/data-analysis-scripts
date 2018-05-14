# -*-coding:Latin-1 -*
import matplotlib as mpl
import numpy as np

def regLinSimple(Y,x):
	n, = Y.shape
	meanY = np.mean(Y)
	meanx = np.mean(x)

	covariancexY = (np.sum(x*Y)) / n-(meanY*meanx)
	bEstimate = covariancexY / np.var(x)
	aEstimate = np.mean(Y) - bEstimate*meanx
	sigma = (np.sum((Y-aEstimate-bEstimate*x)**2))/n	
	
	quadratic_error = np.sum((Y-aEstimate-bEstimate*x)**2)

	lumi_predictor = aEstimate*x+bEstimate

	print("estimateur de a: ",aEstimate)
	print("estimateur de b: ",bEstimate)
	print("estimateur de sigma: ",sigma)
	print("erreur quadratique: ",quadratic_error)
	print("prediction: ",lumi_predictor)

def regLinMultiple(Y,u,v):
	n, = Y.shape
	Y = Y.reshape((n,1))
	
	X = np.matrix(np.concatenate((np.ones((n,1)),u.reshape((n,1)),v.reshape((n,1))), axis=1))	
	P = np.linalg.inv(X.T*X)*X.T
	theta = P*Y
	estim_theta = np.asarray(theta).reshape(-1)

	I = np.eye(n,n)
	R = I-X*P
	epsilon = np.asarray(R*Y).reshape(-1) # permet de transformer la matrice R*Y en vecteur
	estim_sigma = (np.sum(epsilon**2))/(n-3)
	
	erreur_quadratique = (Y-X*theta).T*(Y-X*theta)

	lumi_predictor=np.asarray(X*theta).reshape(-1)
	
	print("estimateurs de theta=",estim_theta)
	print("estimateur du maximum de vraisemblance=",estim_sigma)
	print("erreur quadratique=",erreur_quadratique[0,0]) # matrice composee d'un unique element
	print("prediction=",lumi_predictor)

	return

data = np.loadtxt('data.txt')
lumi = data[:,0]
volt = data[:,1]
mA = data[:,2]

print("Regression lineaire simple de la luminosite ambiante en fonction de la tension a vide aux bornes du capteur")
regLinSimple(lumi,volt)

print("Regression lineaire simple de la luminosite ambiante en fonction du courant de court-circuit du capteur")
regLinSimple(lumi,mA)

print("Regression lineaire multiple de la luminosite ambiante en fonction de la tension a vide et du courant de court-circuit aux bornes du capteur")
regLinMultiple(lumi,volt,mA)
