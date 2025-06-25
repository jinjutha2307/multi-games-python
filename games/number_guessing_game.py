import random


def start():
    count = 0
    random_number = random.randint(1, 100)
    print(random_number)
    while True:
        try:
            choice = int(input("Guess the number (between 1 and 100): "))
            count += 1
            if choice < random_number:
                print("Too low! Try again")

            elif choice > random_number:
                print("Too high!! Try again")
            else:
                print(f"Congratulations! You guessed the number in {count} attemps")
                break
        except ValueError:
            print("Please enter valid value")
