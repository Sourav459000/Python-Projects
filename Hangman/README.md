# Hangman Game

This Python script implements a simple console-based Hangman game. The player needs to guess a randomly chosen word by inputting individual letters. The game provides feedback on correct and incorrect guesses and displays the hangman stages to represent the player's remaining lives.

## How to Play:

1. Run the script.
2. The game logo (`logo`) will be displayed.
3. A random word will be selected for the player to guess.
4. The player is represented with underscores for each letter in the word.
5. Guess letters one at a time by inputting them when prompted.
6. Incorrect guesses result in the display of the current hangman stage and a reduction in lives.
7. The game continues until the player correctly guesses the word or runs out of lives.
8. The player is notified of their win or loss, and the correct word is revealed.

## Code Overview:

### Main Program:

- The script starts by selecting a random word from the `list` module and initializing game variables.
- A loop runs until the game ends (`while not end`):
  - The current display of guessed and blank spaces is shown.
  - The player inputs a letter guess.
  - Correct guesses update the display, while incorrect guesses reduce the player's lives.
  - The hangman stage corresponding to the remaining lives is displayed.
  - The game ends when the player wins by correctly guessing the word or loses by running out of lives.

### Modules:

- **`list` Module:**
  - Contains a list of words that the game randomly selects for the player to guess.

- **`stages` Module:**
  - Contains ASCII art representations of the hangman stages for each level of remaining lives.

- **`logo` Module:**
  - Contains ASCII art for the game logo.

## MIT License

Copyright (c) 2022 Sourav Toshniwal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
