# Higher Lower Game

This Python script implements a Higher Lower game, where the player compares the follower counts of two randomly selected Instagram accounts. The player needs to guess which account has more followers.

## How to Play:

1. Run the script.
2. The game logo (`hl`) will be displayed.
3. Two random Instagram accounts with their names, descriptions, and countries are shown.
4. The player is prompted to guess which account has more followers, 'A' or 'B'.
5. The script checks the player's guess and updates the score accordingly.
6. The game continues with new account comparisons until the player decides to stop.
7. The player's final score is displayed.

## Code Overview:

### Main Program:

- The script starts by selecting two random Instagram accounts from the `data` module.
- The game runs in a loop (`while want_to_continue == 'y'`):
  - The current score is displayed.
  - Two accounts are shown, and the player guesses which one has more followers.
  - The player's guess is checked, and the score is updated accordingly.
  - The player decides whether to continue playing or exit.

### Modules:

- **`data` Module:**
  - Contains a list of Instagram account data, including names, descriptions, countries, and follower counts.

- **`hl` Module:**
  - Contains ASCII art for the game logo.

- **`vs` Module:**
  - Contains ASCII art for the "versus" symbol.

## MIT License

Copyright (c) 2022 Sourav Toshniwal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
