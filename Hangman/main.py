import random
from list import list, stages
from logo import logo
print(logo)
chosen_word = random.choice(list)
end = False
lives = len(stages)-1
display = []
for _ in range(len(chosen_word)):
    display += "_"
while not end:
    print(f"{' '.join(display)}")
    guess = input("Guess the letter in the word: ").lower()
    if guess in display:
        print(f"\nYou've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives ==0:
            end = True
            print("\nYou lose.")
            print(f"\nThe word was {chosen_word}")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end = True
        print("\nYou win")
    print(stages[lives])