import random
import string
from tkinter import *


def generate_password():
    password_length = length_entry.get()

    if password_length.isdigit() and int(password_length) > 0:
        password_length = int(password_length)
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for _ in range(password_length))
        password_label.config(text="Generated Password: \n\n" + password)
    else:
        password_label.config(text="Invalid password length")


# Create the Tkinter window
window = Tk()
window.title("Random Password Generator")
window.minsize(width=400, height=600)

# window.columnconfigure(0, weight=1)
# Configure column 0 to expand and fill the available space
window.columnconfigure(1, weight=1)
height_label = Label(text="Random Password Generator", font=("Arial", 16, "bold"), fg="green")
height_label.grid(column=1, row=0, columnspan=3, sticky="ew")


# Password length label and entry field
length_label = Label(window, text="Password Length:",font=("Arial", 13, "bold"))
length_label.grid(column=1, row=1, pady=(20, 0))

length_entry = Entry(window, width=20,font=("Arial", 12), fg="gray")  # Set the width parameter to change the size
length_entry.grid(column=1, row=2, pady=(15, 0))

# Load the image
tm_img = PhotoImage(file="pass.png")

# Display the image using a Label widget
image_label = Label(window, image=tm_img,bg="black")
image_label.grid(column=1, row=3, pady=(20, 0))

# Generate button
generate_button = Button(window, text="Generate Password", command=generate_password,font=("Arial", 12, "bold"),bg="green")
generate_button.grid(column=1, row=4, pady=(20, 0))

# Generated password label
password_label = Label(window, text="Generated Password:",font=("Arial", 13, "bold"),bg="darkgrey")
password_label.grid(column=1, row=5, pady=(20, 0))

# Run the Tkinter event loop
window.mainloop()