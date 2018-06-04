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
from Cluster import Cluster

class Kmeans:
    def __init__(self, nbBarycentre):
        self.nbBarycentre = nbBarycentre
        self.barycentres = []
        for i in range(nbBarycentre):
            self.barycentres.append(Cluster())

    def getNearestBarycentre(self, trajet):
        index = -1
        distance = -1
        i = 0
        while i < len(self.barycentres):
            tmpDistance = self.barycentres[i].getDistance(trajet)
            if index == -1 or tmpDistance < distance:
                distance = tmpDistance
                index = i
            i += 1
        print("Nearest: " + str(index))
        return self.barycentres[index]

    def display(self):
        print("Clusters display")
        for cluster in self.barycentres:
            cluster.display()

    def addTrajet(self, trajet, rowNumber):
        print("Row number: " + str(rowNumber))
        isAdded = False
        # Regarde si un des clusters est vide
        # Si vide, ajoute le trajet
        for cluster in self.barycentres:
            if(cluster.isEmpty()):
                print("Empty => add")
                cluster.addTrajet(trajet)
                isAdded = True
                break

        # Si tous non-vide, l'ajoute au plus proche
        if(isAdded == False):
            nearestBarycentre = self.getNearestBarycentre(trajet)
            nearestBarycentre.addTrajet(trajet)
            self.calculeBarycentres()

    def calculeBarycentres(self):
        for cluster in self.barycentres:
            cluster.updateBarycentre()
        # haveModification = 1
        # while haveModification:
        #     print("New evaluation")
        #     haveModification = 0

# On garde en mémoire les futurs barycentres
# barycentres € [, , ,]

# while smth: (sarrête quand les barycentres sont stables)
# 	barycentres[2] €  R^d
# 	Initiliaser un vecteur de contribution: futur_barycentres_non_renorma = [0,0,0] R^d
# 	nb_pts = [0,0,0]
# 	for d in all_data:
# 		d -> cherche le barycentre le plus proche -> k
# 		futur_barycentres_non_renorma[k] += d
# 		nb_pts[k]+<-1
# 	for k
# 		barycentres[k] = futur_barycentres_non_renorma[k]/nb_pts[k]

# barycentre = un trajet typique/moyen

# afficher sur le graphe des flèches + grosses si nb de trajets + grand