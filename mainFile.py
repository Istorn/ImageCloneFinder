# USAGE
# python compare.py

# import the necessary packages
#from skimage.measure import structural_similarity as ssim
from skimage import measure as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os 
import glob
def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	#m = mse(imageA, imageB)
    #Normalizziamo le due immagini
    if ((imageA.shape[0]!=imageB.shape[0]) or (imageA.shape[1]!=imageB.shape[1])):
        print("Immagine da stretchare")
        (H, W) = imageA.shape
    	# to resize and set the new width and height 
        imageB = cv2.resize(imageB, (W, H))
    s = ssim.compare_ssim(imageA, imageB)
    #calcolato il sim torniamo true se raggiunge una certa soglia
    return s
	

# load the images -- the original, the original + contrast,
# and the original + photoshop
absolute_path = os.path.join(os.getcwd(),'images/');
#prendiamo le immagini di tutta la cartella


# convert the images to grayscale
image_list = []
for filename in glob.glob(absolute_path+'/*.jpeg'):
    image=cv2.imread(filename)
    #convertiamo in grigio
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #aggiungiamo alla lista
    image_list.append([filename,image])
for filename in glob.glob(absolute_path+'/*.jpg'):
    image=cv2.imread(filename)
    #convertiamo in grigio
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #aggiungiamo alla lista
    image_list.append([filename,image])
for filename in glob.glob(absolute_path+'/*.png'):
    image=cv2.imread(filename)
    #convertiamo in grigio
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #aggiungiamo alla lista
    image_list.append([filename,image])
for filename in glob.glob(absolute_path+'/*.tiff'):
    image=cv2.imread(filename)
    #convertiamo in grigio
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #aggiungiamo alla lista
    image_list.append([filename,image])
for filename in glob.glob(absolute_path+'/*.bmp'):
    image=cv2.imread(filename)
    #convertiamo in grigio
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #aggiungiamo alla lista
    image_list.append([filename,image])



# initialize the figure
fig = plt.figure("Images")


# loop over the images
for image in image_list:
	# compariamo le immagini
    #le compariamo con le altre nella cartella
	for imageconf in image_list:
		if (imageconf[0]!=image[0]):
			result=compare_images(image[1],imageconf[1],"Confronto")
			print("Grado di similarità tra "+imageconf[0]+" e "+image[0]+": "+str(result))
			if (result>=0.87):
                #rimuoviamo l'elemento dalla lista
				print("Immagini molto simili, elimino")
				os.remove(imageconf[0])
				print("File "+imageconf[0]+" eliminato")
				image_list.remove(imageconf)







