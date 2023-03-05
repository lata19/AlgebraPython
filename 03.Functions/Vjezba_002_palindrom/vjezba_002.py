# def is_palindrom(rijec):
#     """
#     Funkcija koja provjerava je li
#     unesena riječ palindrom
#     """
#     if rijec.lower() == rijec[::-1].lower():
#         return f"Rijec {rijec} je palindrom"
#     else:
#         return f"Rijec {rijec} nije palindrom"

# print(is_palindrom("kayak"))
# print(is_palindrom("ana"))
# print(is_palindrom("bok"))
# print(is_palindrom("Ana"))





# Boolean
def is_palindrom(rijec):
    return rijec.lower() == rijec[::-1].lower()

word = input("Upišite riječ koju želite provjeriti: ")
if is_palindrom(word):
    print("Palindrom je")
else:
    print("Nije palindrom")