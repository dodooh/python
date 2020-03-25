# Rock Paper Scissors Game
# Make a rock-paper-scissors game where it is the player vs the computer. 
# The computer’s answer will be randomly generated, while the program will ask the user for their input. 
# This project will better your understanding of while loops and if statements.

import random

while(True):
    bot = random.choice(['rock','paper','scissors'])
    user_input = input('One Two Three ')
    print(bot)
    if (bot == 'Rock'):
        if (user_input == 'rock'): print('Draw')
        if (user_input == 'paper'): print('You win')
        if (user_input == 'scissors'): print('You lose')
    elif (bot == 'paper'):
        if (user_input == 'rock'): print('You lose')
        if (user_input == 'paper'): print('Draw')
        if (user_input == 'scissors'): print('You win')
    elif (bot == 'scissors'):
        if (user_input == 'rock'): print('You win')
        if (user_input == 'paper'): print('You lose')
        if (user_input == 'scissors'): print('Draw')
    continous = input('Continue? (y/n) ')
    if continous == 'y' :
        continue
    else:
        break
        
