# Način bez inputa
consumption_per_100km = 5.3
fuel_price_per_liter = 9.56
price_per_km = (consumption_per_100km / 100) * fuel_price_per_liter
print(f"Kilometar vožnje automobilom košta {price_per_km} kn")
job_trip_length = 20
month = 30

monthly_fuel_cost = price_per_km * (job_trip_length * 2) * month

print(f"Vozilo troši {consumption_per_100km} litara/100 km")
print(f"Cijena goriva je {fuel_price_per_liter} kn/litra")
print(f"Udaljenost do posla je {job_trip_length} km")
print(f"Mjesečna potrošnja goriva za putovanje na posao i s posla iznosi: {round(monthly_fuel_cost, 2)} kn")



# Način s input-om
fuel = input("Upišite vrstu goriva koje koristi vaš automobil: ")
consumption_per_100km = float(input(f"Upišite potrošnju {fuel}a vašeg automobila: "))
fuel_price_per_liter = float(input(f"Upišite cijenu {fuel}a u kunama: "))
price_per_km = (consumption_per_100km / 100) * fuel_price_per_liter
print(f"Kilometar vožnje automobilom košta {price_per_km} kn")
job_trip_length = float(input("Upišite duljinu putovanja na posao u kilometrima (za jedan smjer): "))
month = int(input("Upišite koliko dana ima u mjesecu: "))

monthly_fuel_cost = price_per_km * (job_trip_length * 2) * month

print(f"Vozilo troši {consumption_per_100km} litara/100 km")
print(f"Cijena goriva je {fuel_price_per_liter} kn/litra")
print(f"Udaljenost do posla je {job_trip_length} km")
print(f"Mjesečna potrošnja goriva za putovanje na posao i s posla iznosi: {round(monthly_fuel_cost, 2)} kn")


