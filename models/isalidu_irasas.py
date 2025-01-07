from models.irasas import Irasas


class Islaiduirasas(Irasas):
    def __repr__(self):
        return f"Išlaidos: {self.suma}"
