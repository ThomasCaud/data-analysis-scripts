import lmdb
import csv
import pickle

from Trajet import Trajet

# https://www.citibikenyc.com/system-data
# json: lent, ne gère pas tous les types, a du mal avec les conversions. Mais human readable
# pickle: générique (on peut créer nos classes), rapides. Mais machine readable

# Sur le graphique, nous n'afficherons que k courbe (une courbe pour chaque cluster, qui représentera le "trajet moyen")

# Utiliser "less" pour lire le fichier ("more" ne lit que dans un sens; less supporte la recherche, le wrapping. Pas de page man more, mais il y en a une pour less)
# less -S fichier 
# zcat fichier.gz | less -S

# un enregistrement csv = un enregistrement lmdb
# stocker objet avec les infos intéressantes
# Avec certaines valeurs, construire une clé unique (compteur ?)
# Clé en forme binaire, objet en b aussi
# Le stocker en base

map_size = 100000
db = lmdb.open('mylmdb', map_size=map_size)
filename='201609-citibike-tripdata.csv'

def getSerializedKey(key):
	return key.encode('ascii')

def getSerializedValue(value):
	return pickle.dumps(value)

def writeLMDB(db, key, value):
	print("Saving data with key = " + str(key) + "...")
	txn.put(getSerializedKey(key), getSerializedValue(value))
	print("Saving data with key = " + str(key) + "...[OK]")

def readTrajets(lmdb_env):
	lmdb_txn = lmdb_env.begin()
	lmdb_cursor = lmdb_txn.cursor()

	for key, value in lmdb_cursor:
		trajet = pickle.loads(value)
		trajet.displayCoordonnee()

def manageData(txn, key, row):
	trajet = Trajet(
		row['start station longitude'],
		row['start station latitude'],
		row['end station longitude'],
		row['end station latitude']
	)

	trajet.displayCoordonnee()
	writeLMDB(txn, key, trajet)

print('Starting...')
with db.begin(write=True) as txn:
	print('Opening LMDB...[OK]')
	with open(filename) as csvfile:
		print('Opening data file...[OK]')
		reader = csv.DictReader(csvfile)
		i = 0
		for row in reader:
			if(i > 10): exit()
			print('Reading row ' + str(i) + '...')
			manageData(txn, str(i), row)
			i += 1
