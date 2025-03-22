import tkinter as tk
from tkinter import messagebox

def calculate_result(operation, symbol):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if symbol == "/" and num2 == 0:
            result_label.config(text="Error: Division by zero")
            return
        
        result = operation(num1, num2)
        result_label.config(text=f"Result: {num1} {symbol} {num2} = {result}")
        history_listbox.insert(tk.END, f"{num1} {symbol} {num2} = {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")
    history_listbox.delete(0, tk.END)

def add(): calculate_result(lambda a, b: a + b, "+")
def subtract(): calculate_result(lambda a, b: a - b, "-")
def multiply(): calculate_result(lambda a, b: a * b, "*")
def divide(): calculate_result(lambda a, b: a / b, "/")

# Initialize GUI
root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("350x500")
root.configure(bg="#f0f0f0")

# Input Fields
entry1 = tk.Entry(root, width=10, font=("Arial", 14))
entry1.pack(pady=10)
entry2 = tk.Entry(root, width=10, font=("Arial", 14))
entry2.pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="+", width=5, height=2, command=add, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="-", width=5, height=2, command=subtract, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="*", width=5, height=2, command=multiply, bg="#FF9800", fg="white").grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="/", width=5, height=2, command=divide, bg="#F44336", fg="white").grid(row=1, column=1, padx=5, pady=5)

# Result Label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14), bg="#f0f0f0")
result_label.pack(pady=10)

# Calculation History
tk.Label(root, text="Calculation History", font=("Arial", 12, "bold"), bg="#f0f0f0").pack()
history_listbox = tk.Listbox(root, width=30, height=5)
history_listbox.pack(pady=5)

# Clear Button
tk.Button(root, text="Clear", command=clear, bg="#666", fg="white", width=10).pack(pady=10)

# Run GUI
root.mainloop()
