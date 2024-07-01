from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = []
    # password_list.extend(password_letter)
    # password_list.extend(password_numbers)
    # password_list.extend(password_symbols)

    password_list = password_numbers + password_symbols + password_letter
    random.shuffle(password_list)

    password = ""
    password = "".join(password_list)
    
    
    password_input.insert(0, password)
    pyperclip.copy(password) 
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any field empty!")
        
    else:

        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details entered:\nEmail: {email_input.get()}\nPassword: {password_input.get()}\nIs it ok to save? ")

        if is_ok:
            with open("./Day29/data.txt", "a") as f:
                f.write(f"\n\n{website_input.get()}\n{email_input.get()} : {password_input.get()}")
                print("added")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #




window = Tk()
window.config(padx=50, pady= 50)
window.title("Password Manager")

logo = PhotoImage(file="./Day29/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image = logo )
canvas.grid(column=1, row= 0)


website_label = Label(text="Website:" )
website_label.grid(column=0, row= 1)

website_input = Entry(width=36)
website_input.grid(column=1,row=1, columnspan= 2)
website_input.focus()

eamil_label = Label(text="Email/Username:" )
eamil_label.grid(column=0, row= 2)

email_input = Entry(width=36 ) 
email_input.grid(column=1,row=2, columnspan= 2)
email_input.insert(0, "codeanjesh@gmail.com")


password_label = Label(text="Password:")
password_label.grid(column=0, row=3,)

password_input = Entry(width= 18)
password_input.grid(column=1, row=3, columnspan=1)

generate_password = Button( text= "Generate Password", command=generate) 
generate_password.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row= 4, columnspan=2)









window.mainloop()
