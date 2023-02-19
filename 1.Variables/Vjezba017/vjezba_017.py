# Naredba slice

brojevi = []

for broj in range(0, 101):
    brojevi.append(broj)

# print(brojevi)

# Zelimo izdvojiti brojeve od 20 do 40
# range(20,41)
# izdvojeni_brojevi = brojevi[20:41]
# print(izdvojeni_brojevi)

# izdvojiti brojeve od predzadnjeg do kraja

# n = len(brojevi) - 2
# izdvojeni_brojevi = brojevi[n:]
# izdvojeni_brojevi = brojevi[-2:]
# print(izdvojeni_brojevi)

# izdvojiti brojeve od prvog fo predzadnjeg
# izdvojeni_brojevi = brojevi[:-1]
# print(izdvojeni_brojevi)

# Print cijele liste od kraja 
izdvojeni_brojevi = brojevi[100::-1]
print(izdvojeni_brojevi)

