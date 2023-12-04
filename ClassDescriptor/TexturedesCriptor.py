import numpy as np
from skimage import feature
from skimage.feature import graycomatrix 
from skimage.feature import graycoprops 
import cv2

class texturedescriptor:
        
    def lbp_features(self, img, radius=1, sampling_pixels=100):
        # LBP operates in single channel images so if RGB images are provided
        # we have to convert it to grayscale
        if (len(img.shape) > 2):
            img = img.astype(float)
            # RGB to grayscale convertion using Luminance
            img = img[:,:,0]*0.3 + img[:,:,1]*0.59 + img[:,:,2]*0.11
    
        # converting to uint8 type for 256 graylevels
        img = img.astype(np.uint8)
        
        # normalize values can also help improving description
        i_min = np.min(img)
        i_max = np.max(img)
        if (i_max - i_min != 0):
            img = (img - i_min)/(i_max-i_min)
        
        # compute LBP
        lbp = feature.local_binary_pattern(img, sampling_pixels, radius, method="uniform")
        
        # LBP returns a matrix with the codes, so we compute the histogram
        (hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, sampling_pixels + 3), range=(0, sampling_pixels + 2))
    
        # normalization
        hist = hist.astype("float")
        hist /= (hist.sum() + 1e-6)
        # return the histogram of Local Binary Patterns
        return hist

    #Normalisation de l'image
    def normalisationImage(self, image):
        normImage = image//16
        normImage = normImage.astype('uint32')
        return normImage

   
    
    #Histogramme d'une image à niveau de gris
    def Histogramme(self, mat):
        histogramme = cv2.calcHist([mat], [0], None, [24,24, 24],[0, 256])
        return histogramme
    
    #Calcul de la distance
    def CalculDistance(self, image1,image2):
        d = (np.linalg.norm((image1-image2))/5)
        return d

    #Matrice de co-occurence
    def MatCooccurence(self, image_gris):
        matCo = graycomatrix(image_gris, [5], [0,np.pi/2,np.pi/4,(np.pi*3)/4], 256,
                         symmetric=True, normed=True)
        return matCo

    #Calcul des parametre de la co occurence
    def ParamCooccurence(self, HistomatCoo):
        energie = graycoprops(HistomatCoo,'energy')
        contraste = graycoprops(HistomatCoo,'contrast')
        dissimilarite = graycoprops(HistomatCoo,'dissimilarity')
        homogeneite = graycoprops(HistomatCoo,'homogeneity')
        correlation = graycoprops(HistomatCoo,'correlation')
        return energie, contraste, dissimilarite,homogeneite,correlation


    #Matrice de co-occurence
    def MatCooccurenceHaralick(self, img):
        param = []
       
        param = np.zeros(5)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        greyImage = self.normalisationImage(gray)
    
        MatCoo = self.MatCooccurence(greyImage)
        energie,contraste,dissimilarite,homogeneite,correlation = self.ParamCooccurence(MatCoo)
        energie = energie[0][0]
        param[0] = energie
        contraste = contraste[0][0]
        param[1] = contraste
        dissimilarite = dissimilarite[0][0]
        param[2] = dissimilarite
        homogeneite = homogeneite[0][0]
        param[3] = homogeneite
        correlation = correlation[0][0]
        param[4] = correlation
       
        return param















