# Način bez inputa
glavnica = 10000
broj_godina = 15
kamata = 2.5

prinos = glavnica * (kamata/100) * broj_godina
ukupni_iznos = glavnica + prinos

print(f"Iznos oročen na štednju (glavnica) je: {glavnica} kn")
print(f"Vrijeme na koje je novac oročen na štednju: {broj_godina} godina")
print(f"Kamata iznosi: {kamata} %")
print(f"Iznos zarađene kamate (prinosa) iznosi: {round(prinos, 2)} kn")
print(f"Ukupan iznos na štednom računu: {round(ukupni_iznos, 2)} kn")

# Način s input-om
glavnica = float(input("Upišite iznos koji želite oročiti u štednju (u kunama): "))
broj_godina = float(input("Upišite broj godina na koje želite oročiti novac: "))
kamata = float(input("Upišite kamatnu stopu: "))

prinos = glavnica * (kamata/100) * broj_godina
ukupni_iznos = glavnica + prinos
print(f"Iznos oročen na štednju (glavnica) je: {glavnica} kn")
print(f"Vrijeme na koje je novac oročen na štednju: {broj_godina} godina")
print(f"Kamata iznosi: {kamata} %")
print(f"Iznos zarađene kamate (prinosa) iznosi: {round(prinos, 2)} kn")
print(f"Ukupan iznos na štednom računu: {round(ukupni_iznos, 2)} kn")