from models.irasas import Irasas


class Pajamuirasas(Irasas):
    def __repr__(self):
        return f"Pajamos: {self.suma}"
