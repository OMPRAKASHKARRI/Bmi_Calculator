import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.config(bg="lightgrey")

def bmi():
    try:
        Height = float(height.get())
        Weight = float(weight.get())
        if Height == 0:
            label_bmi.config(text="Error")
            label_category.config(text="Height cannot be 0")
            return
        m = Height / 100
        B = round(Weight / m ** 2, 1)
        label_bmi.config(text=str(B))
        if B <= 18.5:
            label_category.config(text="Underweight")
        elif 18.5 < B <= 25:
            label_category.config(text="Normal")
        elif 25 < B <= 30:
            label_category.config(text="Overweight")
        else:
            label_category.config(text="Health is at risk!\nNeed to lose weight")
    except ValueError:
        label_bmi.config(text="Error")
        label_category.config(text="Enter valid numbers")

# Title
tk.Label(root, text="BMI CALCULATOR", font=("arial", 25, "bold"), width=25, bd=5, bg="white").place(x=0, y=0)

# Background box at bottom
tk.Label(root, width=72, height=18, bg="lightcyan").pack(side="bottom")

# Height Label
tk.Label(root, text="Height (cm)", font=("arial", 12, "bold"), bg="lightgrey").place(x=35, y=130)

# Weight Label
tk.Label(root, text="Weight (kg)", font=("arial", 12, "bold"), bg="lightgrey").place(x=255, y=130)

# Entry Fields
height = tk.StringVar()
weight = tk.StringVar()

h_entry = tk.Entry(root, textvariable=height, width=5, font=("arial", 50), bg="white", fg="black", bd=0, justify="center")
h_entry.place(x=35, y=160)

w_entry = tk.Entry(root, textvariable=weight, width=5, font=("arial", 50), bg="white", fg="black", bd=0, justify="center")
w_entry.place(x=255, y=160)

# Sliders
current_height = tk.DoubleVar()
current_weight = tk.DoubleVar()

def update_height(event): height.set(f"{current_height.get():.2f}")
def update_weight(event): weight.set(f"{current_weight.get():.2f}")

style = ttk.Style()
style.configure("TScale", background="white")

slider_h = ttk.Scale(root, from_=0, to=220, orient="horizontal", style="TScale", command=update_height, variable=current_height)
slider_h.place(x=80, y=250)

slider_w = ttk.Scale(root, from_=0, to=200, orient="horizontal", style="TScale", command=update_weight, variable=current_weight)
slider_w.place(x=300, y=250)

# Optional: Person Image (optional image, not critical)
try:
    man_img = Image.open("man.png")
    man_resized = man_img.resize((50, 100))
    man_photo = ImageTk.PhotoImage(man_resized)
    man_label = tk.Label(root, image=man_photo, bg="lightcyan")
    man_label.place(x=70, y=450)
except:
    man_label = tk.Label(root, bg="lightcyan")
    man_label.place(x=70, y=450)

# Report Button
tk.Button(root, text="Generate Report", width=15, height=2, font=("Arial", 10, "bold"), bg="#1f6e68", fg="white", command=bmi).place(x=280, y=340)

# BMI Output Title
tk.Label(root, text="Your BMI:", font=("arial", 14, "bold"), bg="lightcyan", fg="black").place(x=270, y=410)

# BMI Result
label_bmi = tk.Label(root, font=("arial", 30, "bold"), bg="lightcyan", fg="black")
label_bmi.place(x=350, y=440)

# Category Title
tk.Label(root, text="Category:", font=("arial", 10, "bold"), bg="lightcyan", fg="black").place(x=200, y=480)

# Category Result
label_category = tk.Label(root, font=("arial", 10, "bold"), bg="lightcyan", fg="black", width=50)
label_category.place(x=200, y=500)

root.mainloop()
