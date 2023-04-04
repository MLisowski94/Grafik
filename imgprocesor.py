from pathlib import Path
import cv2
import numpy
import  math
from matplotlib import pyplot as plt

class Procesor:
    def __init__(self, name, path):
        # Checking for path validity
        if not Path(path).exists():
            raise TypeError("Podana sciezka jest nieprawidłowa")
        if not Path(path).is_file() and Path(path).match("*.img"):
            raise TypeError("Podana sciezka nie wskazuje na plik o formacie img")

        self.name = name
        self.path = path
        self.image = cv2.imread(path)
    def getDim(self):
        h, w = self.image.shape[:2]
        # Displaying the height and width
        print("Height = {},  Width = {}".format(h, w))
    def getContourMatrix(self, matrixHeight, matrixWidth, lowThreshold, highThreshold):

        #scaling image according to matrix dimmensions, rounding scale up to avoid to big dimensions of img
        h, w = self.image.shape[:2]
        if h/matrixHeight > w/matrixWidth:
            scale = math.ceil(h/matrixHeight)
        else:
            scale = math.ceil(w/matrixWidth)
        #using Canny alghoritm to modify scaled image
        _resized_image = cv2.resize(self.image, (int(w/scale), int(h/scale)), interpolation = cv2.INTER_CUBIC)
        self.image_contour = cv2.Canny(_resized_image, int(lowThreshold), int(highThreshold))
        h1, w1 = self.image_contour.shape[:2]

        self.contourMatrix = numpy.empty([matrixHeight, matrixWidth], dtype=int)
        for x in range(h1):
            for y in range(w1):
                self.contourMatrix[x, y] = int(self.image_contour[x,y])

        slicedMatrix = self.contourMatrix[:50, :50]
        print(self.image.shape)
        print(scale)
        print(self.image_contour.shape)
        print(slicedMatrix)
        numpy.savetxt("data.csv", self.contourMatrix, delimiter=",")

        cv2.imshow('kontur', self.image_contour)

        # waits for user to press any key
        # (this is necessary to avoid Python kernel form crashing)
        cv2.waitKey(0)

        # closing all open windows
        cv2.destroyAllWindows()







