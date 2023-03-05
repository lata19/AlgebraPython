game = ""

while game != "stop":
    print("1: Kilometar (km) - Milja (m)")
    print("2: Stupanj Celzijus (°C) - Stupanj Fahrenheit (°F)")
    print("3: Kilogram (kg) - Funta (lbs) ")
    print("4: Litra (l) - Gallon ()")
    print("5: Kilowatt (kW) - Konjska snaga (KS)")
    print("6: Kuna (HRK) - Euro (€)")
    selection = int(input("Upišite broj prema popisu za koji želite obaviti konverziju: "))
    print("-" * 100)

    # Provjera jesu li upisan odgovarajući broj
    while True:
        if selection != 1 and selection != 2 and selection != 3 and selection != 4 and selection != 5 and selection != 6:
            print("Pogrešan unos. Pokušajte ponovo!")
            print("-" * 100)
            print("1: Kilometar (km) - Milja (m)")
            print("2: Stupanj Celzijus (°C) - Stupanj Fahrenheit (°F)")
            print("3: Kilogram - Funta (Pounds) ")
            print("4: Litra - Gallon")
            print("5: Kilowatt (kW) - Konjska snaga (KS)")
            print("6: Kuna (HRK) - Euro (€)")
            selection = int(input("Upišite broj prema popisu za koji želite obaviti konverziju: "))
            print("-" * 100)
        else:
            break
    # Provjera koji je broj unesen
    # Kilometri u milje i obrnuto         
    if selection == 1:
        print("1: Kilometar (km) u Milja (m)")
        print("2: Milja (m) u Kilometar (km)")
        way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if way == 1:
            km = float(input("Upišite iznos kilometara koji želite konvertirati u milje: "))
            mile = km * 0.621371192
            print(f"{km} km = {round(mile, 2)} mi")
            print("-" * 100)
        elif way == 2:
            mile = float(input("Upišite iznos milja koji želite konvertirati u kilometre: "))
            km = mile * 1.609344
            print(f"{mile} mi = {round(km, 2)} km")
            print("-" * 100)
    
    # Celzijus u Fahrenheit i obrnuto
    elif selection == 2:
        print("1: Stupanj Celzijus (°C) u stupanj Fahrenheit (°F)")
        print("2: Stupanj Fahrenheit u stupanj Celzijus (°C)")
        way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if way == 1:
            c = float(input("Upišite iznos stupnjeva Celzijusa koji želite konvertirati u stupanj Fahrenheita: "))
            f = c * 1.8 + 32
            print(f"{c} °C = {round(f, 2)} °F")
            print("-" * 100)
        elif way == 2:
            f = float(input("Upišite iznos milja koji želite konvertirati u kilometre: "))
            c = (f - 32)/1.8
            print(f"{f} °F = {round(c, 2)} °C")
            print("-" * 100)
    
    # Kilogram u Funtu i obrnuto
    elif selection == 3:
        print("1: Kilogram (kg) u Funta (lbs)")
        print("2: Funta (lbs) u Kilogram (kg)")
        way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if way == 1:
            kg = float(input("Upišite iznos kilograma koji želite konvertirati u funtu: "))
            lbs = kg * 2.20462
            print(f"{kg} kg = {round(lbs, 2)} lbs")
            print("-" * 100)
        elif way == 2:
            lbs = float(input("Upišite iznos funti koji želite konvertirati u kilograma: "))
            kg = lbs * 0.45359291
            print(f"{lbs} lbs = {round(kg, 2)} kg")
            print("-" * 100)
    
    # Litra u Gallon i obrnuto
    elif selection == 4:
        print("1: Litra (l) u Gallon (gal)")
        print("2: Gallon (gal) u Litra (l)")
        way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if way == 1:
            l = float(input("Upišite iznos litri koje želite konvertirati u gallone: "))
            gal = l * 0.2641720524
            print(f"{l} l = {round(gal, 2)} gal")
            print("-" * 100)
        elif way == 2:
            gal = float(input("Upišite iznos gallona koje želite konvertirati u litre: "))
            l = gal * 3.78541178
            print(f"{gal} gal = {round(l, 2)} l")
            print("-" * 100)
    
    # Kilowatt u Konjsku snagu i obrnuto
    elif selection == 5:
        print("1: Kilowatt (kW) u Konjska snaga (KS)")
        print("2: Konjska snaga (KS) u Kilowatt (kW)")
        way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if way == 1:
            kw = float(input("Upišite iznos Kilowatt-a koje želite konvertirati u Konjsku snagu: "))
            ks = kw * 1,341
            print(f"{kw} kW = {round(ks, 2)} KS")
            print("-" * 100)
        elif way == 2:
            ks = float(input("Upišite iznos Konjske snage koje želite konvertirati u Kilowatte: "))
            kw = ks * 0.745
            print(f"{ks} KS = {round(kw, 2)} kW")
            print("-" * 100)
    
    # Kuna u Euro i obrnuto
    elif selection == 6:
        print("1: Euro (€) u Hrvatska kuna (kn)")
        print("2: Hrvatska kuna (kn) u Euro (€)")
        way = int(input("Upišite, prema popisu, u kojem smjeru želite obaviti konverziju: "))
        print("-" * 100)
        if way == 1:
            euro = float(input("Upišite iznos Eura koje želite konvertirati u Hrvatsku kunu: "))
            kn = euro * 7.5345
            print(f"{euro} € = {round(kn, 2)} kn")
            print("-" * 100)
        elif way == 2:
            kn = float(input("Upišite iznos Hrvatskih kuna koje želite konvertirati u Euro: "))
            euro = kn * 0.132723
            print(f"{kn} kn = {round(euro, 2)} €")
            print("-" * 100)

        game = input("Za kraj programa upišite \"stop\": ")
        game = game.lower()     