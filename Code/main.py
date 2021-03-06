from textwrap import indent
from tkinter import *
from tkinter import font
from tkinter import messagebox
from turtle import title
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_input.get().lower()
    email = email_input.get().lower()
    password = password_input.get()
    new_data = {
        website:{
            'email': email,
            'password': password,
            }
        }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Empty field', message='There can not be empty fields.')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# SEARCH

def search_data():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            website = website_input.get().lower()
            if website in data:
                messagebox.showinfo(title=website, message=f'Email: {data[website]["email"]}\nPassword: {data[website]["password"]}')
            else:
                messagebox.showinfo(title='Website not found', message='Website not registered')
    except FileNotFoundError:
        messagebox.showinfo(title='Website not found', message='Website not registered')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# LABELS
website_label = Label(text='Website:', font=('arial', 15,))
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:', font=('arial', 15,))
email_label.grid(row=2, column=0)

password_label = Label(text='Password:', font=('arial', 15,))
password_label.grid(row=3, column=0)

# ENTRIES
website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=39)
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# BUTTONS
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)

generate_button = Button(text='Search', command=search_data)
generate_button.grid(row=1, column=2)

add_button = Button(text='Add', width=33, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
