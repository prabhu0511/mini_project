import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f} ({category})")

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

title = tk.Label(root, text="BMI Calculator", font=("Arial", 16))
title.pack(pady=10)


tk.Label(root, text="Weight (kg)").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (cm)").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()