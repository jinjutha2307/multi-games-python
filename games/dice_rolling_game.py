import random


def start():
    print("Welcome to the Dice Rolling Game!")
    print("You can roll multiple dice and track how many times you've rolled them.")
    count = 0
    while True:

        try:
            choice = input("Roll the dice? (y/n):")
            if choice.lower() == "y":
                number_of_dice = int(input("How many dice do wanna roll?: "))
                count += 1
                result = ""
                for i in range(number_of_dice):
                    dice = random.randint(1, 6)
                    result += f"{dice}" + ("," if i < number_of_dice - 1 else "")

                print(result)

            elif choice.lower() == "n":
                print(f"Thank you!!. You have rolled the dice {count} times!!")
                break
            else:
                raise ValueError

        except ValueError:
            print("invalid input")
