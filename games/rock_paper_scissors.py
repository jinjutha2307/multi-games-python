import random


options = {"r": "🪨", "p": "📃", "s": "✂️"}

repeat = True
user_victory_counter = 0
computer_victory_counter = 0


while repeat:
    try:
        userChoose = input("Rock, paper, or scissors? (r/p/s): ").lower()
        computerChoose = random.choice(list(options.keys()))
        if userChoose not in options:
            raise ValueError("Please enter valid value")

        print(f"You choose {options[userChoose]}")
        print(f"Computer choose {options[computerChoose]}")

        if userChoose == computerChoose:
            print("Tie")
        elif (
            (userChoose == "r" and computerChoose == "s")
            or (userChoose == "p" and computerChoose == "r")
            or (userChoose == "s" and computerChoose == "p")
        ):
            print("You win!!")
            user_victory_counter += 1
        else:
            print("You loose")
            computer_victory_counter += 1

        # break the loop when any user wins 2 of 3 times
        # if 2 <= (user_victory_counter or computer_victory_counter) < 3:
        #     print(
        #         f"The winner is {'user' if user_victory_counter > computer_victory_counter else 'computer'}"
        #     )
        #     break

        continue_game = True
        while continue_game:
            try:
                replay = input("Continue? (y/n): ")
                if replay == "n":
                    repeat = False
                    print(
                        f"User wins {user_victory_counter}, Computer wins {computer_victory_counter}"
                    )
                    break
                elif replay == "y":
                    break
                else:
                    raise ValueError("Please enter valid value")
            except ValueError as e:
                print(e)

    except ValueError as e:
        print(e)
