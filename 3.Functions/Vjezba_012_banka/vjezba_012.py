import os
import random

accounts = {}

def otvaranje_racuna():
    os.system("cls")
    firstname = input("Upišite Vaše ime: ").capitalize()
    lastname = input("Upišite Vaše prezime: ").capitalize()
    oib = input("Upišite Vaš OIB: ")
    while len(oib) != 11:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        oib = input("Upišite Vaš OIB: ")
    new_account = []
    while len(new_account) < 16:
        i = random.randint(0, 9)
        new_account.append(str(i))
        if len(new_account) == 16:
            new_account = "".join(new_account)
            if new_account in accounts:
                new_account = []

    accounts[new_account] = {
        "firstname": firstname,
        "lastname": lastname,
        "OIB": oib,
        "Balance": 0.0
    }
    print(accounts)


def prikaz_stanja_racuna():
    os.system("cls")
    firstname = input("Upišite Vaše ime: ").capitalize()
    lastname = input("Upišite Vaše prezime: ").capitalize()
    oib = input("Upišite Vaš OIB: ")
    while len(oib) < 11 and len(oib) > 11:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        oib = input("Upišite Vaš OIB: ")
    account_number = input("Upišite 16-znamenkasti broj računa: ")
    while len(account_number) < 16 and len(account_number) > 16:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        account_number = input("Upišite 16-znamenkasti broj računa: ")
    for k, v in accounts.items():
        if k == account_number:
            print("Stanje Vašeg računa je: {} €".format(v["Balance"]))
            break

def prikaz_prometa_po_racunu():
    os.system("cls")

def polog_novca():
    os.system("cls")
    firstname = input("Upišite Vaše ime: ").capitalize()
    lastname = input("Upišite Vaše prezime: ").capitalize()
    oib = input("Upišite Vaš OIB: ")
    while len(oib) < 11 and len(oib) > 11:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        oib = input("Upišite Vaš OIB: ")
    account_number = input("Upišite 16-znamenkasti broj računa: ")
    while len(account_number) < 16 and len(account_number) > 16:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        account_number = input("Upišite 16-znamenkasti broj računa: ")
    for k, v in accounts.items():
        if k == account_number:
            payment = float(input("Upišite iznos € koji želite uplatiti na svoj račun: "))
            v["Balance"] += payment
            print("Stanje Vašeg računa je: {} €".format(v["Balance"]))
            break


def podizanje_novca():
    os.system("cls")
    firstname = input("Upišite Vaše ime: ").capitalize()
    lastname = input("Upišite Vaše prezime: ").capitalize()
    oib = input("Upišite Vaš OIB: ")
    while len(oib) < 11 and len(oib) > 11:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        oib = input("Upišite Vaš OIB: ")
    account_number = input("Upišite 16-znamenkasti broj računa: ")
    while len(account_number) < 16 and len(account_number) > 16:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        account_number = input("Upišite 16-znamenkasti broj računa: ")
    for k, v in accounts.items():
        if k == account_number:
            payment = float(input("Upišite iznos € koji želite podići sa svog računa: "))
            v["Balance"] -= payment
            print("Stanje Vašeg računa je: {} €".format(v["Balance"]))
            break



# izbornik
def main_menu():
    os.system("cls")

    while True:
        print("Dobrodošli u izbornik banke")
        action = int(input("""Upišite željeni broj:
        1 - Otvaranje računa
        2 - Prikaz stanja računa
        3 - Prikaz prometa po računu
        4 - Polog novca
        5 - Podizanje novca
        0 - Izlaz
        : """))
        if action == 1:
            otvaranje_racuna()
        if action == 2:
            prikaz_stanja_racuna()
        if action == 3:
            prikaz_prometa_po_racunu()
        if action == 4:
            polog_novca()
        if action == 5:
            podizanje_novca()
        if action == 0:
            break

        print("Hvala što ste koristili usluge naše banke!")

main_menu()