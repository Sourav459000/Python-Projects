# Password Manager

This Python script utilizes the Tkinter library to create a simple password manager with a graphical user interface (GUI). The application allows users to generate strong passwords, save them along with website and email details, and store the information in a text file.

## How to Use:

1. Run the script.
2. The GUI window will appear, prompting you to enter website details, email/username, and password.
3. Click the "Generate Password" button to automatically generate a strong password.
4. Click the "Add" button to save the entered details.
5. The saved information is stored in a text file named "Passwords.txt."

## Code Overview:

- The script uses Tkinter for creating the GUI components, including entry fields, buttons, and labels.
- Passwords are generated using a combination of letters, numbers, and symbols.
- The `pyperclip` library is used to copy the generated password to the clipboard.
- Entered details are saved in a text file (`Passwords.txt`) when the "Add" button is clicked.
- Error handling is implemented to ensure that no field is left empty.

## MIT License

Copyright (c) 2022 Sourav Toshniwal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
