import datetime

# def pozdrav(ime):
#     """
#     Funkcija koja na konolu ispisuje pozdravnu poruku osobi čije ime je proslijeđeno u funkciju kao parametar
#     """
#     print(f"Dobar dan, {ime}. Kako ste danas?")

# # pozdrav("Nikola")
# # pozdrav(input("Upiši ime: "))
# uneseno_ime = input("Upiši ime: ")
# pozdrav(uneseno_ime)

# print(pozdrav.__doc__)



# def pozdrav(ime):
#     """
#     Funkcija koja ovisno o dobu dana vrati pozivatelju pozdravnu poruku
#     za osobu čije ime smo poslali
#     """
#     if datetime.datetime.now().hour < 12:
#         print(f"Dobro jutro, {ime}. Danas je novi dan.")
#     elif datetime.datetime.now().hour >= 12 and datetime.datetime.now().hour < 19:
#         print(f"Dobar dan, {ime}. Dobro vam ide, nastavite tako.")
#     else:
#         print(f"Dobra veče, {ime}. Današnji dan je bio uspješan.")

# # print(datetime.datetime.now())
# # print(datetime.datetime.now().hour)
# pozdrav("Petar")

def pozdrav(ime):
    """
    Funkcija koja ovisno o dobu dana vrati pozivatelju pozdravnu poruku
    za osobu čije ime smo poslali
    """
    if datetime.datetime.now().hour < 12:
        return f"Dobro jutro, {ime}. Danas je novi dan."
    elif datetime.datetime.now().hour >= 12 and datetime.datetime.now().hour < 19:
        return f"Dobar dan, {ime}. Dobro vam ide, nastavite tako."
    else:
        return f"Dobra veče, {ime}. Današnji dan je bio uspješan."

# print(datetime.datetime.now())
# print(datetime.datetime.now().hour)
pozdrav_imenu = pozdrav("Petar")
print(pozdrav_imenu)