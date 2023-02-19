motorcycles = []
personal_vehicles = []
trucks = []

class Vehicle:
    def __init__(self, brand, model, year_of_production, status, lenght, width, height, number_of_wheels, wheelbase, number_of_seats, engine_power, max_speed, mass, capacity, category, fuel):
        self.brand = brand
        self.model = model
        self.year_of_production = year_of_production
        self.status = status
        self.lenght = lenght
        self.width = width
        self.height = height
        self.number_of_wheels = number_of_wheels
        self.wheelbase = wheelbase
        self.number_of_seats = number_of_seats
        self.engine_power = engine_power
        self.max_speed = max_speed
        self.mass = mass
        self.capacity = capacity
        self.category = category
        self.fuel = fuel
    
    def print(self):
        print(f"Marka: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Godina prizvodnje: {self.year_of_production}")
        print(f"Status: {self.status}")
        print(f"Dužina: {self.lenght}")
        print(f"Širina: {self.width}")
        print(f"Visina: {self.height}")
        print(f"Broj kotača: {self.number_of_wheels}")
        print(f"Osovinski razmak: {self.wheelbase}")
        print(f"Broj sjedala: {self.number_of_seats}")
        print(f"Snaga motora: {self.engine_power}")
        print(f"Maksimalna brzina: {self.max_speed}")
        print(f"Masa: {self.mass}")
        print(f"Nosivnost: {self.capacity}")
        print(f"Kategorija: {self.category}")
        print(f"Pogon: {self.fuel}")

# Motocikl
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year_of_production, status, lenght, width, height, number_of_wheels, wheelbase, number_of_seats, engine_power, max_speed, mass, capacity, category, fuel, shock_absorbers, brakes):
        Vehicle.__init__(self, brand, model, year_of_production, status, lenght, width, height, number_of_wheels, wheelbase, number_of_seats, engine_power, max_speed, mass, capacity, category, fuel)
        self.shock_absorbers = shock_absorbers
        self.brakes = brakes

    def print(self):
        Vehicle.print(self)
        print(f"Vrsta amortizera: {self.shock_absorbers}")
        print(f"Vrsta kočnica: {self.brakes}")

# Osobno vozilo
class PersonalVehicle(Vehicle):
    def __init__(self, brand, model, year_of_production, status, lenght, width, height, number_of_wheels, wheelbase, number_of_seats, engine_power, max_speed, mass, capacity, category, fuel, number_of_doors, vehicle_type):
        Vehicle.__init__(self, brand, model, year_of_production, status, lenght, width, height, number_of_wheels, wheelbase, number_of_seats, engine_power, max_speed, mass, capacity, category, fuel)
        self.number_of_doors = number_of_doors
        self.vehicle_type = vehicle_type

    def print(self):
        Vehicle.print(self)
        print(f"Broj vrata: {self.number_of_doors}")
        print(f"Oblik vozila: {self.vehicle_type}")

# Teretno vozilo
class Truck(Vehicle):
    def __init__(self, brand, model, year_of_production, status, lenght, width, height, number_of_wheels, wheelbase, number_of_seats, engine_power, max_speed, mass, capacity, category, fuel, number_of_trailers, trailer_volume):
        Vehicle.__init__(self, brand, model, year_of_production, status, lenght, width, height, number_of_wheels, wheelbase, number_of_seats, engine_power, max_speed, mass, capacity, category, fuel)
        self.number_of_trailers = number_of_trailers
        self.trailer_volume = trailer_volume


    def print(self):
        Vehicle.print(self)
        print(f"Broj prikolica: {self.number_of_trailers}")
        print(f"Volumen prikolice: {self.trailer_volume}")

