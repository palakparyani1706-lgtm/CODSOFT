import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password

def create_password():
    try:
        length = int(length_entry.get())

        password = generate_password(
            length,
            upper_var.get(),
            digits_var.get(),
            symbols_var.get()
        )

        if password is None:
            messagebox.showerror("Error", "Invalid input or no options selected!")
        else:
            result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

def copy_password():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Window setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x350")
root.resizable(False, False)

# Title
tk.Label(root, text="Password Generator", font=("Arial", 14, "bold")).pack(pady=10)

# Length input
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root, justify="center")
length_entry.pack(pady=5)

# Options (default selected)
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack(anchor="w", padx=80)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(anchor="w", padx=80)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor="w", padx=80)

# Buttons
tk.Button(root, text="Generate Password", command=create_password).pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=5)

# Output
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30, justify="center", font=("Arial", 10)).pack(pady=10)

# Run app
root.mainloop()
