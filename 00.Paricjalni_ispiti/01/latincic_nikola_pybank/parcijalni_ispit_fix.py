import datetime as dt
import locale
import os

locale.setlocale(locale.LC_TIME, 'hr_HR')
accounts = {}

# Definiranje klase Račun
class Account:
    def __init__(self, account_number, company_name, adress, zip_code, city, pin, authorized_person, currency, balance, transactions=[]):
        self.account_number = account_number
        self.company_name = company_name
        self.adress = adress
        self.zip_code = zip_code
        self.city = city
        self.pin = pin
        self.authorized_person = authorized_person
        self.currency = currency
        self.balance = balance
        self.transactions = transactions

    def name_change(self, new_company_name):
        """
        Metoda koja mijenja naziv kompanije
        :param new_company_name: Novi naziv kompanije
        :return: Novi naziv komapnije
        """
        self.company_name = new_company_name
        return f"Novi naziv kompanije je {self.company_name}"
    
    def adress_change(self, new_adress):
        self.adress = new_adress
    
    def zip_code_change(self, new_zip_code):
        self.zip_code = new_zip_code
    
    def city_change(self, new_city):
        self.city = new_city

    def authorized_person_change(self, new_authorized_person):
        self.authorized_person = new_authorized_person
    
    def currency_change(self, new_currency):
        self.currency = new_currency
        conversion_rate = float(input("Upišite tečaj konverzije na novu valutu: "))
        self.balance /= conversion_rate

    def balance_inquiry(self):
        start_screen()
        print(f"Broj računa: {self.account_number}")
        print(f"Datum i vrijeme: {date_check().strftime('%A, %d.%m.%Y. %H:%M:%S').capitalize()}\n")
        print(f"Stanje računa: {self.balance} {self.currency}")
        input("Pritisnite bilo koju tipku za nastavak: ")

    def deposit(self):
        os.system("cls")
        print("*" * 100)
        print("{:^100}".format("PyBank Algebra\n"))
        print("{:^100}".format("POLOG NOVCA NA RAČUN\n"))
        print(f"Broj računa: {self.account_number}")
        print(f"Datum i vrijeme: {date_check().strftime('%A, %d.%m.%Y. %H:%M:%S').capitalize()}\n")
        print(f"Stanje računa: {self.balance} {currency}")
        payment = float(input("Upišite iznos koji želite uplatiti na svoj račun: "))
        self.balance += payment
        date = f"{date_check().strftime('%d.%m.%Y. %H:%M:%S')}"
        transaction = Transaction("Uplata", date, payment)
        self.transactions.append(transaction)
        start_screen()
        print(f"Broj računa: {self.account_number}")
        print(f"Datum i vrijeme: {date_check().strftime('%A, %d.%m.%Y. %H:%M:%S').capitalize()}\n")
        print(f"Stanje Vašeg računa nakon provedene transakcije: {self.balance} {self.currency}")
        input("Pritisnite bilo koju tipku za nastavak: ")

    def withdrawal(self):
        os.system("cls")
        print("*" * 100)
        print("{:^100}".format("PyBank Algebra\n"))
        print("{:^100}".format("PODIZANJE NOVCA s RAČUN\n"))
        print(f"Broj računa: {self.account_number}")
        print(f"Datum i vrijeme: {date_check().strftime('%A, %d.%m.%Y. %H:%M:%S').capitalize()}\n")
        print(f"Stanje računa: {self.balance} {self.currency}")
        while True:
            payment = float(input("Upišite iznos koji želite podići sa svog računa: "))
            if payment > self.balance:
                print("Nedovoljan iznos sredstava na računu. Molimo Vas pokušajte ponovo.")
            else:
                break
        self.balance -= payment
        date = f"{date_check().strftime('%d.%m.%Y. %H:%M:%S')}"
        transaction = Transaction("Isplata", date, payment)
        self.transactions.append(transaction)
        start_screen()
        print(f"Broj računa: {self.account_number}")
        print(f"Datum i vrijeme: {date_check().strftime('%A, %d.%m.%Y. %H:%M:%S').capitalize()}\n")
        print(f"Stanje Vašeg računa nakon provedene transakcije: {self.balance} {self.currency}")
        input("Pritisnite bilo koju tipku za nastavak: ")
    
    def ispis(self):
        print(f"""
        Transakcije: {self.transactions}
        """)

