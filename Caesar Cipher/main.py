from logo import l
print(l)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char = 'yes'
while char == 'yes' or char == 'Yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    def caesor_cipher(plain_text, shift_amount, direction1 ):
        cipher_text = ''
        if direction1 == 'decode':
            shift_amount = shift_amount* -1
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += letter
        print(f"The {direction1}d text is {cipher_text}.")

    caesor_cipher(plain_text=text,shift_amount=shift,direction1=direction)

    char = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if char == 'no' or char == 'No':
        print("Goodbye.")