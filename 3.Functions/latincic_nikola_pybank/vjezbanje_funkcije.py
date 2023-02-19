



def izbornik():
    print("Odaberi neku opciju")
    opcija = input("Upisi nesto")

    while True:
        if opcija == 1:
            izbornik()
        else:
            print("U elsu sam")