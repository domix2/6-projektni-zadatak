from utillities import unos_telefona, unos_intervala
from .poslovni_korisnik import PoslovniKorisnik
from .privatni_korisnik import PrivatniKorisnik

def unos_korisnika(redni_broj):
    email = input(f'Unesite email {redni_broj}. korisnika: ').strip()
    telefon = unos_telefona(f'Unesite telefon {redni_broj}. korisnika: ')
    print('Tipovi korisnika:')
    print('\t 1. Poslovni korisnik')
    print('\t 2. Privatni korisnik')
    tip = unos_intervala(1, 2)

    if tip == 1:
        naziv = input(f'Unesite naziv {redni_broj}. korisnika: ')
        web = input(f'Unesite web stranicu {redni_broj}. korisnika: ')

        return PoslovniKorisnik(naziv, web, telefon, email)

    elif tip == 2:
        ime = input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
        prezime = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
        return PrivatniKorisnik(ime, prezime, telefon, email)