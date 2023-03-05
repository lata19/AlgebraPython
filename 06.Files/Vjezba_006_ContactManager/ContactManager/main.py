import os
from OrganizationManager import OrganizationManager
from EmployeesManager import EmployeesManager
from CustomersManager import CustomerManager


file_path = "organizacije.txt"

# Upis organizacije
print("*********Stvorite novu organizaciju*********")
name = input("Upisite ime organizacije: ")
adress = input("Upisite adresu organizacije: ")
oib = input("Upisite OIB organizacije: ")

OrganizationManager.create_organization(name, adress, oib)
OrganizationManager.write_all_organization_to_file(file_path)

# Upis zaposlenika
while True:
    os.system("cls")
    print("*********Upis zaposlenika organizacije**********")
    first_name = input("Upišite ime zaposlenika: ")
    last_name = input("Upišite prezime zaposlenika: ")
    oib = input("Upisite OIB zaposlenika: ")
    position = input("Upišite radno mjesto zaposlenika: ")
    EmployeesManager.create_employee(first_name, last_name, oib, position)

    if input("Želite li dodati još jednog zaposlenika? (da/ne) - ").lower() != "da":
        break

EmployeesManager.append_all_employees_to_file(file_path)

# Upis korisnika
while True:
    os.system("cls")
    print("*********Upis korisnika organizacije*********")
    first_name = input("Upišite ime korisnika: ")
    last_name = input("Upišite prezime korisnika: ")
    adress = input("Upišite adresu korisnika: ")
    oib = input("Upisite OIB korisnika: ")
    email = input("Upišite E-mail korisnika: ")
    CustomerManager.create_customer(first_name, last_name, adress, oib, email)

    if input("Želite li dodati još jednog korisnika? (da/ne) - ").lower() != "da":
        break

CustomerManager.append_all_customers_to_file(file_path)