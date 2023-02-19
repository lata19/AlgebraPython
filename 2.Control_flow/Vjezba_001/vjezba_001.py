brojevi = []

for broj in range(1,31):
    brojevi.append(broj)

djeljivi_1 = []
for broj in brojevi:
    if broj % 3 == 0 or broj % 6 == 0 or broj %9 == 0:
        djeljivi_1.append(broj)

djeljivi_2 = []
for broj in brojevi:
    if broj % 3 == 0 and broj % 6 == 0 and broj %9 == 0:
        djeljivi_2.append(broj)

print(f"Brojevi djeljivi s 3 ili 6 ili 9 su: {djeljivi_1}")

print(f"Brojevi djeljivi s 3 i 6 i 9 su: {djeljivi_2}")