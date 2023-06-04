from .artikl import Artikl

class Stan(Artikl):

    def __init__(self, kvadratura, naslov, opis, cijena):
        super().__init__(naslov, opis, cijena)
        self.kvadratura = kvadratura

    def ispis(self):
        print('Informacije o stanu: ')
        print(f'\t Naslov: {self.naslov}')
        print(f'\t Opis: {self.opis}')
        print(f'\t Cijena: {self.cijena}')
        print(f'\t Kvadratura: {self.kvadratura}')