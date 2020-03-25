#Rock Paper Scissors Game
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
        