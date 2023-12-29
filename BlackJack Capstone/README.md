# Blackjack Game

This Python script represents a simple text-based implementation of the popular card game Blackjack. The game allows the user to play against a computerized dealer.

## How to Play:

1. Run the script, and you'll be prompted to play a game of Blackjack.
2. If you choose to play ('y'), the game will start.
3. You and the computer dealer will each receive two cards from a standard deck of cards.
4. The goal is to have a hand value as close to 21 as possible without going over.

## Code Overview:

### Functions:

1. **`deal_card()` Function:**
   - Returns a random card from the deck.
   - The deck consists of cards with values 2 through 10 and face cards (Jack, Queen, King) with a value of 10.
   - The Ace is considered as 11 by default but can be adjusted to 1 if needed.

2. **`calculate_score(cards)` Function:**
   - Takes a list of cards as input and calculates the total score.
   - Handles the special case of Blackjack (an Ace and a 10-value card as the initial two cards).

3. **`compare(user_score, computer_score)` Function:**
   - Compares the final scores of the user and computer.
   - Determines the winner based on various conditions such as going over 21, having a Blackjack, or having a higher score.

4. **`play_game()` Function:**
   - Initiates a game of Blackjack.
   - Deals initial cards to the player and the computer.
   - Manages the game loop, allowing the player to choose whether to get another card or pass.
   - Computes the final scores and determines the winner.

### Main Game Loop:

1. The game starts by displaying the Blackjack logo (`a`) and initializing the player's and computer's card lists.

2. Two cards are dealt to each player.

3. The player is prompted to decide whether to get another card ('y') or pass ('n').

4. The game continues until the player decides to pass, reaches Blackjack, or goes over 21.

5. The computer then takes its turn, automatically drawing cards until it has a score of at least 17.

6. The final hands and scores are displayed, and the winner is determined using the `compare` function.

7. The player is asked if they want to play another round.

### Dependencies:

- The script uses the `random` module for card shuffling and dealing.
- It also imports a custom ASCII art logo from the `logo` module.

## MIT License

Copyright (c) 2022 Sourav Toshniwal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
