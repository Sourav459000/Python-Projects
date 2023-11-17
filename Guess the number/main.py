from replit import clear
import random
from logo import a

EASY = 10
HARD = 5


def check_answer(guess, NUMBER, turns):
    if guess > NUMBER:
        print("Too high.")
        return turns-1
    elif guess < NUMBER:
        print("Too low.")
        return turns - 1
    elif guess == NUMBER:
        print("You guessed it right. You won.")


def difficulty():
    choice = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
    if choice == 'easy':
        return EASY
    elif choice == 'hard':
        return HARD


def game():
    NUMBER = random.randint(1, 100)

    turns = difficulty()
    guess = 0
    while guess != NUMBER:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, NUMBER, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The number was {NUMBER}. Better luck next time.")
            return
        elif guess != NUMBER:
            print("Guess again.")



want_to_continue = 'y'

while want_to_continue == 'y':
    print(a)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    game()
    want_to_continue = input("Type 'y' to guess again or type 'n'.").lower()
    if want_to_continue == 'n':
        print("Goodbye!")
    elif want_to_continue == 'y':
        clear()
