from FileManager import FileManager

class Customers:
    def __init__(self, first_name, last_name, adress, oib, email):
        self.first_name = first_name
        self.last_name = last_name
        self.adress = adress
        self.oib = oib
        self.email = email

    def convert_to_string(self, i):
        return f"{i}. Ime i prezime korisnika: {self.first_name} {self.last_name}\tAdresa korisnika: {self.adress}\tOIB korisnika: {self.oib}\tE-adresa korisnika: {self.email}"

    def change_first_name(self, new_first_name):
        self.first_name = new_first_name

    def change_last_name(self, new_last_name):
        self.last_name = new_last_name
    
    def change_adress(self, new_adress):
        self.adress = new_adress

    def change_email(self, new_email):
        self.email = new_email

customers = {}

def create_customer(first_name, last_name, adress, oib, email):
    customer = Customers(first_name, last_name, adress, oib, email)
    customers[oib] = customer

def append_all_customers_to_file(file_path):
    i = 1
    file_writer = FileManager.openFilePathForAppending(file_path)
    for customer in customers.values():
        line = customer.convert_to_string(i)
        FileManager.writeLineWithFileWriter(file_writer, line)
        i += 1
    
    FileManager.closeFileConnection(file_writer)