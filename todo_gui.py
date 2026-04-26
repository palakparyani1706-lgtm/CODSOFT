import tkinter as tk
from tkinter import messagebox
import json

FILE = "tasks.json"
tasks = []

# ---------------- FILE HANDLING ----------------
def load_tasks():
    global tasks
    try:
        with open(FILE, "r") as f:
            tasks = json.load(f)
    except:
        tasks = []

def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f)

# ---------------- FUNCTIONS ----------------
def refresh_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task == "":
        messagebox.showerror("Error", "Please enter a task")
        return
    tasks.append(task)
    save_tasks()
    entry.delete(0, tk.END)
    refresh_list()

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        save_tasks()
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a task first")

def update_task():
    try:
        index = listbox.curselection()[0]
        new_task = entry.get()
        if new_task == "":
            messagebox.showerror("Error", "Enter new task")
            return
        tasks[index] = new_task
        save_tasks()
        entry.delete(0, tk.END)
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a task first")

# ---------------- UI ----------------
root = tk.Tk()
root.title("To-Do List App")
root.geometry("320x420")

tk.Label(root, text="My To-Do List", font=("Arial", 14)).pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

listbox = tk.Listbox(root, width=35)
listbox.pack(pady=10)

tk.Button(root, text="Add Task", width=15, command=add_task).pack(pady=2)
tk.Button(root, text="Delete Task", width=15, command=delete_task).pack(pady=2)
tk.Button(root, text="Update Task", width=15, command=update_task).pack(pady=2)

# ---------------- START ----------------
load_tasks()
refresh_list()

root.mainloop()