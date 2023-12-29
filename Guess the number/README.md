# Number Guessing Game

This Python script implements a simple number guessing game. The player needs to guess a randomly generated number within a specified range. The game includes difficulty levels (easy and hard) that determine the number of attempts allowed.

## How to Play:

1. Run the script.
2. The game logo (`a`) will be displayed.
3. You'll be prompted to choose the difficulty level: 'easy' or 'hard'.
4. The computer will randomly generate a number between 1 and 100.
5. You have a certain number of attempts to guess the correct number based on the chosen difficulty.
6. After each guess, the script will provide feedback on whether the guess is too high, too low, or correct.
7. If you run out of attempts, the game ends, and the correct number is revealed.
8. You can choose to play again by typing 'y' or exit by typing 'n'.

## Code Overview:

### Functions:

1. **`check_answer(guess, NUMBER, turns)` Function:**
   - Compares the user's guess with the randomly generated number.
   - Provides feedback on whether the guess is too high, too low, or correct.
   - Returns the updated number of turns.

2. **`difficulty()` Function:**
   - Prompts the user to choose the difficulty level ('easy' or 'hard').
   - Returns the number of attempts allowed based on the chosen difficulty.

3. **`game()` Function:**
   - Generates a random number.
   - Calls the `difficulty` function to determine the number of attempts.
   - Implements the game loop, where the user makes guesses until they guess correctly or run out of attempts.

### Main Program:

- The main program runs in a loop (`while want_to_continue == 'y'`):
  - Clears the screen and prints the logo and welcome message.
  - Calls the `game` function to play the number guessing game.
  - Prompts the user to play again or exit.

## MIT License

Copyright (c) 2022 Sourav Toshniwal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
