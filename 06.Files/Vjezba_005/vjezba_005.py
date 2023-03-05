# try:
#     with open("6.Files/Vjezba_005/adresar2.txt", "r") as file_reader:
#         file_data = file_reader.read()
#         print(file_data)
# except Exception as e:
#     print(f"Dogodila se pogreška {e}")



# try:
#     with open("6.Files/Vjezba_005/adresar2.txt", "r") as file_reader:
#         for row in file_reader:
#             print(row)

# except Exception as e:
#     print(f"Dogodila se pogreška {e}")



# try:
#     with open("6.Files/Vjezba_005/adresar2.txt", "r") as file_reader:
#         for row in file_reader:
#             row_parts = row.rstrip().split(";")
#             print(f"ID: {row_parts[0]}\tIme: {row_parts[1]}\tPrezime: {row_parts[2]}\tBroj telefona: {row_parts[3]}")

# except Exception as e:
#     print(f"Dogodila se pogreška {e}")




class Contact:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def print_contact(self):
        print(f"ID: {self.id}\tIme: {self.first_name}\tPrezime: {self.last_name}\tBroj telefona: {self.phone}")
    
adress_book = {}

try:
    with open("6.Files/Vjezba_005/adresar2.txt", "r") as file_reader:
        for row in file_reader:
            row_parts = row.rstrip().split(";")
            person_info = Contact(row_parts[0], row_parts[1], row_parts[2], row_parts[3])
            adress_book[row_parts[0]] = person_info
            # adress_book[person_info.id] = person_info            

except Exception as e:
    print(f"Dogodila se pogreška {e}")

for key, value in adress_book.items():
    print(key, end="\t")
    value.print_contact()

# print(adress_book)