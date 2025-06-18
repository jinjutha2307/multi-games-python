import random


count = 0
randomNumber = random.randint(1, 100)
print(randomNumber)
while True:
    try:
        choice = int(input('Guess the number (between 1 and 100): '))
        count += 1
        if choice < randomNumber:
            print("Too low! Try again")

        elif choice > randomNumber:
            print('Too high!! Try again')
        else:
            print(
                f"Congratulations! You guessed the number in {count} attemps")
            break
    except ValueError:
        print("Please enter valid value")
