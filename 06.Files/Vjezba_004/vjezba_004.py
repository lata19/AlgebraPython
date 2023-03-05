brojac = 1

while True:
    ime = input("Upisite ime kontakta: ")
    prezime = input("Upisite prezime kontakta: ")
    telefon = input("Upisite telefon kontakta: ")

    try:
        # file_writer = open("6.Files/Vjezba_002/adresar.txt", "a")

        # file_writer.write(f"{brojac}{ime};{prezime};{telefon}\n")
        # brojac += 1
        with open("6.Files/Vjezba_002/adresar2.txt", "a") as file_writer:
            file_writer.write(f"{brojac}{ime};{prezime};{telefon}\n")
            brojac += 1

    except Exception as e:
        print(f"Dogodila se pogrška {e}")


    if input("Zelite li unijeti novi kontakt (da/ne): ") != "da":
        break