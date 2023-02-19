


class Osoba:
    def __init__(self, ime, oib, email, telefon, adresa):
        self.ime = ime
        self.oib = oib
        self.email = email
        self.telefon = telefon
        self.adresa = adresa

    def ispis(self):
        print()
        print(self.ime)
        print(self.oib)
        print(self.email)
        print(self.telefon)
        print(self.adresa)

class Djelatnik(Osoba):
    def __init__(self, ime, prezime, oib, email, telefon, adresa, radno_mjesto):
        super().__init__(ime, oib, email, telefon, adresa)
        self.prezime = prezime
        self.radno_mjesto = radno_mjesto

    def ispis(self):
        print()
        print(self.ime)
        print(self.prezime)
        print(self.oib)
        print(self.email)
        print(self.telefon)
        print(self.adresa)
        print(self.radno_mjesto)
        print()

class Kupac(Osoba):
    def __init__(self, ime, oib, email, telefon, adresa, djelatnost):
        super().__init__(ime, oib, email, telefon, adresa)
        self.djelatnost = djelatnost

    def ispis(self):
        super().ispis()
        print(self.djelatnost)
        print()


kupci = []
while True:
    naziv = input("Unesite naziv kupca: ")
    oib = input("Unesite OIB kupca: ")
    email = input("Unesite email kupca: ")
    telefon = input("Unesite telefon kupca: ")
    sjediste = input("Unesite sjedište kupca: ")
    djelatnost = input("Unesite djelatnost kupca: ")

    kupac = Kupac(naziv, oib, email, telefon, sjediste, djelatnost)
    kupci.append(kupac)

    odgovor = input("Želite li dodati novog kupca? (d/n)")
    if odgovor == "n":
        break

for kupac in kupci:
    kupac.ispis()


# djelatnici = []
# while True:
#     ime = input("Unesite naziv djelatnika: ")
#     prezime = input("Unesti prezime djelatnika: ")
#     oib = input("Unesite OIB djelatnika: ")
#     email = input("Unesite email djelatnika: ")
#     telefon = input("Unesite telefon djelatnika: ")
#     adresa = input("Unesite adresu djelatnika: ")
#     radno_mjesto = input("Unesite radno mjesto djelatnika: ")

#     djelatnik = Djelatnik(ime, prezime, oib, email, telefon, adresa, radno_mjesto)
#     djelatnici.append(djelatnik)

#     odgovor = input("Želite li dodati novog kupca? (d/n)")
#     if odgovor == "n":
#         break

# for djelatnik in djelatnici:
#     djelatnik.ispis()