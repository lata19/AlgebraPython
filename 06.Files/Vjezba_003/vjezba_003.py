brojac = 1
while True:
    ime = input("Upisite ime kontakta: ")
    prezime = input("Upisite prezime kontakta: ")
    telefon = input("Upisite telefon kontakta: ")

    try:
        file_writer = open("6.Files/Vjezba_002/adresar.txt", "a")

        file_writer.write(f"{brojac}{ime};{prezime};{telefon}\n")
        brojac += 1
    except Exception as e:
        print(f"Dogodila se pogrška {e}")

    finally:
        #bez obzira je li se dogodila greška ili nije
        # UVIJEK cemo zatvoriti komunikaciju prema datoteci
        file_writer.close()

    if input("Zelite li unijeti novi kontakt (da/ne): ") != "da":
        break