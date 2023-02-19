class Osoba:
    def __init__(self, ime, oib, adresa):
        self.ime = ime
        self.oib = oib
        self.adresa = adresa

# class Tvrtka():
#     def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
#         self.ime = ime
#         self.oib = oib
#         self.adresa = adresa
#         self.broj_djelatnika = broj_djelatnika
#         self.pravni_oblik = pravni_oblik

# class Djelatnik():
#     def __init__(self, ime, oib, adresa, radno_mjesto):
#         self.ime = ime
#         self.oib = oib
#         self.adresa = adresa
#         self.radno_mjesto = radno_mjesto


class Tvrtka(Osoba):
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
        Osoba.__init__(self, ime, oib, adresa)
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik

class Djelatnik(Osoba):
    def __init__(self, ime, oib, adresa, radno_mjesto):
        super().__init__(ime, oib, adresa)
        self.radno_mjesto = radno_mjesto

djelatnik = Djelatnik("Petar", "544853160", "Ilica 50", "Programer")
print(djelatnik.ime)