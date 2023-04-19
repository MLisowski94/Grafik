from pathlib import Path
import cv2
import numpy
import math
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
        self.scale = None
        self.image_contour = None
        self.image = cv2.imread(path)

    def set_scale(self, scale):
        heigh, width = self.image.shape[:2]
        heigh_scaled = math.ceil(heigh / scale)
        width_scaled = math.ceil(width / scale)
        #Checking for validity of scale
        if not type(scale) == int:
            raise TypeError("Wartosc zmiennej scale musi być typu iny")
        if heigh_scaled < 1 or width_scaled < 1:
            raise ValueError("Wartosc zmiennej skala ma zbyt duza wartosc, "
                             "po przeksalowaniu obraz staje sie mniejszy niż 1px")
        self.scale = scale;
        dimensions = {
            "scale": scale,
            "heigh_original": heigh,
            "width_original": width,
            "heigh_scaled": heigh_scaled,
            "width_scaled": width_scaled
        }
        return dimensions

    def set_edge_detection(self, low_threshold, high_threshold):
        if self.scale == None:
            raise ValueError("Zmiennej scale nie została przypisana wartosc, "
                             "uzyj do tego funckji set_scale")
        #scaling image
        heigh, width = self.image.shape[:2]
        _resized_image = cv2.resize(self.image, (int(width / self.scale), int(heigh / self.scale)),
                                    interpolation = cv2.INTER_CUBIC)
        # using Canny alghoritm to modify scaled image
        self.image_contour = cv2.Canny(_resized_image, int(low_threshold), int(high_threshold))
        return self.image_contour

    def get_contour_matrix(self):
        if self.image_contour == None:
            raise ValueError("Obraz musi zostać przetworzony przy pomocy funkcji set_edge_detection")
        contour_heigh, contour_width  = self.image_contour.shape[:2]
        #making numpy array on base of image_contour
        contour_matrix = numpy.zeros([contour_heigh, contour_width], dtype=int)
        for x in range(contour_heigh):
            for y in range(contour_width):
                    contour_matrix[x, y] = int(self.image_contour[x, y])
        return contour_matrix

        #
        # #saving matrix as output file
        # numpy.savetxt("data.txt", self.contour_matrix, fmt="%3i", delimiter=",")
        #
        # cv2.imshow('kontur', self.image_contour)
        #
        # # waits for user to press any key
        # # (this is necessary to avoid Python kernel form crashing)
        # cv2.waitKey(0)
        #
        # # closing all open windows
        # cv2.destroyAllWindows()







