# Calculator

This Python script implements a basic calculator that performs addition, subtraction, multiplication, and division operations on two numbers. The calculator utilizes functions for each operation and allows the user to perform consecutive calculations until they choose to exit.

## How to Use:

1. Run the script.
2. The calculator logo (`a`) will be displayed.
3. Enter the first number.
4. Choose the desired operation from the available options: "+", "-", "*", or "/".
5. Enter the second number.
6. The result of the calculation will be displayed.
7. You can choose to continue calculating with the result or start a new calculation.

## Code Overview:

### Functions:

1. **`add(n1, n2)` Function:**
   - Adds two numbers and returns the result.

2. **`sub(n1, n2)` Function:**
   - Subtracts the second number from the first and returns the result.

3. **`mul(n1, n2)` Function:**
   - Multiplies two numbers and returns the result.

4. **`div(n1, n2)` Function:**
   - Divides the first number by the second and returns the result.

### Main Program:

- The script defines a dictionary `operations` that maps arithmetic symbols to their corresponding functions.

- The `calculator` function:
  - Prints the calculator logo.
  - Takes user input for the first number.
  - Displays the available arithmetic operations.
  - Continues to prompt the user for an operation and the second number until they choose to exit.
  - Clears the screen and starts a new calculation if the user decides to continue.

### Dependencies:

- The script uses the `replit` library for clearing the console screen.
- It also imports a custom ASCII art logo from the `logo` module.

## MIT License

Copyright (c) 2022 Sourav Toshniwal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
