


# ADRESAR - Pokusaj 1
brojac = 1
while True:
    ime = input("Upisite ime kontakta: ")
    prezime = input("Upisite prezime kontakta: ")
    telefon = input("Upisite telefon kontakta: ")

    file_writer = open("6.Files/Vjezba_002/adresar.txt", "a")

    file_writer.write(f"{brojac}{ime};{prezime};{telefon}\n")
    brojac += 1

    file_writer.close()

    if input("Zelite li unijeti novi kontakt (da/ne): ") != "da":
        break