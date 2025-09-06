import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0")
        return
    
    characters = ""
    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation
    
    if not characters:
        messagebox.showerror("Error", "Please select at least one character set")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---- GUI ----
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Password length
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
length_var = tk.IntVar(value=12)
tk.Entry(root, textvariable=length_var, width=10).pack()

# Options
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor="w", padx=20)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white").pack(pady=10)

# Display generated password
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, width=30, font=("Arial", 12)).pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="green", fg="white").pack(pady=5)

root.mainloop()