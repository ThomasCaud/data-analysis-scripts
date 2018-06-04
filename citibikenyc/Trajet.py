import numpy as np
import math
# Todo ajouter date pour pouvoir faire une analyse partielle

class Trajet:
    def __init__(self, start_longi, start_lati, end_longi, end_lati):
        self.slon = float(start_longi)
        self.slat = float(start_lati)
        self.elon = float(end_longi)
        self.elat = float(end_lati)
        self.xy4 = self.to_xy4()

    def setTrajet(self, start_longi, start_lati, end_longi, end_lati):
        self.slon = float(start_longi)
        self.slat = float(start_lati)
        self.elon = float(end_longi)
        self.elat = float(end_lati)
        self.xy4 = self.to_xy4()

    # Conversion longitude et latitude de départ, à des points sur un plan euclidien (à 4 dimensions)
    # dilatation de l'axe
    def to_xy4(self):
        Rt = 6371e3
        sy = Rt * (self.slat/180*np.pi)
        ey = Rt * ((self.elat-40)/180*np.pi)
        sx = Rt * np.cos(40/180*np.pi) * ((self.slon+70)/180*np.pi)
        ex = Rt * np.cos(40/180*np.pi) * ((self.elon+70)/180*np.pi)
        return np.array((sx, sy, ex, ey))

    def display(self):
        print ("[Start] - Longitude: ", str(self.slon) + ", latitude: " + str(self.slat))
        print ("[End] - Longitude: ", str(self.elon) + ", latitude: " + str(self.elat))
        # print("xy4: ", self.xy4)

    def add(self, trajet):
        self.slon += trajet.slon
        self.slat += trajet.slat
        self.slon += trajet.slon
        self.slat += trajet.slat
        self.xy7 = self.to_xy4()

    # Retourne la distance entre les deux points de départs + la distance entre les deux points d'arrivés
    # todo faire enfonction de xy4
    def getDistance(self, trajet):
        return math.sqrt(
            (self.slon- trajet.slon)**2 + 
            (self.slat-trajet.slat)**2
        ) + math.sqrt(
            (self.elon- trajet.elon)**2 + 
            (self.elat-trajet.elat)**2
        )