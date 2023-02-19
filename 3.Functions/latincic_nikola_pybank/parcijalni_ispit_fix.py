import os
from datetime import datetime

accounts = {
    "BA-2023-2-00001": {
        "Naziv tvrtke": "Algebra",
        "Adresa": "Maksimirska 158",
        "Poštanski broj": "10000",
        "Grad": "Zagreb",
        "OIB": "05306114531",
        "Odgovorna osoba": "Nikola Latincic",
        "Valuta": "EUR",
        "Balance": 125500.0,
    }
}
account_traffic = {}
currency = ""
def otvaranje_racuna():
    """Funkcija koja otvara računa u banci"""

    global currency
    start_screen()
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

    i = len(accounts) + 1
    day, month, year, hour, minute, second = date_check()
    year = datetime.now().year
    month = datetime.now().month
    new_account = f"BA-{year}-{month}-{str(i).zfill(5)}"

    accounts[new_account] = {
    "Naziv tvrtke": company_name,
    "Adresa": adress,
    "Poštanski broj": zip_code,
    "Grad": city,
    "OIB": oib,
    "Odgovorna osoba": ap_name,
    "Valuta": currency,
    "Balance": 0.0,
    }
    account_traffic[new_account] = {}

    start_screen()
    print("Stanje računa\n")
    print(f"Broj računa: {new_account}")
    print("Trenutno stanje računa: {} {}".format(accounts[new_account]["Balance"], currency))
    payment = float(input("Upišite iznos koji želite položiti na račun: "))
    accounts[new_account]["Balance"] += payment
    day, month, year, hour, minute, second = date_check()
    date = f"{day}.{month}.{year}., {hour}:{minute}:{second}"
    account_traffic[new_account] = {
        f"Uplata: {date}": payment
    }

def prikaz_stanja_racuna():
    """Funkcija koja ispisuje stanje računa"""

    start_screen()
    print("{:^100}".format("PRIKAZ STANJA RAČUNA\n"))

    account_number = user_check()
    balance = accounts[account_number]["Balance"]

    
    start_screen()
    print(f"Broj računa: {account_number}")
    print(f"Datum i vrijeme: {datetime.now()}\n")
    print(f"Stanje računa: {balance} {currency}")
    input("Pritisnite bilo koju tipku za nastavak: ")

def prikaz_prometa_po_racunu():
    """Funkcija koja na ekranu ispisuje promet po računu"""

    start_screen()
    print("{:^100}".format("PRIKAZ PROMETA PO RAČUNU\n"))
    
    account_number = user_check()

    start_screen()
    print(f"Broj računa: {account_number}")
    print(f"Datum i vrijeme: {datetime.now()}\n")
    print("Promet po računu:")
    for v in account_traffic.values():
        print(v)
    input("Pritisnite bilo koju tipku za nastavak: ")

def polog_novca():
    """Funkcija za polog novca na račun"""
    start_screen()
    print("{:^100}".format("POLOG NOVCA NA RAČUN\n"))
    account_number = user_check()
    for k, v in accounts.items():
        if k == account_number:
            os.system("cls")
            print("*" * 100)
            print("{:^100}".format("PyBank Algebra\n"))
            print("{:^100}".format("POLOG NOVCA NA RAČUN\n"))
            print(f"Broj računa: {k}")
            print(f"Datum i vrijeme: {datetime.now()}\n")
            print(f"Stanje računa: {v['Balance']} {currency}")
            payment = float(input("Upišite iznos koji želite uplatiti na svoj račun: "))
            v["Balance"] += payment
            day, month, year, hour, minute, second = date_check()
            date = f"{day}.{month}.{year}., {hour}:{minute}:{second}"
            account_traffic[account_number][f"Uplata: {date}"] = f"+{payment}"
            break
        
    start_screen()
    print(f"Broj računa: {k}")
    print(f"Datum i vrijeme: {datetime.now()}\n")
    print("Stanje Vašeg računa nakon provedene transakcije: {} {}".format(v["Balance"], currency))
    input("Pritisnite bilo koju tipku za nastavak: ")

# TODO završiti ostatak
def podizanje_novca():
    """Funkcija za podizanje novca s računa"""
    start_screen()
    print("{:^100}".format("PODIZANJE NOVCA S RAČUN\n"))
    account_number = user_check()

    for k, v in accounts.items():
            if k == account_number:
                balance = v["Balance"]
                os.system("cls")
                print("*" * 100)
                print("{:^100}".format("PyBank Algebra\n"))
                print("{:^100}".format("PODIZANJE NOVCA s RAČUN\n"))
                print(f"Broj računa: {k}")
                print(f"Datum i vrijeme: {datetime.now()}\n")
                print(f"Stanje računa: {balance} {currency}")
                while True:
                    payment = float(input("Upišite iznos koji želite podići sa svog računa: "))
                    if payment > v["Balance"]:
                        print("Nedovoljan iznos sredstava na računu. Molimo Vas pokušajte ponovo.")
                    else:
                        break
                v["Balance"] -= payment
                day, month, year, hour, minute, second = date_check()
                date = f"{day}.{month}.{year}., {hour}:{minute}:{second}"
                account_traffic[account_number][f"Isplata: {date}"] = f"-{payment}"
                break
            
    start_screen()
    print(f"Broj računa: {k}")
    print(f"Datum i vrijeme: {datetime.now()}\n")
    print("Stanje Vašeg računa nakon provedene transakcije: {} {}".format(v["Balance"], currency))
    input("Pritisnite bilo koju tipku za nastavak: ")


# izbornik
def main_menu():
    """Funkcija za pokretanje glavnog izbornika banke"""
    
    os.system("cls")

    while True:
        start_screen()
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
            start_screen()
            print("{:^100}".format("GLAVNI IZBORNIK\n"))
            print("{:^100}".format("Hvala što ste koristili usluge naše banke!\n"))
            break
        else:
            print("Pogrešan unos. Molimo vas pokušajte ponovo.")

def start_screen():
    os.system("cls")
    print("*" * 100)
    print("{:^100}".format("PyBank Algebra\n"))
        
def user_check():
    while True:
        account_number = input("Upišite broj Vašeg računa: ")
        if account_number in accounts:
            account_data = accounts[account_number]
            break
        else:
            print("Pogrešan unos. Pokušajte ponovo.")
    
    while True:
        oib = input("Upišite OIB Vaše tvrtke: ")
        if oib in account_data["OIB"]:
            break
        else:
            print("Pogrešan unos. Pokušajte ponovo.")
    
    return account_number

def date_check():
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second

    return day, month, year, hour, minute, second

main_menu()