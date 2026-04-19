import tkinter as tk
from tkinter import messagebox
import random
import string
import json
import os

FILE = "passwords.json"

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(12))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def save_data():
    site = entry_site.get()
    user = entry_user.get()
    pwd = entry_password.get()

    if not site or not user or not pwd:
        messagebox.showerror("Error", "Fill all fields")
        return

    new_data = {site: {"username": user, "password": pwd}}

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data.update(new_data)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

    messagebox.showinfo("Saved", "Data saved successfully!")

def view_data():
    if not os.path.exists(FILE):
        messagebox.showinfo("Info", "No data found")
        return

    with open(FILE, "r") as f:
        data = json.load(f)

    result = ""
    for site, details in data.items():
        result += f"{site} | {details['username']} | {details['password']}\n"

    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, result)

root = tk.Tk()
root.title("Password Manager")
root.geometry("400x450")
root.configure(bg="#1e1e1e")

tk.Label(root, text="🔐 Password Manager", font=("Arial", 16),
         bg="#1e1e1e", fg="white").pack(pady=10)

entry_site = tk.Entry(root, width=30)
entry_site.pack(pady=5)
entry_site.insert(0, "Website")

entry_user = tk.Entry(root, width=30)
entry_user.pack(pady=5)
entry_user.insert(0, "Username")

entry_password = tk.Entry(root, width=30)
entry_password.pack(pady=5)
entry_password.insert(0, "Password")

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)
tk.Button(root, text="Save", command=save_data).pack(pady=5)
tk.Button(root, text="View Saved", command=view_data).pack(pady=5)

text_box = tk.Text(root, height=10, width=45)
text_box.pack(pady=10)

root.mainloop()