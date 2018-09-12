"""
Guessing Game I
Duration: 1 hr

Create a game that allows a single player to guess a secret number. The script should
generate a random number between 0 and 100, take user input and allow the user 10 guesses. The game
should return whether the player has won or lost.

BONUS: Give the player hints when their guess is too high or too low!

Python Learning:
1. Loops
2. Condition
3. import random
4. input()

Concepts:
* Program loops
* Incrementing

Further Reading:
- for loops: https://youtu.be/9LgyKiq_hU0
- while loops: https://youtu.be/D0Nb2Fs3Q8c
- https://pymotw.com/3/random/index.html#module-random
- https://docs.python.org/3/library/random.html
"""
import random

MAX_GUESSES = 3
GUESS_COUNT = 0
SECRET_NUMBER = random.randrange(100)

while GUESS_COUNT <= MAX_GUESSES:
    guess = input('Guess: ')
    if guess == SECRET_NUMBER:
        print("You win!")
        break
    elif guess > SECRET_NUMBER:
        print("Too high!")
    elif guess < SECRET_NUMBER:
        print("Too low!")
    else:
        print("Try again!")
        GUESS_COUNT += 1
