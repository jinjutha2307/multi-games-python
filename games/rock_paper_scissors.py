import random


def start():
    options = {"r": "🪨", "p": "📃", "s": "✂️"}

    repeat = True
    user_wins = 0
    computer_wins = 0
    while repeat:
        try:
            user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
            computer_choice = random.choice(list(options.keys()))
            if user_choice not in options:
                raise ValueError("Please enter valid value")

            print(f"You choose {options[user_choice]}")
            print(f"Computer choose {options[computer_choice]}")

            if user_choice == computer_choice:
                print("Tie")
            elif (
                (user_choice == "r" and computer_choice == "s")
                or (user_choice == "p" and computer_choice == "r")
                or (user_choice == "s" and computer_choice == "p")
            ):
                print("You win!!")
                user_wins += 1
            else:
                print("You loose")
                computer_wins += 1

            continue_game = True
            while continue_game:
                try:
                    replay = input("Continue? (y/n): ")
                    if replay == "n":
                        repeat = False
                        print(f"User wins {user_wins}, Computer wins {computer_wins}")
                        break
                    elif replay == "y":
                        break
                    else:
                        raise ValueError("Please enter valid value")
                except ValueError as e:
                    print(e)

        except ValueError as e:
            print(e)
