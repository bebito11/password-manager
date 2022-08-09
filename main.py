from cgitb import text
from email import message
import tkinter
from tkinter import messagebox
import random
import json

# ---------------------------------- SEARCH ------------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            #loading data from file
            data = json.load(file)    
    except FileNotFoundError:
        messagebox.showerror(title = "Error", message = "No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password =data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email: {email}\nPassword: {password}")
        else: 
            #If the website entered by the user is not found
            messagebox.showerror(title = "Error", message = f"No details for {website} exists.")
# ---------------------------- RANDOM PASSWORD ------------------------------- #
def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))] 

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():

    new_data = {
        website.get():{
            "email": username.get(),
            "password": password.get()
        }
    }
    if len(password.get()) == 0 or len(website.get()) == 0 or len(username.get()) == 0:
        messagebox.showinfo(title = "Oops", message = "Please fill every entry!") 
    else:
        try:
            with open("data.json", "r") as file:
                #reading old data
                data = json.load(file)
        except FileNotFoundError: 
            with open("data.json","w") as file:
                #writing to created file
                json.dump(new_data, file, indent = 4)
        else:
            #updating old data with new data
            data.update(new_data)
            
            with open("data.json","w") as file:
                #saving updated data
                json.dump(data, file, indent = 4) 
        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
   
    

# ---------------------------- UI SETUP ------------------------------- #
"""Window"""
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row = 0, column = 1)


"""Labels"""
website_label = tkinter.Label(text = "Website:")
website_label.grid(row = 1, column= 0)

username_label = tkinter.Label(text = "Email/Username:")
username_label.grid(row = 2, column = 0)

password_label =tkinter.Label(text = "Password:")
password_label.grid(row = 3, column = 0)


"""Entries"""
website = website_entry = tkinter.Entry(width=21)
website_entry.grid(row = 1, column = 1)
website_entry.focus() # cursor goes directly to that entry

username = username_entry =tkinter.Entry(width = 38)
username_entry.grid(row = 2, column = 1, columnspan = 2)

password = password_entry =tkinter.Entry(width =21)
password_entry.grid(row = 3, column = 1)



"""Buttons"""
password_button = tkinter.Button(text = "Generate Password", command = random_password)
password_button.grid(row = 3, column = 2) 

add_button = tkinter.Button(text = "Add", width = 36, command = save_to_file)
add_button.grid(row = 4, column = 1, columnspan = 2) 

search_button = tkinter.Button(text = "search", width = 13, command = search_password)
search_button.grid(row = 1, column = 2, columnspan=2)
window.mainloop()