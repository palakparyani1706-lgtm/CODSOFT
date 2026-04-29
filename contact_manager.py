import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts()
    print("Contact saved successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact List:")
    for c in contacts:
        print(f"{c['name']} - {c['phone']}")
    print()

def search_contact():
    search = input("Search by name/phone: ")
    for c in contacts:
        if search.lower() in c['name'].lower() or search in c['phone']:
            print(c)
            return
    print("Contact not found.\n")

def update_contact():
    name = input("Enter name to update: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = input("New phone: ")
            c['email'] = input("New email: ")
            c['address'] = input("New address: ")
            save_contacts()
            print("Updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            save_contacts()
            print("Deleted successfully!\n")
            return
    print("Contact not found.\n")

def menu():
    while True:
        print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
        ch = input("Choice: ")

        if ch == '1': add_contact()
        elif ch == '2': view_contacts()
        elif ch == '3': search_contact()
        elif ch == '4': update_contact()
        elif ch == '5': delete_contact()
        elif ch == '6': break
        else: print("Invalid choice")

menu()