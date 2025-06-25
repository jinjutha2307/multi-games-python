from games import (
    dice_rolling_game,
    number_guessing_game,
    rock_paper_scissors,
)
from games.quiz_game import quiz_game

CHOICES = [
    "Exit",
    "Quiz Game",
    "Dice Roller",
    "Rock Paper Scissors",
    "Number Guessing Game",
    "Convert Currency",
    "Generate QR code",
]


def main():
    print("Welcome to the Game Hub!\nHere are the available games and services:")
    while True:
        for i, CHOICES in enumerate(CHOICES, start=1):
            print(f"{i}. {CHOICES[i]} or 0 to exit")

        choice = input("Enter the number of your choice: ")
        match choice:
            case "5":
                print("Thank you for playing! Goodbye!")
                return
            case "1":
                quiz_game.start()
            case "2":
                dice_rolling_game.start()
            case "3":
                rock_paper_scissors.start()
            case "4":
                number_guessing_game.start()

            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
