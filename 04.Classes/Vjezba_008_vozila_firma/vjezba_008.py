motorcycles = {}
personal_vehicles = {}
trucks = {}
working_machines = {}

# Klasa Vozilo
class Vehicle:
    def __init__(self, brand, model, year_of_production, country_of_production):
        self.brand = brand
        self.model = model
        self.year_of_production = year_of_production
        self.country_of_production = country_of_production


# Klasa Motocikl
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year_of_production, country_of_production, category):
        Vehicle.__init__(self, brand, model, year_of_production, country_of_production)
        self.category = category
    
    def print_vehicle(self):
        Vehicle.print(self)
        print(f"Kategorija vozila: {self.category}")

# Klasa Osobno vozilo (Auto)
class PersonalVehicle(Vehicle):
    def __init__(self, brand, model, year_of_production, country_of_production, vehicle_type):
        Vehicle.__init__(self, brand, model, year_of_production, country_of_production)
        self.vehicle_type = vehicle_type

    def print_vehicle(self):
        Vehicle.print(self)
        print(f"Oblik karoserije vozila: {self.vehicle_type}")

# Klasa Teretno vozilo (Kamion)
class Truck(Vehicle):
    def __init__(self, brand, model, year_of_production, country_of_production, category):
        Vehicle.__init__(self, brand, model, year_of_production, country_of_production)
        self.category = category

    def print_vehicle(self):
        Vehicle.print(self)
        print(f"Kategorija vozila: {self.category}")

# Klasa Radni stroj
class WorkMachine(Vehicle):
    def __init__(self, brand, model, year_of_production, country_of_production, working_machine_type):
        Vehicle.__init__(self, brand, model, year_of_production, country_of_production)
        self.working_machine_type = working_machine_type

    def print(self):
        Vehicle.print(self)
        print(f"Vrsta radnog stroja: {self.working_machine_type}")

# Funkcija za input podataka
def input_function(vehicle):
    plate_number = input("Upišite registraciju (Format: ZG0000AA): ").upper()
    brand = input("Upišite marku vozila: ").capitalize()
    model = input ("Upišite model vozila: ").capitalize()
    year_of_production = int(input("Upišite godinu proizvodnje: "))
    country_of_production = input("Upišite državu proizvodnje: ").capitalize()
    if vehicle == "motocikl":
        category = input("Upišite kategoriju motocikla: ").capitalize()
        mc = Motorcycle(brand, model, year_of_production, country_of_production, category)
        motorcycles[plate_number] = mc.__dict__
        return motorcycles

    elif vehicle == "auto":
        vehicle_type = input("Upišite oblik karoserije vozila: ").capitalize()
        personal_vehicles[plate_number] = {
            "Marka": brand,
            "Model": model,
            "Godina proizvodnje": year_of_production,
            "Država proizvodnje": country_of_production,
            "Oblik karoserije vozila": vehicle_type
        }
    elif vehicle == "kamion":
        category = input("Upišite kategoriju motocikla: ").capitalize()
        trucks[plate_number] = {
            "Marka": brand,
            "Model": model,
            "Godina proizvodnje": year_of_production,
            "Država proizvodnje": country_of_production,
            "Kategorija teretnog vozila": category
        }
    elif vehicle == "radni stroj":
        working_machine_type = input("Upišite vrstu radnog stroja: ").capitalize()
        working_machines[plate_number] = {
            "Marka": brand,
            "Model": model,
            "Godina proizvodnje": year_of_production,
            "Država proizvodnje": country_of_production,
            "Vrsta radnog stroja": working_machine_type
        }


while True:
    vehicle = input("Upišite vrstu vozila (Motocikl, Auto, Kamion ili Radni stroj): ").lower()
    if vehicle != "motocikl" and vehicle != "auto" and vehicle != "kamion"  and vehicle != "radni stroj":
        print("Pogrešan unos. Pokušajte ponovo.")
    else:
        input_function(vehicle)
        answer = input("Želite li dodati novo vozilo? (d/n): ")
        if answer == "n":
            break

for motorcycle in motorcycles.items():
    print("Popis motocikala:")
    print(motorcycle)


"""
motorcycles = {
    ZG6545TR: {
        "brand": Honda,
        "model": 234,
        "year_of_production": 2021,
        "country_of_production": Japan,
        "category": A3, 
    }
}
"""