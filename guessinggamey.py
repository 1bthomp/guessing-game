# A simple number guessing game

#import the random module

import random

# Make n a random number between 1 and 99

n = random.randint(1, 99)

#Ask users to guess the number
guess = int(input("Enter a integer from 1 to 99: "))

while n != "guess":
    if guess < n:
            print("Too low. Please try again")
            guess = int(input("Enter a integer from 1 to 99: "))
    elif guess > n:
        print("Too high. please try again")
        guess = int(input("Enter a integer from 1 to 99: "))
    else:
        print("You guessed it!")
        break
