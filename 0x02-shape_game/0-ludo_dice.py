import random

while True:
    command = input("Enter a command ('toss' or 'quit' :")

    if command == "toss":
        dice_number = random.randint(1,6)
        dice2_number = random.randint(1,6)
        print("Dice rolled:", dice_number ,":" , dice2_number)
    elif command == "quit":
        print("Goodbye and thank you for playing")
        break
    else:
        print("Invalid input. Please try again.")
