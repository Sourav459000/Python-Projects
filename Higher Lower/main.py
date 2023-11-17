from game_data import data
from logo import hl, vs
import random
from replit import clear

want_to_continue = 'y'
score = 0


def game(score):
    a = data[random.randint(0, 49)]
    b = data[random.randint(0, 49)]
    while b == a:
        b = data[random.randint(0, 49)]
    print(hl)
    print(f"Your current score: {score}.")
    print(f"Compare A: {a['name']}, {a['description']}, {a['country']}. ")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, {b['country']}. ")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess == 'A':
        if a['follower_count'] > b['follower_count']:
            score += 1
            print(f"Got it right. Score = {score} ")
            game(score)
        else:
            print(f"Sorry that's wrong. Final score = {score} ")
    elif guess == 'B':
        if b['follower_count'] > a['follower_count']:
            score += 1
            print(f"Got it right. Score = {score} ")
            game(score)
        else:
            print(f"Sorry that's wrong. Final score = {score} ")

while want_to_continue == 'y':
    game(score)
    want_to_continue = input("Type 'y' to play again or type 'n'.").lower()
    if want_to_continue == 'n':
        print("Goodbye!")
    elif want_to_continue == 'y':
        clear()
