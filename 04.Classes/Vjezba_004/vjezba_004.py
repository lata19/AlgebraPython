class Osoba:
    def __init__(self):
        self.ime = ""
        self.oib = ""
        self.adresa = ""
    
# class Tvrtka:
#     def __init__(self):
#         self.ime = ""
#         self.oib = ""
#         self.adresa = ""
#         self.broj_djelatnika = 0
#         self.pravni_oblik = ""

# class Djelatnik:
#     def __init__(self):
#         self.ime = ""
#         self.oib = ""
#         self.adresa = ""
#         self.radno_mjesto = ""


class Tvrtka(Osoba):
    def _init__(self):
        super().__init__
        self.broj_djelatnika = 0
        self.pravni_oblik = ""


class Djelatnik(Osoba):
    def __init__(self):
        super().__init__()
        self.radno_mjesto = ""