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

## Example:

```plaintext
 _    _                                         _   
| |  | |                                       | |  
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __ | |_ 
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \| __|
| |  | | (_| | | | | (_| | | | | | | (_| | | | | |_ 
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\__|
                    __/ |                             
                   |___/                              

_ _ _ _ _ _ _ _ _
Guess the letter in the word: e

_ _ _ e _ _ _ _ _ 
Guess the letter in the word: a

_ a _ e _ _ _ _ _ 
Guess the letter in the word: i

I've already guessed i
_ a _ e _ _ _ _ _ 
Guess the letter in the word: s

_ a s e _ _ _ _ _ 
Guess the letter in the word: r

_ a s e _ r _ _ _ 
Guess the letter in the word: t

_ a s e _ r t _ _ 
Guess the letter in the word: w

_ a s e _ r t _ _ 
Guess the letter in the word: l

Lose a life.

_ a s e _ r t _ _ 
Guess the letter in the word: o

_ a s e _ r t o _ 
Guess the letter in the word: p

_ a s e _ r t o p 
You win
```

## License:

This Hangman Game script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```text
MIT License

Copyright (c) [Year] [Your Name]
```
