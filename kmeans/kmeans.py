import random

import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import sys
import math
sys.stdout.flush()

def generatePoints(N):
	X = random.sample(range(1, 100), N)
	Y = random.sample(range(1, 100), N)
	return list(zip(X, Y))

def getBarycentre(points):
	N = len(points)

	if N > 0:
		sumX = 0
		sumY = 0
		for X, Y in points:
			sumX += X
			sumY += Y
		return (sumX/N, sumY/N)
	return (0,0)

def getBarycentres(clusters):
	K = len(clusters)
	barycentres = []
	for i in range(K):
		barycentres.append(getBarycentre(clusters[i]))
	return barycentres

def getInitBarycentres(points, N, K):
	barycentres = []
	for i in range(K):
		randomInt = random.randint(0, N-1)
		barycentres.append(points[randomInt])
	return barycentres

def getDistance(pointA, pointB):
	return math.sqrt(
		(pointA[0]-pointB[0])**2 + 
		(pointA[1]-pointB[1])**2
	)

def getIndexOfNearestBarycentre(barycentres, point):
	index = -1
	distance = -1
	i = 0
	while i < len(barycentres):
		tmpDistance = getDistance(barycentres[i], point)
		if index == -1 or tmpDistance < distance:
			distance = tmpDistance
			index = i
		i += 1

	return index

def displayKMeans(plt, clusters):
	colors = ['blue', 'red', 'green', 'orange', 'black']
	i = 0
	while i < len(clusters):
		x = []; y=[]
		for point in clusters[i]:
		   x.append(point[0])
		   y.append(point[1])

		plt.plot(x, y, color=colors[i % len(colors)])
		i += 1
	return

def displayBarycentres(plt, barycentres):
	x = []; y=[]
	for point in barycentres:
	   x.append(point[0])
	   y.append(point[1])

	plt.plot(x, y, '+', color='red', markersize=12)
	return

def display(clusters, barycentres):
	plt.figure()
	displayKMeans(plt, clusters)
	displayBarycentres(plt, barycentres)
	plt.show()
	return

def deletePointFromCluster(clusters, point):
	for cluster in clusters:
		if point in cluster:
			cluster.remove(point)
	return

# Number of points
N = 99

# Number of clusters
K = 4

points = generatePoints(N)
barycentres = getInitBarycentres(points, N, K)
nearestBary = getIndexOfNearestBarycentre(barycentres, points[0])

clusters = np.empty((K, 0)).tolist()

haveModification = 1
while haveModification:
	print("Itération")
	haveModification = 0

	for point in points:
		nearestBaryIndex = getIndexOfNearestBarycentre(barycentres, point)
		if point not in clusters[nearestBaryIndex]:
			print("barycentres: {0}" . format(barycentres))
			print("Point : {0}" . format(point))
			print("Nearest: {0}" . format(barycentres[nearestBaryIndex]))

			haveModification = 1
			# supprimer le point de son ancien cluster
			deletePointFromCluster(clusters, point)
			clusters[nearestBaryIndex].append(point)
			barycentres = getBarycentres(clusters)

display(clusters, barycentres)