import random

class Asiakas:
    def __init__(self, nimi, ika):
        self._nimi = nimi  # Asiakkaan nimi
        self._ika = ika  # Asiakkaan ikä
        self._asiakasnumero = self._luo_nro()  # Asiakasnumeron luominen

    def get_nimi(self):
        return self._nimi  # Palauttaa asiakkaan nimen

    def set_nimi(self, nimi):
        if not nimi:
            raise ValueError("Uusi nimi on annettava.")  # Virheviesti, jos nimeä ei ole annettu
        self._nimi = nimi  # Asettaa asiakkaan nimen

    def get_ika(self):
        return self._ika  # Palauttaa asiakkaan iän

    def set_ika(self, ika):
        if not ika:
            raise ValueError("Uusi ikä on annettava.")  # Virheviesti, jos ikää ei ole annettu
        self._ika = ika  # Asettaa asiakkaan iän

    def get_asiakasnumero(self):
        return f"{self._asiakasnumero[0]:02}-{self._asiakasnumero[1]:03}-{self._asiakasnumero[2]:03}"  # Palauttaa asiakasnumeron muodossa XX-XXX-XXX

    def _luo_nro(self):
        return [random.randint(10, 99), random.randint(100, 999), random.randint(100, 999)]  # Luo satunnaisen asiakasnumeron


class Palvelu:
    def __init__(self, tuotenimi):
        self._tuotenimi = tuotenimi  # Palvelun tuotenimi
        self._asiakkaat = []  # Lista palvelun asiakkaista

    def lisaa_asiakas(self, asiakas):
        if not asiakas:
            raise ValueError("Asiakas on annettava.")  # Virheviesti, jos asiakasta ei ole annettu
        self._asiakkaat.append(asiakas)  # Lisää asiakkaan palveluun

    def poista_asiakas(self, asiakas):
        try:
            self._asiakkaat.remove(asiakas)  # Poistaa asiakkaan palvelusta
        except ValueError:
            pass

    def tulosta_asiakkaat(self):
        print(f"Tuotteen {self._tuotenimi} asiakkaat ovat:")  # Tulostaa palvelun asiakkaat
        for asiakas in self._asiakkaat:
            print(self._luo_asiakasrivi(asiakas))  # Tulostaa yksittäisen asiakkaan tiedot
        print()

    def _luo_asiakasrivi(self, asiakas):
        return f'{asiakas.get_nimi()} ({asiakas.get_asiakasnumero()}) on {asiakas.get_ika()}-vuotias.'  # Palauttaa asiakkaan tiedot merkkijonona


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self._edut = []  # Lista paremman palvelun eduista

    def lisaa_etu(self, etu):
        self._edut.append(etu)  # Lisää edun parempaan palveluun

    def poista_etu(self, etu):
        try:
            self._edut.remove(etu)  # Poistaa edun paremmasta palvelusta
        except ValueError:
            pass

    def tulosta_edut(self):
        print(f"Tuotteen {self._tuotenimi} edut ovat:")  # Tulostaa paremman palvelun edut
        for etu in self._edut:
            print(etu)  # Tulostaa yksittäisen edun
        print()
