
import numpy as np
import matplotlib.pyplot as plt

def displayPlots():
        fig = plt.figure()
        plt.plot(volt,lumi,'+')
        plt.xlabel('volt')
        plt.ylabel('lumi')
        plt.show()

        plt.figure()
        plt.plot(mA,lumi,'+')
        plt.xlabel('mA')
        plt.ylabel('lumi')
        plt.show()
        return

def regLinSimple(Y,x, n):
        # Calcul de la moyenne
        meanY = np.mean(Y)
        meanx = np.mean(x)

        # Calcul de la covariance
        covariancexY = (np.sum(x*Y)) / n-(meanY*meanx)

        # Calcul de sigma
        b = covariancexY / np.var(x)
        a = np.mean(Y) - b*meanx
        sigma = (np.sum((Y-a-b*x)**2))/n        

        # Calcul de l'erreur quadratique
        quadratic_error = np.sum((Y-a-b*x)**2)

        # Calcul de la prediction
        lumi_predictor = a*x+b

        print("a estimation: ",a)
        print("b estimation: ",b)
        print("sigma estimation: ",sigma)
        print("Quadratic error: ",quadratic_error)
        print("Lumi predictor: ",lumi_predictor)

        return

data = np.loadtxt('data.txt')
lumi = data[:,0]
volt = data[:,1]
mA = data[:,2]
n, = lumi.shape

print("[RLS] Luminosite ambiante en fonction de la tension à vide")
regLinSimple(lumi, volt, n)

print("[RLS] Luminosite ambiante en fonction du courant de court-circuit du capteur")
regLinSimple(lumi,mA, n)

# Parameter estimator for all the parameters
# Regression model: lum_i = Θ_0 + x_i(1) Θ_1 + x_i(2) Θ_2 + E_i
Y = lumi

X = np.matrix(np.concatenate((
        		np.ones((n,1)),
        		volt.reshape((n,1)),
        		mA.reshape((n,1))
        	), axis=1))
theta = np.multiply(np.linalg.inv(X.T*X)*X.T, Y) # (Xt*X)^(-1)*Xt*y
lumi_predictor = X*theta
quadratic_error = (Y - X*theta).T * (Y - X*theta)
print("Regression lineaire multiple de la luminosite ambiante en fonction de ces deux paramètres")
#print("Lumi predictor: ", lumi_predictor)
#print("Quadratic error: ", quadratic_error)
