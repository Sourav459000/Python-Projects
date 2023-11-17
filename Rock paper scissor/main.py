import random
from replit import clear
from logo import rock, paper, scissors
game_images = [rock, paper, scissors]

want_to_continue = 'y'

while want_to_continue == 'y':
    def game():
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        if user_choice >= 3 or user_choice < 0:
            print("You typed an invalid number, you lose!")

        else:
            print(game_images[user_choice])

            computer_choice = random.randint(0, 2)
            print("Computer chose:")
            print(game_images[computer_choice])

            if user_choice == 0 and computer_choice == 2:
                print("You win!")
            elif computer_choice == 0 and user_choice == 2:
                print("You lose")
            elif computer_choice > user_choice:
                print("You lose")
            elif user_choice > computer_choice:
                print("You win!")
            elif computer_choice == user_choice:
                print("It's a draw")


    game()
    want_to_continue = input("Type 'y' to play again or type 'n'.").lower()
    if want_to_continue == 'n':
        print("Goodbye!")
    elif want_to_continue == 'y':
        clear()
