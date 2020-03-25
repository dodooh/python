# Guess The Number

# Write a programme where the computer randomly generates a number between 0 and 20. 
# The user needs to guess what the number is. If the user guesses wrong, 
# tell them their guess is either too high, or too low. 
# This will get you started with the random library if you haven't already used it.

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
