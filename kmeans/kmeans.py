import random

import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.stdout.flush()

def generatePoints(N):
	X = random.sample(range(1, 100), N)
	Y = random.sample(range(1, 100), N)
	return list(zip(X, Y))

def getBarycentre(points, N):
	sumX = 0
	sumY = 0
	for X, Y in points:
		sumX += X
		sumY += Y
	return (sumX/N, sumY/N)

def getInitBarycentres(points, N, K):
	barycentres = []
	for i in range(K):
		randomInt = random.randint(0, N-1)
		barycentres.append(points[randomInt])

	return barycentres

# Number of points
N = 50

# Number of clusters
K = 5

points = generatePoints(N)
barycentres = getInitBarycentres(points, N, K)

print(barycentres)

