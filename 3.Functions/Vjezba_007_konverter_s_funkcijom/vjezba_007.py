# def konverter(user_pick):
#     """Funkcija koja konvertira unesene vrijednosti
#     prema odabiru ponuđenih konvertera"""
#     while user_pick != "stop":
#         if user_pick == "udaljenost" or user_pick == "temperatura" or user_pick == "masa" or user_pick == "obujam" or user_pick == "snaga" or user_pick == "valuta":
#             break
#         else:
#             print("Pogrešan unos. Molimo Vas pokušajte ponovo.")
#             user_pick = input("Upišite koju vrstu konverzije želite obaviti: ").lower()
    
#     # Kilometri u milje i obrnuto
#     if user_pick == "udaljenost":
#         print("1: Kilometar (km) u Milja (m)")
#         print("2: Milja (m) u Kilometar (km)")
#         user_way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
#         print("-" * 100)
#         if user_way == 1:
#             km = float(input("Upišite iznos kilometara koji želite konvertirati u milje: "))
#             mile = round(km * 0.621371192, 2)
#             print(f"{km} km = {mile} mi")
#             print("-" * 100)
#         elif user_way == 2:
#             mile = float(input("Upišite iznos milja koji želite konvertirati u kilometre: "))
#             km = round(mile * 1.609344, 2)
#             print(f"{mile} mi = {km} km")
#             print("-" * 100)
#     # Celzijus u Fahrenheit i obrnuto
#     elif user_pick == "temperatura":
#         print("1: Stupanj Celzijus (°C) u stupanj Fahrenheit (°F)")
#         print("2: Stupanj Fahrenheit u stupanj Celzijus (°C)")
#         user_way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
#         print("-" * 100)
#         if user_way == 1:
#             c = float(input("Upišite iznos stupnjeva Celzijusa koji želite konvertirati u stupanj Fahrenheita: "))
#             f = round(c * 1.8 + 32, 2)
#             print(f"{c} °C = {f} °F")
#             print("-" * 100)
#         elif user_way == 2:
#             f = float(input("Upišite iznos milja koji želite konvertirati u kilometre: "))
#             c = round((f - 32)/1.8, 2)
#             print(f"{f} °F = {c} °C")
#             print("-" * 100)
    
#     # Kilogram u Funtu i obrnuto
#     elif user_pick == "masa":
#         print("1: Kilogram (kg) u Funta (lbs)")
#         print("2: Funta (lbs) u Kilogram (kg)")
#         user_way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
#         print("-" * 100)
#         if user_way == 1:
#             kg = float(input("Upišite iznos kilograma koji želite konvertirati u funtu: "))
#             lbs = round(kg * 2.20462, 2)
#             print(f"{kg} kg = {lbs} lbs")
#             print("-" * 100)
#         elif user_way == 2:
#             lbs = float(input("Upišite iznos funti koji želite konvertirati u kilograma: "))
#             kg = round(lbs * 0.45359291, 2)
#             print(f"{lbs} lbs = {kg} kg")
#             print("-" * 100)
    
#     # Litra u Gallon i obrnuto
#     elif user_pick == "obujam":
#         print("1: Litra (l) u Gallon (gal)")
#         print("2: Gallon (gal) u Litra (l)")
#         user_way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
#         print("-" * 100)
#         if user_way == 1:
#             l = float(input("Upišite iznos litri koje želite konvertirati u gallone: "))
#             gal = round(l * 0.2641720524, 2)
#             print(f"{l} l = {gal} gal")
#             print("-" * 100)
#         elif user_way == 2:
#             gal = float(input("Upišite iznos gallona koje želite konvertirati u litre: "))
#             l = round(gal * 3.78541178, 2)
#             print(f"{gal} gal = {l} l")
#             print("-" * 100)
    
#     # Kilowatt u Konjsku snagu i obrnuto
#     elif user_pick == "snaga":
#         print("1: Kilowatt (kW) u Konjska snaga (KS)")
#         print("2: Konjska snaga (KS) u Kilowatt (kW)")
#         user_way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
#         print("-" * 100)
#         if user_way == 1:
#             kw = float(input("Upišite iznos Kilowatt-a koje želite konvertirati u Konjsku snagu: "))
#             ks = round(kw * 1,341, 2)
#             print(f"{kw} kW = {ks} KS")
#             print("-" * 100)
#         elif user_way == 2:
#             ks = float(input("Upišite iznos Konjske snage koje želite konvertirati u Kilowatte: "))
#             kw = round(ks * 0.745, 2)
#             print(f"{ks} KS = {kw} kW")
#             print("-" * 100)
    
#     # Kuna u Euro i obrnuto
#     elif user_pick == "valuta":
#         print("1: Euro (€) u Hrvatska kuna (kn)")
#         print("2: Hrvatska kuna (kn) u Euro (€)")
#         user_way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
#         print("-" * 100)
#         if user_way == 1:
#             euro = float(input("Upišite iznos Eura koje želite konvertirati u Hrvatsku kunu: "))
#             kn = round(euro * 7.5345, 2)
#             print(f"{euro} € = {kn} kn")
#             print("-" * 100)
#         elif user_way == 2:
#             kn = float(input("Upišite iznos Hrvatskih kuna koje želite konvertirati u Euro: "))
#             euro = round(kn * 0.132723, 2)
#             print(f"{kn} kn = {euro} €")
#             print("-" * 100)


