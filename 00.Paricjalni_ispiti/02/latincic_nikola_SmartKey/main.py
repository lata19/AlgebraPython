from SmartKey import BazaPodataka, GrafickoSucelje

path = "00.Paricjalni_ispiti/02/latincic_nikola_SmartKey/SmartKey/SmartKey.db"
session = BazaPodataka.create_engine(path)

family = [
    ["Admin", "Admin", "9182", True],
    ["Ante", "Antic", "8907", True],
    ["Iva", "Ivic", "4325", True],
    ["Petra", "Peric", "3425", True],
    ["Ivan", "Horvat", "4256", True],
]

for person in family:
    BazaPodataka.add_person(
        session,
        first_name=person[0],
        last_name=person[1],
        pin=person[2],
        active=person[3],
    )
