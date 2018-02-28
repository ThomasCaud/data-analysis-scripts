
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt')
lumi = data[:,0]
volt = data[:,1]
mA = data[:,2]

plt.figure()
plt.plot(volt,lumi,'+')
plt.show()

plt.figure()
plt.plot(mA,lumi,'+')
plt.show()

n, = lumi.shape

X = np.matrix(np.concatenate(
        ( np.ones((n,1)), volt.reshape((n,1)), mA.reshape((n,1)) ), 
        axis=1))

theta = np.linalg.inv(X.T*X)*X.T*lumi

lumi_predictor = X*theta



