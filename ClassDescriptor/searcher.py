# import the necessary packages
import numpy as np
import csv

listeglobal = {}

class Searcher:
	def __init__(self, indexPath):
		# store our index path
		self.indexPath = indexPath
        

         
	#-------------serch of color histogramme ---------------------------------#
	def search(self, queryFeatures, limit = 10):
		# initialize our dictionary of results
		results = {}
        
        # open the index file for reading
		with open(self.indexPath) as f:
			# initialize the CSV reader
			reader = csv.reader(f)
			# loop over the rows in the index
			for row in reader:
				# parse out the image ID and features, then compute the
				# chi-squared distance between the features in our index
				# and our query features
				features = [float(x) for x in row[1:]]
				d = self.chi2_distance(features, queryFeatures)
				# now that we have the distance between the two feature
				# vectors, we can udpate the results dictionary -- the
				# key is the current image ID in the index and the
				# value is the distance we just computed, representing
				# how 'similar' the image in the index is to our query
				results[row[0]] = d
			# close the reader
			f.close()
		# sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		results = sorted([(v, k) for (k, v) in results.items()])
		lesDistances = tuple(x[0] for x in results)
		pourcentage = []
		for laDistance in lesDistances :
			pource = 100 - (laDistance / lesDistances[-1])*100
			pourcentage.append(round(pource, 2))
            
		return results[:limit] ,pourcentage
    
    #-------------serch of color histogramme ---------------------------------#
	def searchcolorMoyenne(self, queryFeatures, limit = 10):
		# initialize our dictionary of results
		results = {}
        
        # open the index file for reading
		with open(self.indexPath) as f:
			# initialize the CSV reader
			reader = csv.reader(f)
			# loop over the rows in the index
			for row in reader:
				# parse out the image ID and features, then compute the
				# chi-squared distance between the features in our index
				# and our query features
				features = [float(x) for x in row[1:]]
				d = self.euclidiane(features, queryFeatures)
				# now that we have the distance between the two feature
				# vectors, we can udpate the results dictionary -- the
				# key is the current image ID in the index and the
				# value is the distance we just computed, representing
				# how 'similar' the image in the index is to our query
				results[row[0]] = d
			# close the reader
			f.close()
		# sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		results = sorted([(v, k) for (k, v) in results.items()])
		lesDistances = tuple(x[0] for x in results)
		pourcentage = []
		for laDistance in lesDistances :
			pource = 100 - (laDistance / lesDistances[-1])*100
			pourcentage.append(round(pource, 2))
		# return our (limited) results
		return results[:limit], pourcentage
    
  
	def chi2_distance(self, histA, histB, eps = 1e-10):
		# compute the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])
		# return the chi-squared distance
		return d
    
    
    #-------------serch of Texture----------------------------------------------#
	def searchTexture(self, queryFeatures, limit = 10):
		# initialize our dictionary of results
		results = {}
        
        # open the index file for reading
		with open(self.indexPath) as f:
			# initialize the CSV reader
			reader = csv.reader(f)
			# loop over the rows in the index
			for row in reader:
				# parse out the image ID and features, then compute the
				# chi-squared distance between the features in our index
				# and our query features
				features = [float(x) for x in row[1:]]
				d = self.Euclidean_distance(features, queryFeatures)
				# now that we have the distance between the two feature
				# vectors, we can udpate the results dictionary -- the
				# key is the current image ID in the index and the
				# value is the distance we just computed, representing
				# how 'similar' the image in the index is to our query
				results[row[0]] = d
			# close the reader
			f.close()
		# sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		results = sorted([(v, k) for (k, v) in results.items()])
		lesDistances = tuple(x[0] for x in results)
		pourcentage = []
		for laDistance in lesDistances :
			pource = 100 - (laDistance / lesDistances[-1])*100
			pourcentage.append(round(pource, 2))
		# return our (limited) results
		return results[:limit], pourcentage
    
    
	def Euclidean_distance(self, p, q):
         dist = np.sqrt(np.sum(np.square(p-q)))
         return dist

    #-------------serch of Shape----------------------------------------------#
	def searchShape(self, queryFeatures, limit = 10):
		results = {}
		i = 1
		with open(self.indexPath) as f:
			reader = csv.reader(f)
			for row in reader:
				caracter = [float(x) for x in row[1:]]
				d = self.euclidiane(caracter, queryFeatures)
				results[row[0]] = d
				i+=1
			f.close()
		results = sorted([(v, k) for (k, v) in results.items()])
		lesDistances = tuple(x[0] for x in results)
		#lesImages = tuple(x[1] for x in results)
		pourcentage = []
		for laDistance in lesDistances :
			pource = 100 - (laDistance / lesDistances[-1])*100
			pourcentage.append(round(pource, 2))
		#print(pourcentage)
		return results[:limit], pourcentage



	def euclidiane(self, histA, histB):
		d = np.sqrt(np.sum([(b - a)**2 for (a, b) in zip(histA, histB)]))
		return d


