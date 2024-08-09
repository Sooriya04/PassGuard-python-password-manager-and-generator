import json
from tkinter import *
from tkinter import messagebox
import random

#password generator 
def generate_pass():
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    password = []

    password_letter = [random.choice(letter) for _ in range(8)]
    password_number = [random.choice(number) for _ in range(2)]
    password_symbols = [random.choice(symbols) for _ in range(4)]

    password_list = password_letter + password_number + password_symbols
    password = "".join(password_list)
    password_input.insert(0, password)
#save password
def add_password():
    website = website_input.get()
    email = mail_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password,
        }
    }
    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title = "message", message = "Entry the email and password" )
    else:
        is_ok = messagebox.askquestion(title = "website" , message = f"These are the detail entered\n Email : {email} \n Password : {password} \n Is it ok")
        if is_ok:
            try:
                with open("day 30 files project/password manger/pass.json", "r") as file:
                    data = json.load(file)
                    new_data.update(data)
            except FileNotFoundError:
                with open("day 30 files project/password manger/pass.json", "w") as file:
                    json.dump(new_data, file, indent = 4)
            else:
                new_data.update(data)
                with open("day 30 files project/password manger/pass.json", "w") as file:
                    json.dump(new_data, file, indent = 4)
            finally:
                website_input.delete(0, END)
                mail_input.delete(0, END)
                password_input.delete(0, END)

#search
def find_pass():
    website = website_input.get()
    with open("day 30 files project/password manger/pass.json", "r") as file:
        data = json.load(file)
        if website in data:
            email = data[website]["email"]
            passw = data[website]["password"]
            messagebox.showinfo(title = "Password search", message = f"Email : {email} \n Password : {passw}")
        else:
            messagebox.showinfo(title = "password message", message = "Website is not found")

#UI setup
window = Tk()
window.title("Password Manager")
window.minsize(width = 600, height = 500)
window.config(padx = 30, pady = 30)

website_label = Label(text = "Website : ", font = ("Arial", 18, "normal"))
website_label.config(padx = 30, pady = 30)
website_label.grid(row = 0, column =0)

website_input = Entry(width = 35)
website_input.grid(row = 0, column = 1, columnspan = 2)
website_input.focus()

search_btn = Button(text = "Search", command = find_pass)
search_btn.grid(row = 0, column = 2)

mail_label = Label(text = "Email/username : ", font = ("Arial", 18, "normal"))
mail_label.config(padx = 30, pady = 30)
mail_label.grid(row = 1, column = 0)

mail_input = Entry(width = 35)
mail_input.grid(row = 1, column = 1, columnspan = 2)

password_label = Label(text = "Password  : ", font = ("Arial", 18, "normal"))
password_label.config(padx = 30, pady = 30)
password_label.grid(row = 2, column = 0)


password_input = Entry(width = 31)
password_input.grid(row = 2,column = 1, columnspan = 2)

password_gen = Button(text = "Generate Password",  font = ("Arial", 12, "normal"), command = generate_pass)
password_gen.grid(row = 2, column = 2, columnspan = 3)


add_btn = Button(text = "Add",  font = ("Arial", 12, "normal"), command = add_password, width = 36)
add_btn.grid(row = 3, column = 1)
window.mainloop()