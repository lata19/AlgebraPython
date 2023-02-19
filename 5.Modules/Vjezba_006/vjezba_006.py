from DateTimeManager import DateTimeManager

class User:
    def __init__(self, first_name, last_name, oib):
        self.first_name = first_name
        self.last_name = last_name
        self.oib = oib

    def print_users(self):
        print(f"Ime: {self.first_name}, Prezime: {self.last_name}, OIB: {self.oib}")
    
class Appointment:
    def __init__(self, date, description):
        self.date = date
        self.description = description
    
    def print_appointments(self):
        print(f"Datum: {self.date}, Opis: {self.description}")


users = {}
appointments_dict = {}

while True:
    print("**********Unos podataka*********")
    first_name = input("Upišite ime korisnika: ")
    last_name = input("Upišite prezime korisnika: ")
    oib = input("Upišite OIB korisnika: ")

    user = User(first_name, last_name, oib)
    users[oib] = user
    while True:
        date = input("Upišite datum termina u formatu dan. mjesec godina. sat:minuta - ")
        date = DateTimeManager.dateConverter(date)
        description = input("Upišite opis termina: ")
        appointment = Appointment(date, description)
        appointments_dict[oib] = appointment
        # users[oib]["appointments"] = appointments_dict[oib]
        if input("Želite li dodati novi termin (da/ne): ").lower() != "da":
            break


    if input("Želite li dodati novog korisnika (da/ne): ").lower() != "da":
        break


for key, value in users.items():
    print(key, end="\t")
    print(value.print_users())

for key, value in appointments_dict.items():
    print(key, end="\t")
    print(value.print_appointments())

