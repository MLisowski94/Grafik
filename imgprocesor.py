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
        self.heigh_scaled = math.ceil(heigh / scale)
        self.width_scaled = math.ceil(width / scale)
        #Checking for validity of scale
        if not type(scale) == int:
            raise TypeError("Wartosc zmiennej scale musi być typu iny")
        if self.heigh_scaled < 1 or self.width_scaled < 1:
            raise ValueError("Wartosc zmiennej skala ma zbyt duza wartosc, "
                             "po przeksalowaniu obraz staje sie mniejszy niż 1px")
        self.scale = scale

    def get_dimensions(self):
        heigh, width = self.image.shape[:2]
        dimensions = {
            "scale": self.scale,
            "heigh_original": heigh,
            "width_original": width,
            "heigh_scaled": self.heigh_scaled,
            "width_scaled": self.width_scaled
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

    def get_contour_matrix(self, znak):
        if not type(znak) == str:
            raise TypeError("Znak musi być typu str")
        if not type(self.image_contour) == numpy.ndarray:
            raise ValueError("Obraz musi zostać przetworzony przy pomocy funkcji set_edge_detection")
        contour_heigh, contour_width  = self.image_contour.shape[:2]
        #making numpy array on base of image_contour
        contour_matrix = numpy.zeros([contour_heigh, contour_width], dtype=str)
        cntr = 0
        for x in range(contour_heigh):
            for y in range(contour_width):
                    if int(self.image_contour[x, y]) > 1:
                        if cntr < len(znak):
                            contour_matrix[x, y] = znak[cntr]
                            cntr += 1
                        else:
                            contour_matrix[x, y] = znak[0]
                            cntr = 1
                    else:
                        contour_matrix[x, y] =" "
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







