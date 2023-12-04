import numpy as np
import csv


class SearcherIbride:
	
 	def __init__(self, indexPathcol, indexPathForm, indexPathTexture):
          self.indexPathcol = indexPathcol
          self.indexPathForm = indexPathForm
          self.indexPathTexture = indexPathTexture
          
          
 	def ibridesearch(self, queryFetrcolor, poidcolor, queryFetexture, poidtextur, queryFetShape, poidShape, limit = 10):
         resltcolor = {}
         resltTexture = {}
         resltForm = {}
         
         distcolor = []
         distTexture = []
         distForme = []
         somdistance = []
         
         resltglobal = {}
         #-------------distance par color-------------------------------------#
         with open(self.indexPathcol) as f:
              readercolor = csv.reader(f)
              for row in readercolor:			
	                featucolor = [float(x) for x in row[1:]]
                    
	                distancol = self.euclidiane(featucolor, queryFetrcolor)
                    
	                resltcolor[row[0]] = distancol * poidcolor
              # close the reader
              f.close()
         resltcolor = [(k, v) for (k, v) in resltcolor.items()]
         distcolor = tuple(x[1] for x in resltcolor)
         #print("resltcolor = ", distcolor)    
         #-------------distance par texture-------------------------------------#
         with open(self.indexPathTexture) as f:
              readertexture = csv.reader(f)
              for row in readertexture:			
	                feattexture = [float(x) for x in row[1:]]
                    
	                distform = self.euclidiane(feattexture, queryFetexture)
                    
	                resltTexture[row[0]] = distform * poidtextur     
              # close the reader
              f.close()
         #print("resltTexture = ", resltTexture) 
         reslttexture = [(k, v) for (k, v) in resltTexture.items()]
         distTexture = tuple(x[1] for x in reslttexture)
         #-------------distance par forme-------------------------------------#
         with open(self.indexPathForm) as f:
              readerform = csv.reader(f)
              for row in readerform:			
	                featuform = [float(x) for x in row[1:]]
                    
	                distform = self.euclidiane(featuform, queryFetShape)
                    
	                resltForm[row[0]] = distform * poidShape
              # close the reader
              f.close()
         #print("resltForm = ", resltForm) 
         resltForme = [(k, v) for (k, v) in resltTexture.items()]
         distForme = tuple(x[1] for x in resltForme)
         #---------------resultat global --------------------------------------#
         
         for i in range(len(distcolor)):
             somdistance.append(distcolor[i] + distTexture[i] + distForme[i])
     	 
         #----rassemble les resultat dans une seul liste ---------------------#
         m=0
         with open(self.indexPathcol) as f:
              readglob = csv.reader(f)
              for row in readglob:			
	                featglob = [float(x) for x in row[1:]]   
	               
	                resltglobal[row[0]] = somdistance[m]
	                m+=1
              f.close()
         #print("resltglobal = ", resltglobal)
         resltglobal = sorted([(v, k) for (k, v) in resltglobal.items()])
         lesDistances = tuple(x[0] for x in resltglobal)
         pourcentage = []
         for laDistance in lesDistances :
              pource = 100 - (laDistance / lesDistances[-1])*100
              pourcentage.append(round(pource, 2))
         return resltglobal[:limit], pourcentage
        
     
 	def chi2_distance(self, histA, histB, eps = 1e-10):
		# compute the chi-squared distance
	   	d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])
		# return the chi-squared distance
	   	return d
       
 	def Euclidean_distance(self, p, q):
         dist = np.sqrt(np.sum(np.square(p-q)))
         return dist
     
        
 	def euclidiane(self, histA, histB):
		 d = np.sqrt(np.sum([(b - a)**2 for (a, b) in zip(histA, histB)]))
		 return d