from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)
    passw = "".join(password_list)
    Password.insert(0, passw)
    pyperclip.copy(passw)


def save():
    website = Website_Name.get()
    emailname = Email_Name.get()
    password_ = Password.get()

    if len(website) == 0 or len(emailname) == 0 or len(password_) == 0:
        messagebox.showwarning(title="Error", message="Oops! Data is missing.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail: {emailname}\nPassword: {password_}\nIs it okay to save?")
        if is_ok:
            with open("Passwords.txt", "a") as Password_file:
                Password_file.write(f"{website} | {emailname} | {password_}\n")
                Website_Name.delete(0, END)
                Password.delete(0, END)


window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
bg_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=1, row=0)

Label(window, text="Website:").grid(column=0, row=1)
Label(window, text="Email/Username:").grid(column=0, row=2)
Label(window, text="Password:").grid(column=0, row=3)

Website_Name = Entry(width=55)
Website_Name.grid(sticky=W, column=1, row=1, columnspan=2)
Website_Name.focus()

Email_Name = Entry(width=55)
Email_Name.grid(sticky=W, column=1, row=2, columnspan=2)
Email_Name.insert(0, "sourav280902@gmail.com")

Password = Entry(width=36)
Password.grid(sticky=W, column=1, row=3)

Generate_Password = Button(text="Generate Password", command=password_generator)
Generate_Password.grid(sticky=W, column=2, row=3)

Add_Button = Button(text="Add", width=46, command=save)
Add_Button.grid(sticky=W, column=1, row=4, columnspan=2)

window.mainloop()
