# brojevi = [1, 2, 3, 4, 5]

# brojevi.clear()
# novi_brojevi = brojevi.copy()


# print(novi_brojevi)


# Debugging
brojevi = []
for broj in range(0, 21):
    brojevi.append(broj)

brojevi.append(15)
print(brojevi)

print()

# brojevi.clear()

brojevi_kopija = brojevi.copy()

# count
brojevi_count = brojevi.count(15)
# print(f"Broj pojavljivanja broja 15 je: {brojevi_count}")

#extend
# rijeci = ["Python", "Algebra", "Programiranje"]

# brojevi.extend(rijeci)
# print(brojevi)
# print(rijeci)

#indeks
# index_elementa = brojevi.index("Python")
# print(index_elementa)

#insert
# brojevi.insert(1, "Ovo")
# print(brojevi)

#sort
# brojevi.sort()
# print(brojevi)

#reverse
brojevi.reverse()
print(brojevi)