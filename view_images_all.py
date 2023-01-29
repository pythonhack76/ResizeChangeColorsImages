# python 3.10.1

# import the library opencv
import cv2
# globbing utility.
import glob
#to resize image import PIL
import PIL 
from PIL import Image
#to resize better images
import matplotlib.pyplot as plt

#################################################################################
#
#      START WITH THE PROGRAM TO CHANGE COLORS AND RESIZE
#         IN THE BEST WAY YOUR IMAGES SOURCED IN YOUR DIRECTORY!
#                    @spritecoder 29-01-2023
# programma di modifica colore immagini di quelle presenti in una data cartella 
#
#################################################################################
def changeColorAll():
    # select the path
    path = ".\images\*.*"
    for bb,file in enumerate (glob.glob(path)):
        image_read = cv2.imread(file)
        # conversion numpy array into rgb image to show 
        c = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
        # writing the images in a folder output_images
        cv2.imwrite('.\images\marchio{}.png'.format(bb), c)
        cv2.imshow('SpriteCoder-Image', c)
        # wait for 1 second
        k = cv2.waitKey(1000)
        # destroy the window
        cv2.destroyAllWindows()

def resizeImage():
    #read image
    img=cv2.imread("./club_altered.jpg")
    print('Immagine larghezza: ',img.shape[1])
    print('Immagine altezza: ',img.shape[0])
    #Resize the image of, say, a size of 800×600 pixels, to 300×300 pixels:
    cv2.resize(img, (100,100))
    img_75 = cv2.resize(img, None, fx = 0.75, fy = 0.75)

#resizeImage() 

#utilizziamo questa funzione per fare crop su immagini 
def CropImage():
    # Opens a image in RGB mode
    im = Image.open(r"./club_altered.jpg")
    
    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size
    
    # Setting the points for cropped image
    left = 6
    top = height / 4
    right = 174
    bottom = 3 * height / 4
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    newsize = (200, 200)
    im1 = im1.resize(newsize)
    # Shows the image in image viewer
    im1.show()

CropImage() 

#istruzioni per creare una venv 
#
# create virtual env
#Python3 -m venv image-resize
#
# activate
#source image-resize/bin/activate
