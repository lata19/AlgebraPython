def print_6r_table(rijecnik):
    print("{:^5} {:^18} {:^12} {:^20} {:^25} {:^12}".format("ID", "Tip", "Proizvođač", "Registarska oznaka", "Godina prve registracije", "Cijena u EUR"))
    print("*" * 100)
    for key, value in rijecnik.items():
        tip, pro, reg, god, c = value
        print("{:^5} {:^18} {:^12} {:^20} {:^25} {:^12}".format(key, tip, pro, reg, god, c))
        print("-" * 100)
        print()

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

print_6r_table(vozila)