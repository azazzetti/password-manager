from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ----------------------------    SEARCH DATA     ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            info = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")
    else:
        if website in info:
            messagebox.showinfo(title=f"{website}", message=f"Email/Username: {info[website]['email']}\n\nPassword: {info[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No records found for that website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = 5
    nr_symbols = 5
    nr_numbers = 5

    random_letters = [random.choice(letters) for letter in range(nr_letters)]
    random_numbers = [random.choice(numbers) for number in range(nr_numbers)]
    random_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]

    characters = random_letters + random_symbols + random_numbers
    random.shuffle(characters)
    password = "".join(characters)
    pyperclip.copy(password)
    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="You are not supposed to leave empty spaces")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"You entered this information:\nWebsite:{website}\nEmail/Username:{email}\nPassword:{password}")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # reading data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            messagebox.showinfo(title="Done!", message="Your information has been saved")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# -------------- CANVAS -------------- #
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# -------------- LABELS -------------- #
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# -------------- INPUT -------------- #

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=54)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "zazzettiagustin@gmail.com")

pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3)

# -------------- BUTTONS -------------- #

generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_pass, width=15)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=47, highlightthickness=0, command=add)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", highlightthickness=0, command=search, width=15)
search_button.grid(column=2, row=1)

window.mainloop()
