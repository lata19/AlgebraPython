# word = input("Upišite riječ: ").lower()
# word2 = word[len(word)::-1]

# if word == word2:
#     print("Upisana riječ je palindrom!")
# else:
#     print("Upisana riječ nije palindrom.")

# Alenovo rješenje
# rijec = input("Upišite riječ za koju mislite da je palindrom: ").lower()

# obrnuta_rijec = rijec[::-1]
# # print(obrnuta_rijec)

# if rijec == obrnuta_rijec:
#     print("Upisana riječ je palindrom!")
# else:
#     print("Upisana riječ nije palindrom.")

# WHILE petlja
while True:
    word = input("Upišite riječ: ").lower()
    word2 = word[::-1]

    if word == word2:
        print("Upisana riječ je palindrom!")
        break
    else:
        print("Upisana riječ nije palindrom. Pokušajte ponovo!")