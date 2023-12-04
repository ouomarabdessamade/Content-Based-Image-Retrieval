from ClassDescriptor.zernikeDescriptor import ZernikeMoments
#from ClassDescriptor.ShapeDetector22 import ShapeDetector
import argparse
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,help = "Path to where the computed index will be stored")
ap.add_argument("-t", "--imagetype", required = True,help = "The type of the image")
args = vars(ap.parse_args())

desc = ZernikeMoments(21)
#desc = ShapedetectZernikor()

output = open(args["index"], "w")
typeim = str(args["imagetype"])
i = 1
if (typeim == "jpg"):
        for imagePath in glob.glob(args["dataset"] + "\*.jpg"):
                imageID = imagePath[imagePath.rfind("\\") + 1:]
                image = cv2.imread(imagePath)

                caracter = desc.detectZernik(image)
                caracter = [str(f) for f in caracter]
                output.write("%s,%s\n" % (imageID, ",".join(caracter)))
                i+=1
                print(i)
elif (typeim == "png"):
        for imagePath in glob.glob(args["dataset"] + "\*.png"):
                imageID = imagePath[imagePath.rfind("\\") + 1:]
                image = cv2.imread(imagePath)

                caracter = desc.detectZernik(image)
                caracter = [str(f) for f in caracter]
                output.write("%s,%s\n" % (imageID, ",".join(caracter)))
                i+=1
                print(i)
elif(typeim == "both"):
        for imagePath in glob.glob(args["dataset"] + "\*.jpg"):
                imageID = imagePath[imagePath.rfind("\\") + 1:]
                image = cv2.imread(imagePath)

                caracter = desc.detectZernik(image)
                caracter = [str(f) for f in caracter]
                output.write("%s,%s\n" % (imageID, ",".join(caracter)))
                i+=1
                print(i)
        for imagePath in glob.glob(args["dataset"] + "\*.png"):
                imageID = imagePath[imagePath.rfind("\\") + 1:]
                image = cv2.imread(imagePath)

                caracter = desc.detectZernik(image)
                caracter = [str(f) for f in caracter]
                output.write("%s,%s\n" % (imageID, ",".join(caracter)))
                i+=1
                print(i)

output.close()
