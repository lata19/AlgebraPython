def card_protection(number, sign):
    while True:
        if len(number) == 16:
            break
        elif len(number) == 19 and number[4] == "-" and number[9] == "-" and number[14] == "-":
            break
        else:
            number = input("Neispravan unos!\nUpišite 16-znamenkasti broj kartice: ")
    
    index = 0
    for i in number[:-4]:
        if i == "-":
            pass
        else:
            number[index] = sign
        index += 1
    number = "".join(number)
    return number




card_number = input("Upišite 16-znamenkasti broj kartice: ")
card_number = list(card_number.strip())
protection_sign = input("Upišite znak s kojim želite zaštiti broj kartice: ")

print(card_protection(card_number, protection_sign))



# Alenovo rješenje
# def sakrij_znakove(tekst, znak_za_maskiranje):
#     zasticeni_tekst = ""
#     if len(tekst) < 5:
#         print("Duljina kartice je prekratka")
#     else:
#         limit_zastite = len(tekst) - 4
#         indeks = 0
#         for znak in tekst:
#             if indeks < limit_zastite:
#                 zasticeni_tekst += znak_za_maskiranje
#             else:
#                 zasticeni_tekst += znak
#             indeks += 1
#         return zasticeni_tekst



# kartica = input("Upisite broj kartice: ")
# znak_za_maskiranje = input("Upisite znak za maskiranje brojeva: ")
# tekst = sakrij_znakove(kartica, znak_za_maskiranje)
# print(kartica)
# print(tekst)
