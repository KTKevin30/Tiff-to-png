from PIL import Image
import glob
from wand.image import Image
import os
 #chemin d'acces au fichier a convertir
IMAGE_PATH = "/home/kevin/DATA/NOK/*.tif"

#chemin d'acces au fichier converti
SAVE_PATH = "/home/kevin/DATA/DATA_PNG/"

#fonction qui permet de convertir une image tif en png
def tif_to_png (path_to_image, save_path):

	#recuperation du fichier a convertir
	ti1 = Image(filename = path_to_image)

	#convertion du fichier recupere en png ensuite stocker dans ti2
	ti2 = ti1.convert('png')

	#recuperation du nom du fichier qui est censé etre à la suite du dernier slash d'ou le -1
	path_to_image = path_to_image.split('/')[-1]

	#replacement de l'extension du fichier à parti du point (d'où le 0), par un l'extension .png
	path_to_image = path_to_image.split('.')[0] + '.png'

	#stoker le fichier converti dans la variable SAVE_PATH qui est le chemin d'acces du dossier des fichier converti
	ti2.save(filename = SAVE_PATH+path_to_image)

#creation d'une liste contenant la liste des fichier a convertir
images = glob.glob(IMAGE_PATH)

#convertion de tous les elements de la liste
for image in images:
	
	#appel de la fonction pour convertir image par image
	tif_to_png(image, SAVE_PATH)