import os
import datetime

accounts = {}
currency = ""
def otvaranje_racuna():
    """Funkcija koja otvara računa u banci"""

    global currency
    os.system("cls")
    print("*" * 100)
    print("{:^100}".format("PyBank Algebra\n"))
    print("{:^100}".format("KREIRANJE RAČUNA\n"))

    company_name = input("{:<55}".format("Upišite ime Vaše tvrtke: "))
    adress = input("{:<55}".format("Upišite adresu i kućni broj sjedišta vaše tvrtke: "))
    zip_code = input("{:<55}".format("Upišite poštanski broj sjedišta Vaše tvrtke: "))
    city = input("{:<55}".format("Upišite grad u kojem je sjedište Vaše tvrtke: "))
    oib = input("{:<55}".format("Upišite OIB Vaše tvrtke: "))
    ap_name = input("{:<55}".format("Upišite ime i prezime ovlaštene osobe: ")) # ap = authorized person
    while len(oib) != 11:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        oib = input("Upišite OIB Vaše tvrtke: ")
    currency = ""
    while currency != "EUR" and currency != "HRK":
        currency = input("Odaberite valutu računa (EUR ili HRK): ").upper()

    input("Pritisnite bilo koju tipku za nastavak: ")

    i = 1
    for konto in accounts:
        i +=1
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    new_account = f"BA-{year}-{month}-{i}"

    accounts[new_account] = {
    "Naziv tvrtke": company_name,
    "Adresa": adress,
    "Poštanski broj": zip_code,
    "Grad": city,
    "OIB": oib,
    "Odgovorna osoba": ap_name,
    "Valuta": currency,
    "Balance": 0.0,
    "Promet po računu": []
    }

    os.system("cls")
    print("*" * 100)
    print("{:^100}".format("PyBank Algebra\n"))
    print("{:^100}".format("KREIRANJE RAČUNA\n"))
    print("Stanje računa\n")
    print(f"Broj računa: {new_account}")
    print("Trenutno stanje računa: {} {}".format(accounts[new_account]["Balance"], currency))
    payment = float(input("Upišite iznos koji želite položiti na račun: "))
    accounts[new_account]["Balance"] += payment
    accounts[new_account]["Promet po računu"].append(f"Uplata ({datetime.datetime.now()}): {payment} {currency}")

    print(accounts)


def prikaz_stanja_racuna():
    """Funkcija koja ispisuje stanje računa"""

    os.system("cls")
    print("*" * 100)
    print("{:^100}".format("PyBank Algebra\n"))
    print("{:^100}".format("PRIKAZ STANJA RAČUNA\n"))
    oib = input("Upišite OIB Vaše tvrtke: ")
    while len(oib) != 11:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        oib = input("Upišite Vaš OIB: ")
    while True:
        account_number = input("Upišite broj Vašeg računa: ")
        if account_number in accounts:
            break
        else:
            print("Broj računa nije ispravan. Pokušajte ponovo.")
    
    for k, v in accounts.items():
        if k == account_number:
            balance = v["Balance"]
            break
    
    os.system("cls")
    print("*" * 100)
    print("{:^100}".format("PyBank Algebra\n"))
    print("{:^100}".format("PRIKAZ STANJA RAČUNA\n"))
    print(f"Broj računa: {k}")
    print(f"Datum i vrijeme: {datetime.datetime.now()}\n")
    print(f"Stanje računa: {balance} {currency}")
    input("Pritisnite bilo koju tipku za nastavak: ")

def prikaz_prometa_po_racunu():
    """Funkcija koja na ekranu ispisuje promet po računu"""

    os.system("cls")
    print("*" * 100)
    print("{:^100}".format("PyBank Algebra\n"))
    print("{:^100}".format("PRIKAZ PROMETA PO RAČUNU\n"))
    oib = input("Upišite OIB Vaše tvrtke: ")
    while len(oib) != 11:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        oib = input("Upišite Vaš OIB: ")
    while True:
        account_number = input("Upišite broj Vašeg računa: ")
        if account_number in accounts:
            break
        else:
            print("Broj računa nije ispravan. Pokušajte ponovo.")
    
    for k, v in accounts.items():
        if k == account_number:
            account_traffic = v["Promet po računu"]
            break

    os.system("cls")
    print("*" * 100)
    print("{:^100}".format("PyBank Algebra\n"))
    print("{:^100}".format("PRIKAZ PROMETA PO RAČUNU\n"))
    print(f"Broj računa: {k}")
    print(f"Datum i vrijeme: {datetime.datetime.now()}\n")
    print(f"Promet po računu:\n{account_traffic}")
    input("Pritisnite bilo koju tipku za nastavak: ")

