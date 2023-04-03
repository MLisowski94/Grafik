import imgprocesor

# Stworzyc:
# a) kod przetwarzajacy obraz i zapisujacy krawedzie w postaci matryc
# b) kod pozwalajacy na rysowanie przy pomocy liter na podstawie matryc
# c) baze danych do przechowywania matryc
# d) GUI sluzace do obslugi
# e) sprobowac wykonac ktores zadan poprzez integracje kodu c z  pythonem



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obraz = imgprocesor.Procesor('obraz', 'images/obraz.jpg')
    obraz.getDim()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
