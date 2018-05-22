class Trajet:
    def __init__(self, start_longi, start_lati, end_longi, end_lati):
    	self.start_longi = start_longi
    	self.start_lati = start_lati
    	self.end_longi = end_longi
    	self.end_lati = end_lati
   
    def displayCoordonnee(self):
    	print ("[Start] - Longitude: ", str(self.start_longi) + ", latitude: " + str(self.start_lati))
    	print ("[End] - Longitude: ", str(self.end_longi) + ", latitude: " + str(self.end_lati))