"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
# print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE **********************************************
import random

count = 1  # start counting the number of times you get correct, initial is 1
while True:

    a = random.randint(10, 99)  # getting a random number between 10 and 99 and storing it in a
    b = random.randint(10, 99)  # getting a random number between 10 and 99 and storing it in b

    correct_ans = a + b  # adding the numbers (a and b)

    print(a, "+", b)
    user_ans = int(input("Enter answer: "))  # getting user input

    if user_ans == correct_ans:  # check if user input is the same as the correct_ans calculated by the computer

        if count > 0:  # check if count is greater than 0
            print("Correct: you have", count, "score in a row")
            count = count + 1  # increase the count by 1

            if count == 4:  # if count reaches four, a congratulations is sent and the program stops
                print("Congratulations! You have mastered Addition! ")
                break  # it stops the program



    else:  # if the user get a wrong answer, the count resets to te original
        print("Wrong: You had it wrong")
        count = count - (count - 1)
