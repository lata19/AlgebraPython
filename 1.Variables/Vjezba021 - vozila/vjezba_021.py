from tabulate import tabulate

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

# Header ROW
header_top_row = f"ID\tTip\t\tProizvođač\t\tRegistarska\t\tGodina prve\t\tCijena"
header_bottom_row = f"  \t  \t\t        \t\toznaka\t\t\tregistracije\t\t(EUR)"
header_line = "_" * 105
print(header_top_row, header_bottom_row, header_line, sep = "\n")

#Table BODY
for key, value in vozila.items():
    print(f"{key}", end = "\t")
    # print(f"{value}")
    # print(f"{value[0]}, {value[1]}, {value[2]}, {value[3]}, {value[4]}")
    for element in value:
        print("{:2d}".format{element}", end="\t\t")
    print()

# print("ID", "Tip", "Proizvođač", "Registarska oznaka", "Godina prve registracije", "Cijena u EUR", sep = "\t")

# for key, value in vozila.items():
#     print(key, value[0], value[1], value[2], value[3], value[4], sep = "\t")
