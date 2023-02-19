

# PISANJE U DATOTEKU
file_writer = open("6.Files/Vjezba_001/ime.txt", "w")

ime = input("Upišite ime i prezime: ")
file_writer.write(ime)

file_writer.close()


# CITANJE IZ DATOTEKE
file_reader = open("6.Files/Vjezba_001/ime.txt", "r")

data_file = file_reader.read()

file_reader.close()

print(f"Sadrzaj datoteke je:\n{data_file}")