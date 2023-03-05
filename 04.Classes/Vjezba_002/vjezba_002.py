

# class PrvaKlasa:
#     """Docstring koji pojasnjava
#     zasto sluzi ova klasa"""
#     pass

# objekt1 = PrvaKlasa()
# objekt2 = PrvaKlasa()


# class Televizor:
#     dijagonala = 55
#     sirina = 124
#     visina = 79
#     proizvodac = "Grundig"
#     model = "Ultra Smart Turbo Extra"
#     je_ukljucen = False
    
#     def ukljuci(self):
#         self.je_ukljucen = True


# tv_dnevni_boravak = Televizor()
# tv_kuhinja = Televizor()


# print(f"Proizdvodac: {tv_dnevni_boravak.proizvodac}")
# print(f"Sirina: {tv_dnevni_boravak.sirina}, Visina: {tv_dnevni_boravak.visina}, Dijagonala: {tv_dnevni_boravak.dijagonala}")



# print("Status oba TV-a")
# if tv_dnevni_boravak.je_ukljucen:
#     print("Status: TV u dnevnom boravku je ukljucen.")
# else:
#     print("Status: TV u dnevnom boravku nije ukljucen.")

# if tv_kuhinja.je_ukljucen:
#     print("Status: TV u kuhinji je ukljucen.")
# else:
#     print("Status: TV u kuhinji nije ukljucen.")


# print("\nUkljuci tv u kuhinji")
# tv_kuhinja.ukljuci()
# if tv_dnevni_boravak.je_ukljucen:
#     print("Status: TV u dnevnom boravku je ukljucen.")
# else:
#     print("Status: TV u dnevnom boravku nije ukljucen.")

# if tv_kuhinja.je_ukljucen:
#     print("Status: TV u kuhinji je ukljucen.")
# else:
#     print("Status: TV u kuhinji nije ukljucen.")




class Televizor:
    def __init__(self, dijagonala, sirina, visina, proizvodac, model, je_ukljucen, program=0, glasnoca=0):
        self.dijagonala = dijagonala
        self.sirina = sirina
        self.visina = visina
        self.proizvodac = proizvodac
        self.model = model
        self.je_ukljucen = je_ukljucen
        self.program = program
        self.glasnoca = glasnoca
    
    def ukljuci(self):
        self.je_ukljucen = True
        self.program = 1
        self.glasnoca = 10

    def promijeni_program(self, program):
        self.program = program

    def podesi_glasnocu(self, podesavanje):
        if podesavanje == "glasnije":
            self.glasnoca += 1
        if podesavanje == "tise":
            self.glasnoca -= 1
        if podesavanje == "prigusi":
            self.glasnoca = 0


novi_tv_dnevni_boravak = Televizor(105, 250, 180, "Sony", "Bravia", False)
print(novi_tv_dnevni_boravak.sirina)
print(f"Status TV-a: {novi_tv_dnevni_boravak.je_ukljucen}, Program: {novi_tv_dnevni_boravak.program}, Glasnoca: {novi_tv_dnevni_boravak.glasnoca}")
novi_tv_dnevni_boravak.ukljuci()
print(f"Status TV-a: {novi_tv_dnevni_boravak.je_ukljucen}, Program: {novi_tv_dnevni_boravak.program}, Glasnoca: {novi_tv_dnevni_boravak.glasnoca}")

novi_tv_dnevni_boravak.promijeni_program(5)
print(f"Status TV-a: {novi_tv_dnevni_boravak.je_ukljucen}, Program: {novi_tv_dnevni_boravak.program}, Glasnoca: {novi_tv_dnevni_boravak.glasnoca}")


novi_tv_dnevni_boravak.podesi_glasnocu("glasnije")
print(f"Status TV-a: {novi_tv_dnevni_boravak.je_ukljucen}, Program: {novi_tv_dnevni_boravak.program}, Glasnoca: {novi_tv_dnevni_boravak.glasnoca}")

novi_tv_dnevni_boravak.podesi_glasnocu("tise")
print(f"Status TV-a: {novi_tv_dnevni_boravak.je_ukljucen}, Program: {novi_tv_dnevni_boravak.program}, Glasnoca: {novi_tv_dnevni_boravak.glasnoca}")

novi_tv_dnevni_boravak.podesi_glasnocu("prigusi")
print(f"Status TV-a: {novi_tv_dnevni_boravak.je_ukljucen}, Program: {novi_tv_dnevni_boravak.program}, Glasnoca: {novi_tv_dnevni_boravak.glasnoca}")

# class Televizor:
#     def __init__(self, dijagonala, sirina, visina, proizvodac, model, je_ukljucen=False): #unaprijed definirane vrijednosti, moraju biti napisane na kraju ne mogu biti u sredini
#         self.dijagonala = dijagonala
#         self.sirina = sirina
#         self.visina = visina
#         self.proizvodac = proizvodac
#         self.model = model
#         self.je_ukljucen = je_ukljucen
    
#     def ukljuci(self):
#         self.je_ukljucen = True


# novi_tv_dnevni_boravak = Televizor(105, 250, 180, "Sony", "Bravia")