# Exercise:
# We are supposed to create a guessing game in which: we will generate
# a random number between a given range and we need the user to guess it,
# if the guess is correct then end the game and if it is incorrect then
# make the user try again.
# We need to do all this guessing via the terminal using a new module named
# sys.
# We also need to make sure our code doesn't break for invalid inputs.

# How to run it?
# To run this game the user needs to:
# Open a terminal and navigate to the directory where
# this file is present and then he/she needs to type:
# python filename.py num1 num2
# where, filename is the name of the file and num1 and num2 are
# the start and end points of the game.

from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))
# print(answer) -> To debug.

count = 0
print("Welcome to the game!")
while True:
    count += 1
    try:
        guess = int(input(f"Guess the number from {sys.argv[1]} to {sys.argv[2]}: "))
        if guess == answer:
            if count == 1:
                print(f"Congrats!, you got it right in {count} attempt.")
            else:
                print(f"Congrats!, you got it right in {count} attempts.")
            break
        if not (int(sys.argv[1]) <= guess <= int(sys.argv[2])):
            print(
                f"The number is from {sys.argv[1]} to {sys.argv[2]}.\nPlease try again."
            )
            continue
        if guess != answer:
            print("Please try again!")
            continue
    except ValueError:
        print("Please enter a valid input.")
        continue
