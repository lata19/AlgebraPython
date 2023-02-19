from datetime import datetime

brojac_racuna = 1


class Racun:
    """Klasa za upravljanje računima"""

    def __init__(self, racun_broj, racun_datum_izdavanja, racun_stavke):
        """"""
        self.racun_broj = racun_broj
        self.racun_datum_izdavanja = racun_datum_izdavanja
        self.racun_stavke = racun_stavke
        self.racun_ukupan_iznos = 0
        self.racun_ukupan_iznos_s_pdvom = 0
        self.izracunaj_ukupan_iznos()
        self.izracunaj_ukupan_pdv()
    
    def izracunaj_ukupan_iznos(self):
        for cijena in self.racun_stavke.values():
            self.racun_ukupan_iznos += cijena

    def izracunaj_ukupan_pdv(self):
        self.racun_ukupan_iznos_s_pdvom = self.racun_ukupan_iznos * 1.25

    def ispisi_racun(self):
        print("*" * 50)
        print(f"\n\tRacun: {self.racun_broj}")
        print(f"\tDatum: {self.racun_datum_izdavanja}")
        print("-" * 50)
        print("\tProizvod\t\tCijena")
        print()
        for k,v in self.racun_stavke.items():
            print(f"\t{k}\t\t{v}EUR")
        print()
        print("")
        print(f"\tUkupan iznos:\t{self.racun_ukupan_iznos}")
        print(f"\tIznos PDV-a:\t{self.racun_ukupan_iznos_s_pdvom}")
        print("*" * 50)
        print()
        input("Pritisni tipku za nastavak")


#stvaranje racuna
#input korisnika po stavkama

def kreiraj_racun():
    global brojac_racuna

    danasnji_datum = datetime.now()
    racun_datum_izdavanja = f"{danasnji_datum.year}-{danasnji_datum.month}-{danasnji_datum.day}"
    racun_broj = f"R-{brojac_racuna}-{racun_datum_izdavanja}"
    brojac_racuna += 1

    racun_stavke = {}
    while True:
        proizvod = input("Upišite naziv proizvoda: ")
        cijena = float(input("Upišite cijenu proizvoda: "))
        racun_stavke[proizvod] = cijena
        if not input("Unos nove stavke? Za prestanak pritisnite ENTER: "):
            break
    
    racun = Racun(racun_broj, racun_datum_izdavanja, racun_stavke)
    return racun


racuni = []
while True:
    novi_racun = kreiraj_racun()
    racuni.append(novi_racun)

    if not input("Unos nove stavke? Za prestanak pritisnite ENTER: "):
        break

for r in racuni:
    r.ispisi_racun()
