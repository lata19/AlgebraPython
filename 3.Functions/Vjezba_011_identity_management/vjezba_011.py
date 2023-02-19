import os
users = {
    "admin": {
        "firstname": "Admin",
        "lastname": "Admin",
        "password": "administrator123"
        },
    "nikola": {
        "firstname": "Nikola",
        "lastname": "Latinčić",
        "password": "123nikola123"
    }
}


def login_check():
    while True:
        global user
        user = input("Upišite svoje korisničko ime: ")
        password = input("Upišite lozinku: ")
        for k, v in users.items():
            if user == k and password == v["password"]:
                return "Dobro došli,", v["firstname"], v["lastname"]
        
        print("Pogrešni korisničko ime i/ili lozinka. Pokušajte ponovo.")

def admin_action():
    while True:
        action = input("""Odaberite radnju koju želite izvršiti: 
        1 - Dodati novog korisnika (dodaj)
        2 - Ažurirati postojećeg korisnika (ažuriraj)
        3 - Brisati postojećeg korisnika (briši): """)
        if action == "1":
            return adding_new_users()
        elif action == "2":
            return updating_users()
        elif action == "3":
            return deleting_users()
        else:
            print("Pogrešan unos. Molimo Vas probajte ponovo.")

def adding_new_users():
    firstname = input("Upišite ime koji želite dodati: ")
    lastname = input("Upišite prezime koji želite dodati: ")
    username = input("Upišite korisničko ime koji želite dodati: ")

    i = 0
    while i < len(users):
        for user in users:
            if user == username:
                print("Odabrano korisničko ime je već u upotrebi. Probajte ponovo.")
                username = input("Upišite korisničko ime koji želite dodati: ")
                i = -1
        i += 1

    password = input("Upišite željenu lozinku: ")
    while len(password) < 10:
        print("Lozinka je prekratka. Lozinka mora imati minimalno 10 znakova.")
        password = input("Upišite željenu lozinku: ")
    password2 = input("Ponovo upišite željenu lozinku: ")

    while password != password2:
        print("Lozinke se ne poklapaju. Probajte ponovo.")
        password = input("Upišite željenu lozinku: ")
        password2 = input("Ponovo upišite željenu lozinku: ")

    users[username] = {
            "firstname": firstname,
            "lastname": lastname,
            "password": password
        }
    os.system("cls")
    print(f"Popis korisnika u bazi:\n{users}")

def updating_users():
    os.system("cls")
    print(f"Popis korisnika:\n{users}")
    while True:
        username_update = input("Upišite korisničko ime korisnika kojeg želite ažurirati: (Napomena: Pazite na velika i mala slova!) ")
        if username_update in users:
            os.system("cls")
            break
        else:
            print(f"Ne postoji korisnik s korisničkim imenom: {username_update}")
    
    update = input("Što želite ažurirati? (username, ime, prezime, lozinka): ").lower()
    while update != "stop":
        if update == "username":
            users[username_update] = input("Upišite novo korisničko ime:")
            update = input("Želite li još nešto ažurirati? (username, ime, prezime, lozinka)\nZa izlaz iz programa upišite \"stop\": ").lower()
        elif update == "ime":
            users[username_update]["firstname"] = input("Upišite novo ime:")
            update = input("Želite li još nešto ažurirati? (username, ime, prezime, lozinka)\nZa izlaz iz programa upišite \"stop\": ").lower()
        elif update == "prezime":
            users[username_update]["lastname"] = input("Upišite novo prezime:")
            update = input("Želite li još nešto ažurirati? (username, ime, prezime, lozinka)\nZa izlaz iz programa upišite \"stop\": ").lower()
        elif update == "lozinka":
            users[username_update]["password"] = input("Upišite novo prezime:")
            update = input("Želite li još nešto ažurirati? (username, ime, prezime, lozinka)\nZa izlaz iz programa upišite \"stop\": ").lower()
    
    os.system("cls")
    print(users)

def deleting_users():
    os.system("cls")
    print(f"Popis korisnika:\n{users}")
    users.pop(input("Upišite korisničko ime koje želite izbrisati: "), "Username nije pronađeno")

    os.system("cls")
    print(users)

print("Dobrodošli. Molimo Vas da se prijavite")
login = login_check()
print(*login)

if user == "admin":
    admin_action()
