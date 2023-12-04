# import the necessary packages
import cv2
import numpy as np


class ColorDesMoyenne:
    
    def describe(self, img):
         feauter = []
        
         redChannel = img[: , :, -1]
         greenChannel = img[: , :, 0]
         blueChannel = img[: , :, 1]
        
         meanR = np.mean(redChannel)
         meanG = np.mean(greenChannel)
         meanB = np.mean(blueChannel)
        
        
         feauter.append(meanR)
         feauter.append(meanG)
         feauter.append(meanB)

         return feauter
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         # features = []
         # avg_color_per_row = np.average(image, axis=0)
         # features = np.average(avg_color_per_row, axis=0)
         # return features