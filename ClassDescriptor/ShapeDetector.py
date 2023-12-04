import cv2
from math import copysign,log10
import imutils
import numpy as np


class ShapeDetector:
    def detect(self,image):
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
        caracter = []

        #-------------------- Pretraitement------------------------

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(7,7),1)
        
        
        
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
        dilate = cv2.dilate(seuil,kernel,iterations=1)
        erode = cv2.erode(dilate,kernel,iterations=1)
        
        #cv2.imshow("Requete",erode)
        #cv2.waitKey(0)
        #------------------- Extraire les contoures ---------------

        contours= cv2.findContours(erode, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        if (len(contours) != 0) :

            #--------------- Extraire le plus grand contour -------
            
            cntrMax = max(contours,key = cv2.contourArea)
            
            moments = cv2.moments(cntrMax)
            
            moments = cv2.HuMoments(moments)

            
            for i in range(0,7):
                if (abs(moments[i]) != 0) :
                    moments[i] = -1* copysign(1.0, moments[i]) * log10(abs(moments[i]))
                    caracter.extend(moments[i])
                else:
                    for i in range(0,7):
                            vecteur = [0]
                            caracter.extend(vecteur)
        else:
            for i in range(0,7):
                    vecteur = [0]
                    caracter.extend(vecteur)

        return caracter


