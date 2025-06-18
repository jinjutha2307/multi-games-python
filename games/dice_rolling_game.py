import random

# basic
# while True:
#     choice = input('Roll the dice? (y/n):')
#     if choice.lower() == 'y':
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         print(f'({dice1}, {dice2})')
#     elif choice.lower() == 'n':
#         print('Thank you')
#         break
#     else:
#         print('Invalid choice')


# Enhancement1 : user can specify how many dice they want to roll
# while True:
#     choice = input('Roll the dice? (y/n):')

#     if choice.lower() == 'y':
#         number_of_dice = int(input('How many dice do wanna roll?: '))
#         result = ''
#         for i in range(number_of_dice):
#             dice = random.randint(1, 6)
#             result += f'{dice}' + (',' if i < number_of_dice - 1 else '')

#         print(result)

#     elif choice.lower() == 'n':
#         print('Thank you!!')
#         break

#     else:
#         print('Invalid choice')


# Enhancement2 : track how many time user has rolled the dice
count = 0
while True:
    choice = input("Roll the dice? (y/n):")

    if choice.lower() == "y":
        count += 1
        number_of_dice = int(input("How many dice do wanna roll?: "))
        result = ""
        for i in range(number_of_dice):
            dice = random.randint(1, 6)
            result += f"{dice}" + ("," if i < number_of_dice - 1 else "")

        print(result)

    elif choice.lower() == "n":
        print(f"Thank you!!. You have rolled the dice {count} times!!")
        break
    else:
        print("Invalid choice")