# print("Moguće konverzije: Udaljenost, Temperatura, Masa, Obujam, Snaga, Valuta.\nAko želite prekinuti program upišite \"stop\"")
# pick = input("Upišite koju vrstu konverzije želite obaviti: ").lower()
# konverter(pick)





# NEW WAY
def distance_converter(user_way, dst):
    if user_way == 1:
        return round(dst * 0.621371192, 2)
    elif user_way == 2:
        return round(dst * 1.609344, 2)

def temperature_converter(user_way, tmp):
    if user_way == 1:
        return round(tmp * 1.8 + 32, 2)
    elif user_way == 2:
        return round((tmp - 32)/1.8, 2)

def mass_converter(user_way, mass):
    if user_way == 1:
        return round(mass * 2.20462, 2)
    elif user_way == 2:
        return round(lbs * 0.45359291, 2)

def volumen_converter(user_way, vol):
    if user_way == 1:
        return round(vol * 0.2641720524, 2)
    elif user_way == 2:
        return round(vol * 3.78541178, 2)

def power_converter(user_way, p):
    if user_way == 1:
        return round(p * 1.341, 2)
    elif user_way == 2:
        return round(p * 0.745, 2)

def currency_converter(user_way, cur):
    if user_way == 1:
        return round(cur * 7.5345, 2)
    elif user_way == 2:
        return round(cur * 0.132723, 2)


while True:
    print("Moguće konverzije: Udaljenost, Temperatura, Masa, Obujam, Snaga, Valuta.\nAko želite prekinuti program upišite \"stop\"")
    pick = input("Upišite koju vrstu konverzije želite obaviti: ").lower()

    if pick == "udaljenost":
        print("1: Kilometar (km) u Milja (m)")
        print("2: Milja (m) u Kilometar (km)")
        user_way = int(input("Upišite broj, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if user_way == 1:
            km = float(input("Upišite iznos kilometara koji želite konvertirati u milje: "))
            print(distance_converter(user_way, km))
            print("-" * 100)
        elif user_way == 2:
            mile = float(input("Upišite iznos milja koji želite konvertirati u kilometre: "))
            print(distance_converter(user_way, mile))
            print("-" * 100)

    elif pick == "temperatura":
        print("1: Stupanj Celzijus (°C) u stupanj Fahrenheit (°F)")
        print("2: Stupanj Fahrenheit u stupanj Celzijus (°C)")
        user_way = int(input("Upišite broj, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if user_way == 1:
            c = float(input("Upišite iznos stupnjeva Celzijusa koji želite konvertirati u stupanj Fahrenheita: "))
            print(temperature_converter(user_way, c))
        elif user_way == 2:
            f = float(input("Upišite iznos milja koji želite konvertirati u kilometre: "))
            print(temperature_converter(user_way, f))
    
    elif pick == "masa":
        print("1: Kilogram (kg) u Funta (lbs)")
        print("2: Funta (lbs) u Kilogram (kg)")
        user_way = int(input("Upišite broj, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if user_way == 1:
            kg = float(input("Upišite iznos kilograma koji želite konvertirati u funtu: "))
            print(mass_converter(user_way, kg))
        elif user_way == 2:
            lbs = float(input("Upišite iznos funti koji želite konvertirati u kilograma: "))
            print(mass_converter(user_way, lbs))
    
    elif pick == "obujam":
        print("1: Litra (l) u Gallon (gal)")
        print("2: Gallon (gal) u Litra (l)")
        user_way = int(input("Upišite broj, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if user_way == 1:
            l = float(input("Upišite iznos litri koje želite konvertirati u gallone: "))
            print(volumen_converter(user_way, l))
        elif user_way == 2:
            gal = float(input("Upišite iznos gallona koje želite konvertirati u litre: "))
            print(volumen_converter(user_way, gal))
    
    elif pick == "snaga":
        print("1: Kilowatt (kW) u Konjska snaga (KS)")
        print("2: Konjska snaga (KS) u Kilowatt (kW)")
        user_way = int(input("Upišite broj, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if user_way == 1:
            kw = float(input("Upišite iznos Kilowatt-a koje želite konvertirati u Konjsku snagu: "))
            print(power_converter(user_way, kw))
        elif user_way == 2:
            ks = float(input("Upišite iznos Konjske snage koje želite konvertirati u Kilowatte: "))
            print(power_converter(user_way, ks))
    
    elif pick == "valuta":
        print("1: Euro (€) u Hrvatska kuna (kn)")
        print("2: Hrvatska kuna (kn) u Euro (€)")
        user_way = int(input("Upišite broj, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if user_way == 1:
            euro = float(input("Upišite iznos Eura koje želite konvertirati u Hrvatsku kunu: "))
            currency_converter(user_way, euro)
        elif user_way == 2:
            kn = float(input("Upišite iznos Hrvatskih kuna koje želite konvertirati u Euro: "))
            currency_converter(user_way, kn)
    
    elif pick == "stop":
        break
    
    else:
        print("Pogrešan unos. Molimo Vas pokušajte ponovo.")