while True:
    vehicle = input("Upišite vrstu vozila (Motocikl, Osobno vozilo ili Teretno vozilo): ").lower()
    if vehicle == "motocikl":
        m_count = len(motorcycles) + 1
        brand = input("Upišite marku motocikla: ")
        model = input("Upišite model motocikla: ")
        year_of_production = input("Upišite godinu proizvodnje motocikla: ")
        status = input("Upišite status motocikla: (Ukljuceno/Iskljuceno) ")
        lenght = input("Upišite dužinu motocikla: ")
        width = input("Upišite širinu motocikla: ")
        height = input("Upišite visinu motocikla: ")
        number_of_wheels = input("Upišite broj kotača motocikla: ")
        wheelbase = input("Upišite osovinski razmak motocikla: ")
        number_of_seats = input("Upišite broj sjedala motocikla: ")
        engine_power = input("Upišite snagu motora motocikla: ")
        max_speed = input("Upišite maksimalnu brzinu motocikla: ")
        mass = input("Upišite masu motocikla: ")
        capacity = input("Upišite nosivost motocikla: ")
        category = input("Upišite kategoriju motocikla: ")
        fuel = input("Upišite pogonsko gorivo motocikla: ")
        shock_absorbers = input("Upišite vrstu amortizera motocikla: ")
        brakes = input("Upišite vrstu kočnca motocikla: ")
        
        mc = Motorcycle(brand, model, year_of_production, status, lenght, width, height, number_of_wheels, wheelbase, number_of_seats, engine_power, max_speed, mass, capacity, category, fuel, shock_absorbers, brakes)
        motorcycles.append(mc)
        answer = input("Želite li dodati novo vozilo? (d/n)")
        if answer == "n":
            break
        
    elif vehicle == "osobno vozilo":
        pv_count = len(personal_vehicles) + 1
        brand = input("Upišite marku osobnog vozila: ")
        model = input("Upišite model osobnog vozila: ")
        year_of_production = input("Upišite godinu proizvodnje osobnog vozila: ")
        status = input("Upišite status osobnog vozila: ")
        lenght = input("Upišite dužinu osobnog vozila: ")
        width = input("Upišite širinu osobnog vozila: ")
        height = input("Upišite visinu osobnog vozila: ")
        number_of_wheels = input("Upišite broj kotača osobnog vozila: ")
        wheelbase = input("Upišite osovinski razmak osobnog vozila: ")
        number_of_seats = input("Upišite broj sjedala osobnog vozila: ")
        engine_power = input("Upišite snagu motora osobnog vozila: ")
        max_speed = input("Upišite maksimalnu brzinu osobnog vozila: ")
        mass = input("Upišite masu osobnog vozila: ")
        capacity = input("Upišite nosivost osobnog vozila: ")
        category = input("Upišite kategoriju osobnog vozila: ")
        fuel = input("Upišite pogonsko gorivo osobnog vozila: ")
        number_of_doors = input("Upišite broj vrata osobnog vozila: ")
        vehicle_type = input("Upišite oblik vozila: ")

        pv = PersonalVehicle(brand, model, year_of_production, status, lenght, width, height, number_of_wheels, wheelbase, number_of_seats, engine_power, max_speed, mass, capacity, category, fuel, shock_absorbers, brakes)
        personal_vehicles.append(pv)
        answer = input("Želite li dodati novo vozilo? (d/n)")
        if answer == "n":
            break
    
    elif vehicle == "teretno vozilo":
        t_count = len(trucks) + 1
        brand = input("Upišite marku teretnog vozila: ")
        model = input("Upišite model teretnog vozila: ")
        year_of_production = input("Upišite godinu proizvodnje teretnog vozila: ")
        status = input("Upišite status teretnog vozila: ")
        lenght = input("Upišite dužinu teretnog vozila: ")
        width = input("Upišite širinu teretnog vozila: ")
        height = input("Upišite visinu teretnog vozila: ")
        number_of_wheels = input("Upišite broj kotača teretnog vozila: ")
        wheelbase = input("Upišite osovinski razmak teretnog vozila: ")
        number_of_seats = input("Upišite broj sjedala teretnog vozila: ")
        engine_power = input("Upišite snagu motora teretnog vozila: ")
        max_speed = input("Upišite maksimalnu brzinu teretnog vozila: ")
        mass = input("Upišite masu teretnog vozila: ")
        capacity = input("Upišite nosivost teretnog vozila: ")
        category = input("Upišite kategoriju teretnog vozila: ")
        fuel = input("Upišite pogonsko gorivo teretnog vozila: ")
        number_of_trailers = input("Upišite broj prikolica teretnog vozila: ")
        trailer_volume = input("Upišite volumen prikolice teretnog vozila: ")

        t = Truck(brand, model, year_of_production, status, lenght, width, height, number_of_wheels, wheelbase, number_of_seats, engine_power, max_speed, mass, capacity, category, fuel, shock_absorbers, brakes)
        trucks.append(t)
        answer = input("Želite li dodati novo vozilo? (d/n)")
        if answer == "n":
            break


for m in motorcycles:
    print("Popis motocikala:")
    m.print()
    print()

for pv in personal_vehicles:
    print("Popis osobnih vozila:")
    pv.print()
    print()

for t in trucks:
    print("Popis teretnih vozila:")
    t.print()
    print()