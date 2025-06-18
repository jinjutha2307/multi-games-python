QUESTIONS = [
    {
        "question": "Question 1: What is the capital of France?\na) Paris\nb) London\nc) Rome",
        "answer": "a",
    },
    {
        "question": "What is the largest planet in our solar system?\na) Earth\nb) Jupiter\nc) Mars",
        "answer": "b",
    },
]

COUNTER = 0

for question in QUESTIONS:
    print(question["question"])
    answer = input("Your answer: ").lower()
    if answer == question["answer"]:
        print("Correct!")
        COUNTER += 1
    else:
        print("Wrong!")
print(f"Your final score is {COUNTER}/{len(QUESTIONS)}")
