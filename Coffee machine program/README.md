# Coffee Machine Simulator

This Python script simulates a coffee machine that offers three types of drinks: espresso, latte, and cappuccino. Users can choose their preferred drink, check the current resource status, and turn off the coffee machine when done. The script tracks the available resources (water, milk, coffee) and calculates the profit based on the drinks sold.

## How to Use:

1. Run the script.
2. The coffee machine logo (`coffee`) will be displayed.
3. Enter the drink choice when prompted: espresso, latte, cappuccino, or type "off" to exit.
4. To check the current resource status, type "report".
5. Follow the prompts to insert coins and complete the transaction.
6. The script will notify you if the drink is ready, and the change will be provided if applicable.
7. Continue making drinks or type "off" to exit the simulation.

## Code Overview:

### Functions:

1. **`is_resource_sufficient(order_ingredients)` Function:**
   - Checks if there are enough resources to make the specified drink.
   - Prints a message if any ingredient is insufficient.

2. **`process_coins()` Function:**
   - Prompts the user to insert coins and calculates the total value of the coins inserted.

3. **`is_transaction_successful(money_received, drink_cost)` Function:**
   - Checks if the payment is sufficient for the selected drink.
   - Calculates and provides change if applicable.
   - Updates the profit based on the successful transaction.

4. **`make_coffee(drink_name, order_ingredients)` Function:**
   - Deducts the required ingredients from the available resources.
   - Prints a message indicating the successful preparation of the drink.

### Main Program:

- The script initializes the coffee machine by printing the logo and setting up the menu and initial resources.

- The main program runs in a loop (`while is_on`):
  - User is prompted to choose a drink or type "off" to exit.
  - Typing "report" displays the current resource status and profit.
  - Based on the user's choice, the resources are checked, and the transaction is processed.

- The menu and resources are defined at the end of the script.

## MIT License

Copyright (c) 2022 Sourav Toshniwal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
