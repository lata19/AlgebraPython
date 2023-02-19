import random
random_number = random.randint(1,100)
number_try = 0

while True:
    guess = int(input("Pogodi broj od 1 do 100:\t"))
    number_try += 1
    
    if guess == random_number:
        print("Čestitam to je broj koji sam zamislio.")
        print(f"Za pogoditi ti je trebalo {number_try} pokušaja.")
        print()
        break
    elif guess < random_number:
        print(f"Zamišljeni broj je veći od {guess}")
    elif guess > random_number:
        print(f"Zamišljeni broj je manji od {guess}")
    