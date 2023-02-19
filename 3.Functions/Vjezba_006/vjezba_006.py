import random
def rock_paper_scissors_game():
    print("Dobro došli u igru Kamen, škare, papir!")
    print("Igra se u formatu \"Best of 5\".")
    count = 1
    user_count = 0
    comp_count = 0
    while count <= 5:
        user = input("Odaberite kamen, škare ili papir: ")
        comp = random.choice(["kamen", "škare", "papir"])
        user = user.lower()
        while True:
            if user != "kamen" and user != "škare" and user != "papir":
                user = input("Pogrešan unos! Odaberite kamen, škare ili papir: ")
            else:
                break
        if user == "kamen" and comp == "škare":
            print(f"Korisnik je odabrao: {user.capitalize()}")
            print(f"Računalo je odabralo: {comp.capitalize()}")
            print(f"Kamen pobjeđuje škare.")
            user_count += 1
            print(f"Trenutni rezultat je: Korisnik({user_count}) - Računalo({comp_count})")
        elif user == "škare" and comp == "kamen":
            print(f"Korisnik je odabrao: {user.capitalize()}")
            print(f"Računalo je odabralo: {comp.capitalize()}")
            print(f"Kamen pobjeđuje škare.")
            comp_count += 1
            print(f"Trenutni rezultat je: Korisnik({user_count}) - Računalo({comp_count})")
        elif user == "kamen" and comp == "papir":
            print(f"Korisnik je odabrao: {user.capitalize()}")
            print(f"Računalo je odabralo: {comp.capitalize()}")
            print(f"Papir pobjeđuje kamen.")
            comp_count += 1
            print(f"Trenutni rezultat je: Korisnik({user_count}) - Računalo({comp_count})")
        elif user == "papir" and comp == "kamen":
            print(f"Korisnik je odabrao: {user.capitalize()}")
            print(f"Računalo je odabralo: {comp.capitalize()}")
            print(f"Papir pobjeđuje kamen.")
            user_count += 1
            print(f"Trenutni rezultat je: Korisnik({user_count}) - Računalo({comp_count})")
        elif user == "papir" and comp == "škare":
            print(f"Korisnik je odabrao: {user.capitalize()}")
            print(f"Računalo je odabralo: {comp.capitalize()}")
            print(f"Škare pobjeđuju papir.")
            comp_count += 1
            print(f"Trenutni rezultat je: Korisnik({user_count}) - Računalo({comp_count})")
        elif user == "škare" and comp == "papir":
            print(f"Korisnik je odabrao: {user.capitalize()}")
            print(f"Računalo je odabralo: {comp.capitalize()}")
            print(f"Škare pobjeđuju papir.")
            user_count += 1
            print(f"Trenutni rezultat je: Korisnik({user_count}) - Računalo({comp_count})")
        elif user == comp:
            print(f"Korisnik je odabrao: {user.capitalize()}")
            print(f"Računalo je odabralo: {comp.capitalize()}")
            print(f"Nerješeno. Igraj ponovo!")
            print(f"Trenutni rezultat je: Korisnik({user_count}) - Računalo({comp_count})")
            continue
        count += 1
    print()
    print(f"Konačni rezultat je: Korisnik({user_count}) - Računalo({comp_count})")
    if user_count > comp_count:
        print("Pobjednik je korisnik.")
    elif user_count < comp_count:
        print("Pobjednik je računalo.")
    pass

rock_paper_scissors_game()