class Transaction(Account):
    def __init__(self, transaction_type, date, payment):
        self.transaction_type  = transaction_type
        self.date = date
        self.payment = payment

    def transactions_print(self):
        start_screen()
        print(f"Broj računa: {self.account_number}")
        print(f"Datum i vrijeme: {date_check().strftime('%A, %d.%m.%Y. %H:%M:%S').capitalize()}\n")
        print("Promet po računu:")
        for transaction in self.transactions:
            print(f"{transaction.transaction_type} - {transaction.date}: {transaction.payment} {self.currency}")
        input("Pritisnite bilo koju tipku za nastavak: ")

    def add_transaction(self):
        return f"{self.transaction_type} - {self.date}: {self.payment}"

def account_open():
    """Funkcija koja otvara računa u banci"""

    global currency
    start_screen()
    print("{:^100}".format("KREIRANJE RAČUNA\n"))
    company_name = input("{:<55}".format("Upišite ime Vaše tvrtke: "))
    adress = input("{:<55}".format("Upišite adresu i kućni broj sjedišta vaše tvrtke: "))
    zip_code = input("{:<55}".format("Upišite poštanski broj sjedišta Vaše tvrtke: "))
    city = input("{:<55}".format("Upišite grad u kojem je sjedište Vaše tvrtke: "))
    ap_name = input("{:<55}".format("Upišite ime i prezime ovlaštene osobe: ")) # ap = authorized person
    pin = input("{:<55}".format("Upišite OIB Vaše tvrtke: "))
    while len(pin) != 11 or pin.isnumeric() == False:
        print("Neispravan unos! Molimo Vas probajte ponovo.")
        pin = input("Upišite OIB Vaše tvrtke: ")
    currency = ""
    while currency != "EUR" and currency != "HRK":
        currency = input("Odaberite valutu računa (EUR ili HRK): ").upper()

    input("Pritisnite bilo koju tipku za nastavak: ")

    i = len(accounts) + 1
    account_number = f"BA-{date_check().strftime('%Y-%m')}-{str(i).zfill(5)}"
    balance = 0
    
    account = Account(account_number, company_name, adress, zip_code, city, pin, ap_name, currency, balance)
    accounts[account_number] = account

    start_screen()
    print("Stanje računa\n")
    print(f"Broj računa: {account.account_number}")
    print(f"Trenutno stanje računa: {account.balance} {account.currency}")
    payment = float(input("Upišite iznos koji želite položiti na račun: "))
    account.balance += payment
    date = f"{date_check().strftime('%d.%m.%Y. %H:%M:%S')}"
    transaction = Transaction("Uplata", date, payment)
    account.transactions.append(transaction)

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
            account_open()
        elif action == 2:
            start_screen()
            print("{:^100}".format("PRIKAZ STANJA RAČUNA\n"))
            account_number = user_check()
            accounts[account_number].balance_inquiry()
        elif action == 3:
            start_screen()
            print("{:^100}".format("PRIKAZ PROMETA PO RAČUNU\n"))
            account_number = user_check()
            Transaction.transactions_print(accounts[account_number])
        elif action == 4:
            start_screen()
            print("{:^100}".format("POLOG NOVCA NA RAČUN\n"))
            account_number = user_check()
            accounts[account_number].deposit()
        elif action == 5:
            start_screen()
            print("{:^100}".format("PODIZANJE NOVCA S RAČUN\n"))
            account_number = user_check()
            accounts[account_number].withdrawal()
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
        pin = input("Upišite OIB Vaše tvrtke: ")
        if pin in account_data.pin:
            break
        else:
            print("Pogrešan unos. Pokušajte ponovo.")
    
    return account_number

def date_check():
    return dt.datetime.now()

main_menu()

for a in accounts.values():
    a.ispis()