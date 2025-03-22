import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to check password strength
def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 8 and (has_upper or has_lower) and has_digit:
        return "Medium"
    else:
        return "Weak"

# Function to generate a secure password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4!")
            return
        
        # Ensure at least one of each required character type
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        
        # Fill the rest of the password with random characters
        password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=length-4)
        random.shuffle(password)
        password = ''.join(password)
        
        # Display password and strength
        password_var.set(password)
        strength_var.set(f"Strength: {check_strength(password)}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

# Heading Label
tk.Label(root, text="Random Password Generator", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

# Password Length Entry
tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#f0f0f0").pack()
length_entry = tk.Entry(root, width=10, font=("Arial", 12))
length_entry.pack(pady=5)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

# Display Generated Password
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=25, state="readonly", justify="center")
password_entry.pack(pady=5)

# Password Strength Label
strength_var = tk.StringVar()
strength_label = tk.Label(root, textvariable=strength_var, font=("Arial", 12, "bold"), bg="#f0f0f0")
strength_label.pack()

# Copy to Clipboard Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=10)

# Run the GUI
root.mainloop()
