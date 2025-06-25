import json
import os


def start():
    json_path = os.path.join(os.path.dirname(__file__), "data.json")

    with open(json_path, "r") as file:
        data = json.load(file)

    COUNTER = 0

    for item in data:
        print(item["question"])
        for option in item["options"]:
            print(option)
        answer = input("Your answer (a/b/c/d): ").lower()
        if answer == item["answer"]:
            print("Correct!")
            COUNTER += 1
        else:
            print("Wrong!")
    print(f"Your final score is {COUNTER}/{len(data)}")
