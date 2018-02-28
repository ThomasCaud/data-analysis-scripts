
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt')
lumi = data[:,0]
volt = data[:,1]
mA = data[:,2]

# fig = plt.figure()
# plt.plot(volt,lumi,'+')
# plt.xlabel('volt')
# plt.ylabel('lumi')
# plt.show()

# plt.figure()
# plt.plot(mA,lumi,'+')
# plt.xlabel('mA')
# plt.ylabel('lumi')
# plt.show()

n, = lumi.shape

# Parameter estimator for the volt parameter only
Xvolt = np.matrix(np.concatenate((
        		np.ones((n,1)), 
        		volt.reshape((n,1)), 
        	), axis=1))
thetaVolt = np.multiply(np.linalg.inv(Xvolt.T*Xvolt)*Xvolt.T, lumi) # (Xt*X)^(-1)*Xt*y
lumi_predictor_volt = Xvolt*thetaVolt

# Parameter estimator for the mA parameter only
XmA = np.matrix(np.concatenate((
        		np.ones((n,1)), 
        		mA.reshape((n,1)), 
        	), axis=1))
thetamA = np.multiply(np.linalg.inv(XmA.T*XmA)*XmA.T, lumi) # (Xt*X)^(-1)*Xt*y
lumi_predictor_mA = XmA*thetamA

# Parameter estimator for all the parameters
X = np.matrix(np.concatenate((
        		np.ones((n,1)), 
        		volt.reshape((n,1)), 
        		mA.reshape((n,1))
        	), axis=1))
theta = np.multiply(np.linalg.inv(X.T*X)*X.T, lumi) # (Xt*X)^(-1)*Xt*y
lumi_predictor = X*theta
