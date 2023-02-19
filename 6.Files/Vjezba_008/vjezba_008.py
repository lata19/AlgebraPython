import json

tekst_json = ""

try:
    with open("6.Files/Vjezba_008/user2.json", "r") as file_reader:
        tekst_json = file_reader.read()
except Exception as e:
    print(f"Dogodila se pogreska {e}")

dict_json = json.loads(tekst_json)
print(dict_json)