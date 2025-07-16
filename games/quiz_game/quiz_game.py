import json
import os


COUNTER = 0
MAX_ATTEMPTS = 3


def start():
    global COUNTER

    COUNTER = 0
    attempt = 0

    print("Welcome to the Quiz Game!")
    json_path = os.path.join(os.path.dirname(__file__), "data.json")

    with open(json_path, "r") as file:
        data = json.load(file)

    for item in data:
        attempt = 0
        print(item["question"])
        for option in item["options"]:
            print(option)
        answer = input("Your answer (a/b/c/d): ").strip().lower()

        while answer not in ["a", "b", "c", "d"]:
            attempt += 1

            print("Invalid option. Please choose a valid answer (a/b/c/d).")
            if attempt >= MAX_ATTEMPTS:
                print("Maximum attempts reached. Moving to the next question.")
                break

            answer = input("Your answer (a/b/c/d): ").strip().lower()

        if attempt < MAX_ATTEMPTS:
            if answer == item["answer"]:
                print("Correct!")
                COUNTER += 1
            else:
                print("Wrong!")

    print(f"Your final score is {COUNTER}/{len(data)}")
