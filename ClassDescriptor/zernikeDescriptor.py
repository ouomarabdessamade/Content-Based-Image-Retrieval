import mahotas
import cv2
import imutils
import numpy as np


class ZernikeMoments:

	def __init__(self, radius):
		# store the size of the radius that will be
		# used when computing moments
		self.radius = radius
        
        
	def detectZernik(self, image):
		# return the Zernike moments for the image
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
            
            #-------------------- Pretraitement------------------------
            
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray,(13,13),0)

            
            
            #------------------- Seuillage ----------------------------
            #Le seuillage adaptatif est la méthode dans laquelle 
            #la valeur de seuil est calculée pour des régions plus petites.
            #Cela conduit à différentes valeurs de seuil pour différentes régions 
            #en ce qui concerne le changement d'éclairage.
            #Nous utilisons cv2.adaptiveThreshold pour cela.
            
            #cv2.ADAPTIVE_THRESH_GAUSSIAN_C : il s'agit d'une somme pondérée du voisinage 
            #blockSize×blockSize d'un point moins une constante.
            
            seuil = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
            
            #------------------- Dilatation puis erosion --------------
            dilate = cv2.dilate(seuil,None,iterations=4)
            erode = cv2.erode(dilate,None,iterations=2)
            
            
            #------------------- Extraire les contoures ---------------
            outline = np.zeros(image.shape, dtype = "uint8")
            contours= cv2.findContours(erode.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            cntrMax = max(contours,key = cv2.contourArea)
            # cv2.drawContours(outline, [cntrMax], -1, 255, -1)
            # for c in contours:
            # create an empty mask for the contour and draw it
            mask = np.zeros(image.shape[:2], dtype="uint8")
            cv2.drawContours(mask, [cntrMax], -1, 255, -1)
      
            # extract the bounding box ROI from the mask
            (x, y, w, h) = cv2.boundingRect(cntrMax)
            roi = mask[y:y + h, x:x + w]
            
            # compute Zernike Moments for the ROI and update the list
            # of shape features
            caracter = mahotas.features.zernike_moments(roi, cv2.minEnclosingCircle(cntrMax)[1], degree=8)
            
            return caracter