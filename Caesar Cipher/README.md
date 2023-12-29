# Caesar Cipher Encoder/Decoder

This Python script implements a simple Caesar Cipher encoder/decoder. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. This shift is determined by a key provided by the user.

## How to Use:

1. Run the script.
2. The Caesar Cipher logo (`l`) will be displayed.
3. Choose whether to 'encode' or 'decode' a message.
4. Enter the message you want to encrypt or decrypt.
5. Input the shift number (key) for the cipher.
6. The script will output the encoded or decoded message.
7. You can choose to continue by typing 'yes' or exit by typing 'no'.

## Code Overview:

### Logo:

- The script imports a custom ASCII art logo from the `logo` module and displays it at the beginning.

### Cipher Algorithm:

- The script defines a list of lowercase letters as the alphabet.
- The main functionality is within the `caesor_cipher` function:
  - It takes the plaintext, shift amount, and direction (encode or decode) as parameters.
  - It shifts each letter in the plaintext according to the given shift amount.
  - The result is displayed as the encoded or decoded message.

### Main Program:

- The program uses a `while` loop to allow the user to encode/decode multiple messages consecutively.
- The user is prompted to choose the direction (encode or decode), input the message, and specify the shift number.
- After each encryption or decryption, the user is asked if they want to continue.
- The loop continues until the user decides to exit.

## MIT License

Copyright (c) 2022 Sourav Toshniwal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
