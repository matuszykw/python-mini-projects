from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    final_password = "".join(password_list)
    password_input.insert(0, final_password)

    pyperclip.copy(final_password)

# ---------------------------- SAVA PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty!")
    else:
        try:
            file = open("password-manager/data.json", "r")
            data = json.load(file)
        except FileNotFoundError:
            file = open("password-manager/data.json", "w")
            json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            file = open("password-manager/data.json", "w")
            json.dump(data, file, indent=4)
        finally:
            file.close()
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    try:
        file = open("password-manager/data.json", "r")
        data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found")
    else:
        website = website_input.get()
        try:
            login_details = data[website]
        except KeyError:
            messagebox.showerror(title="Error", message="Website not found")
        else:
            messagebox.showinfo(title=website, message=f"Email: {login_details['email']} \nPassword: {login_details['password']}")
    finally:
        file.close

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="C:\Python_mini_projects\password-manager\logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Inputs
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "matuszykwiktor21@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#Buttons
password_button = Button(text="Generate Password", width=14, command=generate_password)
password_button.grid(column=2, row=3)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()