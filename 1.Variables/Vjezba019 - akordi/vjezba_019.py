tonovi = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]

print(f"Lista svih tonova: ")
for ton in tonovi:
    print(ton, end= ", ")
print()

pocetni_ton = input("Unesite početni ton akorda: ").upper()
i = True

while True:
    for ton in tonovi:
        if ton == pocetni_ton:
            index_pocetnog_tona = tonovi.index(pocetni_ton)
            i = False
            break

    if i == False:
        break
    else:
        pocetni_ton = input("Unesite odgovarajući početni ton akorda: ").upper()

tonovi.extend(tonovi)

akord = input("Unesite za koji akord želite tonove (Dur ili Mol): ")
i = True

while i == True:
    if akord.capitalize() == "Dur":
        print(f"Dur akord za pocetni ton {pocetni_ton} čine tonovi {pocetni_ton}, {tonovi[index_pocetnog_tona + 3]}, {tonovi[index_pocetnog_tona + 6]}")
        i = False
    elif akord.capitalize() == "Mol":
        print(f"Mol akord za pocetni ton {pocetni_ton} čine tonovi {pocetni_ton}, {tonovi[index_pocetnog_tona + 2]}, {tonovi[index_pocetnog_tona + 6]}")
        i = False
    else:
        akord = input("Unesite za koji akord želite tonove (Dur ili Mol): ")
