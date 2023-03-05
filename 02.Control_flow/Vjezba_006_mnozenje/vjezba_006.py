input_broj = int(input("Unesite cijeli broj: "))

for i in range(1, input_broj+1):
    for j in range(1, input_broj+1):
        print("{:2d}".format(i * j), end = " ")
    print()