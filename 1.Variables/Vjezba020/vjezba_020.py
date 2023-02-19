stanovnistvo_lista = ["Petar Perić", "Marko Marić", "Ivan Ivic", "Josip Josipović", "Marko Marić"]


stanovnistvo = {
    "54879632105": "Petar Perić",
    "76567281726": "Marko Marić",
    "54875965845": "Ivan Ivić",
    "55847850364": "Josip Josipović",
    "87996302784": "Marko Marić"
}

# print(stanovnistvo_lista[1])

# print(stanovnistvo["76567281726"])

stanovnistvo["85452632157"] = "Hrvoje Horvat"

# print(stanovnistvo)

# for key in stanovnistvo.keys():
#     print(key)

# for value in stanovnistvo.values():
#     print(value)

# for item in stanovnistvo.items():
#     print(item)

# for key, value in stanovnistvo.items():
#     print(key)
#     print(value)
#     print()

stanovnistvo = {
    "123443261": ["Petar", "Peric", 30, "zaposlen"],
    "123443262": ["Marko", "Maric", 32, "zaposlen"],
    "123443263": ["Ivan", "Ivic", 350, "zaposlen"],
    "123443264": ["Josip", "Josipovic", 3, "nezaposlen"],
    "123443265": ["Marko", "Maric", 43, "zaposlen"],
    "123443266": ["Hrvoje", "Horvat", 32, "nezaposlen"],
}


# zelimo ispisati prezime osobe pod identifikatorom 123443265

lista = stanovnistvo["123443265"]
print(lista[1])

print(stanovnistvo["123443265"][1]) 