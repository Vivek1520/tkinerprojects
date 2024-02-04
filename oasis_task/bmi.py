from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.minsize(width=400, height=650)
window.title("BMI Calculator")

# Title label
title = Label(text="BMI CALCULATOR", font=("Arial", 16, "bold"), fg="blue")
title.grid(column=1, row=0, pady=35)

# Canvas for image
canvas = Canvas(width=400, height=300, highlightthickness=0)
canvas.grid(column=1, row=1)
canvas.configure(background="#FFFFFF")

# Function to calculate BMI
def bmi_cal():
    height = float(height_entry.get()) / 100  # Convert height to meters
    weight = float(weight_entry.get())  # Get weight in kilograms

    bmi = round(weight / (height * height))
    print(bmi)

    if bmi < 18.5:
        message = "Underweight"
    elif 18.5 <= bmi < 25:
        message = "Normal weight"
    elif 25 <= bmi < 30:
        message = "Overweight"
    else:
        message = "Obese"

    answer.config(text=f"Your BMI IS {bmi}\n{message}", font=("Arial", 12, "bold"), fg="red")

# Load the original image
original_image = Image.open("bmi.png")

# Calculate the aspect ratio
aspect_ratio = original_image.width / original_image.height

# Calculate the new width and height to fit within the canvas
canvas_width = 400
canvas_height = int(canvas_width / aspect_ratio)

# Resize the image
resized_image = original_image.resize((canvas_width, canvas_height))

# Create an ImageTk object from the resized image
image = ImageTk.PhotoImage(resized_image)

# Draw the resized image on the canvas
canvas.create_image(0, 0, anchor=NW, image=image)

# Answer label
answer = Label(text="Calculate Your BMI", font=("Arial", 14), fg="green")
answer.grid(column=1, row=2,pady=(20, 0))

# Height entry field
def on_height_entry_click(event):
    if height_entry.get() == "Enter height":
        height_entry.delete(0, END)
        height_entry.configure(fg="black")

def on_height_entry_leave(event):
    if height_entry.get() == "":
        height_entry.insert(0, "Enter height")
        height_entry.configure(fg="gray")

height_entry = Entry(font=("Arial", 12), fg="gray")
height_entry.grid(column=1, row=3, pady=(15, 0))
height_entry.insert(0, "Enter height")
height_entry.bind("<FocusIn>", on_height_entry_click)
height_entry.bind("<FocusOut>", on_height_entry_leave)

# Weight entry field
def on_weight_entry_click(event):
    if weight_entry.get() == "Enter weight":
        weight_entry.delete(0, END)
        weight_entry.configure(fg="black")

def on_weight_entry_leave(event):
    if weight_entry.get() == "":
        weight_entry.insert(0, "Enter weight")
        weight_entry.configure(fg="gray")

weight_entry = Entry(font=("Arial", 12), fg="gray")
weight_entry.grid(column=1, row=4, pady=(15, 0))
weight_entry.insert(0, "Enter weight")
weight_entry.bind("<FocusIn>", on_weight_entry_click)
weight_entry.bind("<FocusOut>", on_weight_entry_leave)

# Calculate button
btn = Button(text="Calculate", command=bmi_cal, font=("Arial", 12, "bold"), fg="white", bg="blue")
btn.grid(column=1, row=5, pady=(20, 0))

window.mainloop()