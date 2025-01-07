from models.pajamu_irasas import Pajamuirasas
from models.isalidu_irasas import Islaiduirasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamas(self):
        suma = float(input("Suma: "))
        irasas = Pajamuirasas(suma)
        self.zurnalas.append(irasas)

    def prideti_islaidas(self):
        suma = float(input("Suma: "))
        irasas = Islaiduirasas(suma)
        self.zurnalas.append(irasas)

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if type(irasas) is Pajamuirasas:
                balansas += irasas.suma
            else:
                balansas -= irasas.suma
            return balansas
