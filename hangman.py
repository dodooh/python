import random
import csv
import string

def update_rtstring(keyword,rt_strg='',user_guess =''):
    puzzle = rt_strg
    if user_guess =='':
        puzzle = ('_'*len(keyword))
    else: 
        for i in range(len(keyword)):
            if user_guess == keyword[i]:
                puzzle = puzzle[:i] + keyword[i] + puzzle[i+1:]
    return puzzle

def update_letter_left(rt_string):
    rt_left = 0
    for c in rt_string:
        if c == "_":
            rt_left +=1
    return rt_left

# read file csv
PATH = "D:\Python\\random ex\sowpods.csv"
file = open(PATH, newline='')
reader = csv.reader(file)
# convert every string line into a set with a string for keyword 
# and an integer for keynumber
datasets = []
for line in reader:
    word = line[0]
    num = int(line[1])
    datasets.append([word,num])
# play game
GUESS_TIMES = 10
print("Welcome to HANGMAN ")
user_input = input('Are you ready? (Y/N) ')
while user_input == 'Y':    
    randset = random.choice(datasets)
    keyword = randset[0]
    print(keyword)
    rt_string = update_rtstring(keyword)
    letter_left = len(keyword)
    guessed = ''
    guess_count = GUESS_TIMES
    print(" ".join(rt_string)+f''' {letter_left} letter(s) left
    You have {guess_count} guess(es) left.''')
    while ((letter_left != 0) and (guess_count != 0)):
        user_guess = input('Your guess? ')
        if user_guess in guessed:
            print("You've already guessed this letter! Guess again\n")
            continue
        elif user_guess in keyword:
            guessed +=user_guess
            rt_string = update_rtstring(keyword,rt_string,user_guess)
            letter_left = update_letter_left(rt_string)
            print(" ".join(rt_string)+f''' {letter_left} letter(s) left
            You have {guess_count} guess(es) left.''')
        else:
            guessed +=user_guess
            guess_count -= 1
            print(f"Wrong! You have {guess_count} guess(es) left")
    if (letter_left == 0):
        print("You win! The keyword is "+ keyword)
    if (guess_count == 0):
        print("You lose! The keyword is "+ keyword)
    user_input = input('Continue? (Y/N) ')
        
            
