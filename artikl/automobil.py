from .vozilo import Vozilo
from .artikl import Artikl

class Automobil(Artikl,Vozilo):

    def __init__(self, snaga, naslov, opis, cijena):
        super().__init__(naslov, opis, cijena)
        self.snaga = snaga

    def ispis(self):
        print('Informacije o vozilu: ')
        print(f'\t Naslov: {self.naslov}')
        print(f'\t Opis: {self.opis}')
        print(f'\t Cijena: {self.cijena}')
        print(f'\t Cijena osiguranja: {self.cijena_osiguranja(self.snaga)}')