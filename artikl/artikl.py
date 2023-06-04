from abc import ABC, abstractmethod

class Artikl(ABC):
    def __init__(self, naslov, opis, cijena):
        self.__naslov = naslov
        self.__opis = opis
        self.__cijena = cijena

    @property
    def naslov(self):
        return self.__naslov

    @naslov.setter
    def naslov(self, naslov):
        self.__naslov = naslov

    @property
    def opis(self):
        return self.__opis

    @opis.setter
    def opis(self, opis):
        self.__opis = opis

    @property
    def cijena(self):
        return self.__cijena

    @cijena.setter
    def cijena(self, cijena):
        self.__cijena = cijena

    @abstractmethod
    def ispis(self):
        pass




