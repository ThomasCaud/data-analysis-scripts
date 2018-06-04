from Trajet import Trajet

class Cluster:
    def __init__(self):
        self.barycentre = Trajet(0,0,0,0)
        self.nbOfTrajet = 0

    def setTrajet(self,sx,sy,ex,ey):
    	self.barycentre.setTrajet(sx,sy,ex,ey)

    def addTrajet(self, trajet):
        self.barycentre.add(trajet)
        self.nbOfTrajet += 1

    def getDistance(self, trajet):
        return self.barycentre.getDistance(trajet)

    def display(self):
    	print("CLUSTER")
    	print("Number of trajets: " + str(self.nbOfTrajet))
    	self.barycentre.display()

    def isEmpty(self):
    	return (self.nbOfTrajet == 0)

    def updateBarycentre(self):
    	self.barycentre.setTrajet(
    		self.barycentre.slon / self.nbOfTrajet,
    		self.barycentre.slat / self.nbOfTrajet,
    		self.barycentre.elon / self.nbOfTrajet,
    		self.barycentre.elat / self.nbOfTrajet,
    	)
