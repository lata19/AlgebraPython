def vehicle_fuel_consumption(consumption, price):
    """Ova funkcija izračunava potrošnju goriva vozila
    izraženu u eurima prema podacima koje korisnik upiše"""
    consumption_eur = round(consumption * price, 2)
    x = (budget / distance) / price
    return x

fuel_consumption = input("Upišite potrošnju goriva Vašeg vozila: ")
fuel_price = input("Upišite cijenu goriva: ")
distance = input("Upišite udaljenost koju pređete u jednom mjesecu: ")
budget = input("Upišite mjesečni budžet za gorivo u Eurima: ")


