from .korisnik import Korisnik

class PoslovniKorisnik(Korisnik):

    def __init__(self, naziv, web, email, telefon):
        super().__init__(email, telefon)
        self.__naziv = naziv
        self.__web = web

    @property
    def naziv(self):
        return self.__naziv

    @naziv.setter
    def naziv(self, naziv):
        self.__naziv = naziv

    @property
    def web(self):
        return self.__web

    @web.setter
    def web(self, web):
        self.__web = web

    def ispis(self):
      print("Informacije o poslovnom korisniku: ")
      print(f'\tNaziv: {self.__naziv}')
      print(f'\tWeb: {self.__web}')
      print(f'\tTelefon: {self.telefon}')
      print(f'\tEmail: {self.email}')