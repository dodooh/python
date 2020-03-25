#Password Generator

# Write a programme, which generates a random password for the user. 
# Ask the user how long they want their password to be,
# and how many letters and numbers they want in their password.
# Have a mix of upper and lowercase letters, as well as numbers and symbols. 
# The password should be a minimum of 6 characters long.

import random
import string

# uppercaseChar = random.choice(string.ascii_uppercase)
# lowercaseChar = random.choice(string.ascii_lowercase)
# symbolsChar = random.choice(string.punctuation)
# numberChar = random.choice(string.digits)

def generate_password(letnum, numnum, symnum):
    #generate character folowing order: letter (lowercase/uppercase) -> number -> symbol,
    #then shuffle it randomly and return
    password =[]
    #randomly generate letters (upper/lower)
    for i in range (letnum):
        up_or_lo = random.randint(0,1)
        if up_or_lo == 0:
            password.append(random.choice(string.ascii_uppercase))
        else:
            password.append(random.choice(string.ascii_lowercase))
    #randomly generate numbers
    for i in range (numnum):
        password.append(random.choice(string.digits))
        #randomly generate symbols
    for i in range (symnum):
        password.append(random.choice(string.punctuation))
    #shuffle
    random.shuffle(password)
    result = ''.join(password)
    #return result string
    return result


pass_len = -1
while (pass_len != 0):
    #Any invalid input will restart the program 
    pass_len = int(input('Give the length of the password. Should be >=6 (0 to exit): '))
    if (pass_len < 6):
        continue
    num_of_letters = int(input(f'How many letters do you want? Should be <={pass_len}: '))
    if (num_of_letters > pass_len):
        continue
    num_of_numbers = int(input(f'How many numbers do you want? Should be <={pass_len -num_of_letters}: '))
    if (num_of_numbers > (pass_len -num_of_letters)):
        continue
    num_of_symbols = pass_len - num_of_letters - num_of_numbers
    password = generate_password(num_of_letters,num_of_numbers,num_of_symbols)
    print(password)