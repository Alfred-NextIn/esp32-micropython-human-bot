import math
import random

#setting lower range
lower = 0
#setting upper range
upper = 99
 
# generating random number between
# the lower and higher defined numbers 

x = random.randint(lower, upper)

#set
correct= False

while not correct:
 
    # taking guessing number as input

    guess = int(input("Guess a number:- "))
 

    # Condition testing

    if x == guess:

        print("Congratulations! Your guess was right")
        found=True
        # Once guessed, loop will break

        break

    elif x > guess:

        print("You guessed too small!")

    elif x < guess:

        print("You Guessed too high!")
 

 



