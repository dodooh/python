import random

a = random.randint(0,20)
while (True):
    user_input = int(input('Guess please: '))
    if (user_input > a):
        print("You're wrong, your answer is too high")
    elif (user_input < a):
        print("You're wrong, your answer is too low")
    else:
        print(f"Bingo! The answer is  {a}")
        break