import imgprocesor
import cv2
import numpy

# Stworzyc:
# a) kod przetwarzajacy obraz i zapisujacy krawedzie w postaci matryc
# b) kod pozwalajacy na rysowanie przy pomocy liter na podstawie matryc
# c) baze danych do przechowywania matryc
# d) GUI sluzace do obslugi
# e) sprobowac wykonac ktores zadan poprzez integracje kodu c z  pythonem



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obraz = imgprocesor.Procesor('obraz', 'images/obraz.jpg')
    wymiary = obraz.set_scale(16)
    print("Oryginalny wymiar to %(heigh_original)d, %(width_original)d, skala to %(scale)d "
          "nowy wymiar to %(heigh_scaled)d, %(width_scaled)d"%wymiary)
    kontur = obraz.set_edge_detection(100, 100)
    cv2.imshow('kontur', kontur)

    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()
    matryca = obraz.get_contour_matrix()
    print(matryca)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
