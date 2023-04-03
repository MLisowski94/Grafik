from pathlib import Path
import cv2
import numpy as np
from matplotlib import pyplot as plt

class Procesor:
    def __init__(self, name, path):
        # Sprwadzanie poprawnosci sciezki
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


