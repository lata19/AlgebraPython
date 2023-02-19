import json

user = {
    "id": 1,
    "firstName": "Petar Peric",
    "lastName": "Petar Peric",
    "username": "pperic",
    "email": "pperic@email.adresa",
    "address": {
        "street": "Ilica 256",
        "city": "Zagreb",
        "zipcode": "10000"
    },
    "phone": "+385 1 8031 564",
    "website": "web.adresa",
    "company": {
        "name": "Medvednica d.o.o.",
        "catchPhrase": "Razvoj specijaliziranih Python aplikacija",
        "bs": "Najbolja poslovna rjesenja"
    },
}

# 1. nacin
try:
    with open("6.Files/Vjezba_007_JSON/user.json", "w") as file_writer:
        json.dump(user, file_writer)
except Exception as e:
    print(f"Dogodila se pogreska {e}")


# 2. nacin
try:
    with open("6.Files/Vjezba_007_JSON/user2.json", "w") as file_writer:
        json.dump(user, file_writer, indent=4)
except Exception as e:
    print(f"Dogodila se pogreska {e}")


# 3. nacin
try:
    with open("6.Files/Vjezba_007_JSON/user3.json", "w") as file_writer:
        content = json.dumps(user)
        file_writer.write(content)
except Exception as e:
    print(f"Dogodila se pogreska {e}")


