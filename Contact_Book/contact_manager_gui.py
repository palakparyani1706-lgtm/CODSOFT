import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"

# ---------------- FILE HANDLING ----------------
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()

# ---------------- FUNCTIONS ----------------
def add_contact():
    if name_entry.get() == "" or phone_entry.get() == "":
        messagebox.showerror("Error", "Name and Phone required")
        return

    contact = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }

    contacts.append(contact)
    save_contacts()
    view_contacts()
    clear_fields()
    messagebox.showinfo("Success", "Contact Added")


def view_contacts():
    listbox.delete(0, tk.END)
    for c in contacts:
        listbox.insert(tk.END, f"{c['name']} - {c['phone']}")


def search_contact():
    search = name_entry.get().lower()
    listbox.delete(0, tk.END)

    for c in contacts:
        if search in c['name'].lower() or search in c['phone']:
            listbox.insert(tk.END, f"{c['name']} - {c['phone']}")


def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact")
        return

    index = selected[0]
    del contacts[index]
    save_contacts()
    view_contacts()
    messagebox.showinfo("Deleted", "Contact Deleted")


def update_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact")
        return

    index = selected[0]

    contacts[index] = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }

    save_contacts()
    view_contacts()
    messagebox.showinfo("Updated", "Contact Updated")


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


# 🔥 IMPORTANT: AUTO-FILL WHEN CLICKING CONTACT
def select_contact(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]

        clear_fields()

        name_entry.insert(0, contact["name"])
        phone_entry.insert(0, contact["phone"])
        email_entry.insert(0, contact["email"])
        address_entry.insert(0, contact["address"])


# ---------------- UI ----------------
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x550")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

# Buttons
tk.Button(root, text="Add", width=20, command=add_contact).pack(pady=5)
tk.Button(root, text="Update", width=20, command=update_contact).pack(pady=5)
tk.Button(root, text="Delete", width=20, command=delete_contact).pack(pady=5)
tk.Button(root, text="Search", width=20, command=search_contact).pack(pady=5)
tk.Button(root, text="View All", width=20, command=view_contacts).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Bind click event
listbox.bind("<<ListboxSelect>>", select_contact)

view_contacts()

root.mainloop()
