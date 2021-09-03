"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))
# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

print('I am thinking of a number between 1 and 99')    # given a hint of what range to guess from

secret_number = random.randint(1,99)    # generating a random number and stored as a secret number

while True:
    guess = int(input('guess a number: ')) # taking an input from the user

    if guess == secret_number:    # comparing if user input is the same as the secret number
        print('congrats! The number was: ', secret_number)    #output for success
        break      # a break point if user guessed right
    elif guess > secret_number:
        print('Try again your guess is too high')   # a message to notify the user if the user guessed too high

    else:
        print('Try again your guess is too low')    # a message to notify the user if the user guessed too low








