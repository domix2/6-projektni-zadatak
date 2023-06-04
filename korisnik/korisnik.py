from abc import ABC,abstractmethod

class Korisnik(ABC):
    def __init__(self, email, telefon):
        self._email = email
        self._telefon = telefon

    @property
    def email(self):
        return self._email

    @property
    def telefon(self):
        return self._telefon

    @abstractmethod
    def ispis(self):
        pass
