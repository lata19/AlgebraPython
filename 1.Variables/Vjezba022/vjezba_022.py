vozila = {
    1: ["Kamion", "Iveco", "OS 001 ZZ", 2015, 45000.00],
    2: ["Kamion", "Iveco", "OS 002 ZZ", 2015, 47000.00],
    3: ["Tegljač", "MAN", "RI 001 ZZ", 2018, 78000.00],
    4: ["Tegljač", "MAN", "RI 001 ZZ", 2020, 97000.00],
    5: ["Kombi", "Meredes Benz", "ST 001 ZZ", 2013, 12000.00],
    6: ["Kombi", "Volkswagen", "ST 001 ZZ", 2021, 35000.00],
    7: ["Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", 2010, 9000.00],
    8: ["Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", 2010, 9300.00]
}
# CLEAR

# print()
# print("Ispis prije clear()")
# for key, value in vozila.items():
#     print(f"{key}", end="\t")
#     for element in value:
#         print(f"{element}", end="\t")
#     print()

# vozila.clear()
# print()

# print("Ispis nakon clear()")
# for key, value in vozila.items():
#     print(f"{key}", end="\t")
#     for element in value:
#         print(f"{element}", end="\t")
#     print()

#POP

# print()
# print("Ispis prije pop()")
# for key, value in vozila.items():
#     print(f"{key}", end="\t")
#     for element in value:
#         print(f"{element}", end="\t")
#     print()

# izbacena_vrijednost = vozila.pop(12, "Ne postoji traženi element u bazi")
# print(f"Izbačena vrijednost je: {izbacena_vrijednost}")
# print()

# print("Ispis nakon pop()")
# for key, value in vozila.items():
#     print(f"{key}", end="\t")
#     for element in value:
#         print(f"{element}", end="\t")
#     print()


#POPITEM
vozila[9] = ["kamion", 100]
print()
print("Ispis prije popitem()")
for key, value in vozila.items():
    print(f"{key}", end="\t")
    for element in value:
        print(f"{element}", end="\t")
    print()

# vrijednost = vozila.popitem()
# print(f"Vrijednost koju je vratio popitem: {vrijednost}")
# print()

# for broj in range(2):
#     vozila.popitem()

for broj in range(1,4):
    vozila.pop(broj)

print("Ispis nakon popitem()")
for key, value in vozila.items():
    print(f"{key}", end="\t")
    for element in value:
        print(f"{element}", end="\t")
    print()