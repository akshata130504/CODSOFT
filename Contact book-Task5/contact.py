import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Initialize contacts
contacts = load_contacts()

# Function to add a contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name and phone:
        contact_id = max([contact["id"] for contact in contacts], default=0) + 1  
        contacts.append({"id": contact_id, "name": name, "phone": phone, "email": email, "address": address})
        save_contacts()
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Warning", "Name and Phone are required!")

# Function to update the contact list display
def update_contact_list():
    contact_list.delete(*contact_list.get_children())  # Clear list
    for contact in contacts:
        contact_list.insert("", "end", values=(contact["id"], contact["name"], contact["phone"], contact["email"], contact["address"]))

# Function to search contacts (highlights matches)
def search_contact():
    query = search_entry.get().strip().lower()

    for item in contact_list.get_children():
        contact_list.item(item, tags=())  # Reset tags

    if query:
        for item in contact_list.get_children():
            values = contact_list.item(item, "values")
            name, phone, email, address = values[1].lower(), values[2].lower(), values[3].lower(), values[4].lower()

            if query in name or query in phone or query in email or query in address:
                contact_list.item(item, tags=("highlight",))

        contact_list.tag_configure("highlight", background="lightyellow")  # Highlight matches

# Function to delete a selected contact
def delete_contact():
    selected_item = contact_list.selection()
    if selected_item:
        contact_id = int(contact_list.item(selected_item, "values")[0])

        global contacts
        contacts = [contact for contact in contacts if contact["id"] != contact_id]

        # Reassign IDs
        for index, contact in enumerate(contacts):
            contact["id"] = index + 1  

        save_contacts()
        update_contact_list()
        messagebox.showinfo("Deleted", "Contact deleted successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete!")

# Function to update a selected contact
def update_contact():
    selected_item = contact_list.selection()
    if selected_item:
        contact_id = int(contact_list.item(selected_item, "values")[0])

        for contact in contacts:
            if contact["id"] == contact_id:
                contact["name"] = name_entry.get().strip()
                contact["phone"] = phone_entry.get().strip()
                contact["email"] = email_entry.get().strip()
                contact["address"] = address_entry.get().strip()
                break

        save_contacts()
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Updated", "Contact updated successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a contact to update!")

# Function to load selected contact details into entry fields
def load_selected_contact(event):
    selected_item = contact_list.selection()
    if selected_item:
        contact_id = int(contact_list.item(selected_item, "values")[0])

        for contact in contacts:
            if contact["id"] == contact_id:
                name_entry.delete(0, tk.END)
                name_entry.insert(0, contact["name"])
                phone_entry.delete(0, tk.END)
                phone_entry.insert(0, contact["phone"])
                email_entry.delete(0, tk.END)
                email_entry.insert(0, contact["email"])
                address_entry.delete(0, tk.END)
                address_entry.insert(0, contact["address"])
                break

# Function to clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("700x500")  # Adjusted for better UI
root.configure(bg="#f0f0f0")

# Labels & Entry Fields
tk.Label(root, text="Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="w")
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5, sticky="w")
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Add", font=("Arial", 12), command=add_contact, width=10, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update", font=("Arial", 12), command=update_contact, width=10, bg="#FFC107", fg="black").grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete", font=("Arial", 12), command=delete_contact, width=10, bg="#F44336", fg="white").grid(row=0, column=2, padx=5)

# Search Field
tk.Label(root, text="Search:", font=("Arial", 12), bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=5, sticky="w")
search_entry = tk.Entry(root, width=30)
search_entry.grid(row=5, column=1, padx=10, pady=5)
tk.Button(root, text="Search", font=("Arial", 12), command=search_contact, bg="#2196F3", fg="white").grid(row=5, column=2, padx=10)

# Contact List (Table)
columns = ("ID", "Name", "Phone", "Email", "Address")
contact_list = ttk.Treeview(root, columns=columns, show="headings", height=10)

for col, width in zip(columns, [40, 150, 100, 150, 200]):
    contact_list.heading(col, text=col)
    contact_list.column(col, width=width)

contact_list.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
contact_list.bind("<<TreeviewSelect>>", load_selected_contact)

# Load existing contacts into the table
update_contact_list()

# Run the application
root.mainloop()
