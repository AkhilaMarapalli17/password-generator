import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate password
def generate_password():
    password = []
    try:
        length = int(length_entry.get())
        if length < 6 or length > 32:
            raise ValueError
        for _ in range(length // 3):
            password.append(random.choice(string.ascii_letters))
            password.append(random.choice(string.punctuation))
            password.append(random.choice(string.digits))
        # Trim in case it's longer than desired
        final_password = ''.join(password[:length])
        password_var.set(final_password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a number between 6 and 32")

# Function to copy password
def copy_to_clipboard():
    generated = password_var.get()
    if generated:
        root.clipboard_clear()
        root.clipboard_append(generated)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# --- GUI Setup ---
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("450x300")
root.configure(bg="#f5f5f5")

title = tk.Label(root, text="🔐 Strong Password Generator", font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#333")
title.pack(pady=10)

# Input for password length
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=10)

length_label = tk.Label(frame, text="Password Length (6–32):", font=("Arial", 12), bg="#f5f5f5")
length_label.grid(row=0, column=0, padx=5)

length_entry = tk.Entry(frame, font=("Arial", 12), width=5, justify='center')
length_entry.insert(0, "12")  # Default length
length_entry.grid(row=0, column=1)

# Generate button
generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white", command=generate_password)
generate_btn.pack(pady=10)

# Password display
password_var = tk.StringVar()
password_display = tk.Entry(root, textvariable=password_var, font=("Consolas", 14), justify="center", bd=2, relief="sunken", width=30, state='readonly')
password_display.pack(pady=10)

# Copy button
copy_btn = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12),
                     bg="#2196F3", fg="white", command=copy_to_clipboard)
copy_btn.pack(pady=5)

# Exit button
exit_btn = tk.Button(root, text="Exit", font=("Arial", 12), bg="#f44336", fg="white", command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()