def polog_novca():
    """Funkcija za polog novca na račun"""

    os.system("cls")
    print("*" * 100)
    print("{:^100}".format("PyBank Algebra\n"))
    print("{:^100}".format("POLOG NOVCA NA RAČUN\n"))
    oib = input("Upišite Vaš OIB: ")
    while len(oib) != 11:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        oib = input("Upišite Vaš OIB: ")
    while True:
        account_number = input("Upišite broj Vašeg računa: ")
        if account_number in accounts:
            break
        else:
            print("Broj računa nije ispravan. Pokušajte ponovo.")
    for k, v in accounts.items():
        if k == account_number:
            balance = v["Balance"]
            os.system("cls")
            print("*" * 100)
            print("{:^100}".format("PyBank Algebra\n"))
            print("{:^100}".format("POLOG NOVCA NA RAČUN\n"))
            print(f"Broj računa: {k}")
            print(f"Datum i vrijeme: {datetime.datetime.now()}\n")
            print(f"Stanje računa: {balance} {currency}")
            payment = float(input("Upišite iznos koji želite uplatiti na svoj račun: "))
            v["Balance"] += payment
            v["Promet po računu"].append(f"Uplata ({datetime.datetime.now()}): {payment} {currency}")
            break
        
    os.system("cls")
    print("*" * 100)
    print("{:^100}".format("PyBank Algebra\n"))
    print("{:^100}".format("POLOG NOVCA NA RAČUN\n"))
    print(f"Broj računa: {k}")
    print(f"Datum i vrijeme: {datetime.datetime.now()}\n")
    print("Stanje Vašeg računa nakon provedene transakcije: {} {}".format(v["Balance"], currency))
    input("Pritisnite bilo koju tipku za nastavak: ")


def podizanje_novca():
    """Funkcija za podizanje novca s računa"""

    os.system("cls")
    print("*" * 100)
    print("{:^100}".format("PyBank Algebra\n"))
    print("{:^100}".format("PODIZANJE NOVCA S RAČUN\n"))
    oib = input("Upišite Vaš OIB: ")
    while len(oib) < 11 and len(oib) > 11:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        oib = input("Upišite Vaš OIB: ")
    while True:
        account_number = input("Upišite broj Vašeg računa: ")
        if account_number in accounts:
            break
        else:
            print("Broj računa nije ispravan. Pokušajte ponovo.")

    for k, v in accounts.items():
            if k == account_number:
                balance = v["Balance"]
                os.system("cls")
                print("*" * 100)
                print("{:^100}".format("PyBank Algebra\n"))
                print("{:^100}".format("PODIZANJE NOVCA s RAČUN\n"))
                print(f"Broj računa: {k}")
                print(f"Datum i vrijeme: {datetime.datetime.now()}\n")
                print(f"Stanje računa: {balance} {currency}")
                while True:
                    payment = float(input("Upišite iznos koji želite podići sa svog računa: "))
                    if payment > v["Balance"]:
                        print("Nedovoljan iznos sredstava na računu. Molimo Vas pokušajte ponovo.")
                    else:
                        break
                v["Balance"] -= payment
                v["Promet po računu"].append(f"Isplata ({datetime.datetime.now()}): {payment} {currency}")
                break
            
    os.system("cls")
    print("*" * 100)
    print("{:^100}".format("PyBank Algebra\n"))
    print("{:^100}".format("POLOG NOVCA NA RAČUN\n"))
    print(f"Broj računa: {k}")
    print(f"Datum i vrijeme: {datetime.datetime.now()}\n")
    print("Stanje Vašeg računa nakon provedene transakcije: {} {}".format(v["Balance"], currency))
    input("Pritisnite bilo koju tipku za nastavak: ")



# izbornik
def main_menu():
    """Funkcija za pokretanje glavnog izbornika banke"""
    
    os.system("cls")

    while True:
        os.system("cls")
        print("*" * 100)
        print("{:^100}".format("PyBank Algebra\n"))
        print("{:^100}".format("GLAVNI IZBORNIK\n"))
        print("1. Otvaranje računa\n2. Prikaz stanja računa\n3. Prikaz prometa po računu\n4. Polog novca\n5. Podizanje novca\n0. Izlaz")
        print("-" * 100)

        if accounts == {}:
            print("Još niste otvorili račun. Molimo Vas da prvo otvorite račun. Hvala!")
            print("-" * 100)

        action = int(input("Vaš izbor: "))
        if action == 1:
            otvaranje_racuna()
        elif action == 2:
            prikaz_stanja_racuna()
        elif action == 3:
            prikaz_prometa_po_racunu()
        elif action == 4:
            polog_novca()
        elif action == 5:
            podizanje_novca()
        elif action == 0:
            os.system("cls")
            print("*" * 100)
            print("{:^100}".format("PyBank Algebra\n"))
            print("{:^100}".format("GLAVNI IZBORNIK\n"))
            print("{:^100}".format("Hvala što ste koristili usluge naše banke!\n"))
            break
        else:
            print("Pogrešan unos. Molimo vas pokušajte ponovo.")
        

main_menu()