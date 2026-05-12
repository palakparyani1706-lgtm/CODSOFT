import tkinter as tk
from tkinter import ttk, messagebox
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
        json.dump(tasks, f, indent=4)

# ---------------- FUNCTIONS ----------------
def refresh_list():

    task_list.delete(*task_list.get_children())

    for i, task in enumerate(tasks):

        status = "✅ Done" if task["done"] else "⌛ Pending"

        task_list.insert(
            "",
            "end",
            iid=i,
            values=(
                task["title"],
                status
            )
        )

def add_task():

    title = task_entry.get()

    if title == "":
        messagebox.showerror("Error", "Please enter a task")
        return

    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)

    save_tasks()
    refresh_list()

    task_entry.delete(0, tk.END)

def delete_task():

    selected = task_list.selection()

    if not selected:
        messagebox.showerror("Error", "Select a task first")
        return

    index = int(selected[0])

    tasks.pop(index)

    save_tasks()
    refresh_list()

def update_task():

    selected = task_list.selection()

    if not selected:
        messagebox.showerror("Error", "Select a task first")
        return

    index = int(selected[0])

    new_title = task_entry.get()

    if new_title == "":
        messagebox.showerror("Error", "Enter task")
        return

    tasks[index]["title"] = new_title

    save_tasks()
    refresh_list()

    task_entry.delete(0, tk.END)

def mark_done():

    selected = task_list.selection()

    if not selected:
        messagebox.showerror("Error", "Select a task first")
        return

    index = int(selected[0])

    tasks[index]["done"] = True

    save_tasks()
    refresh_list()

def load_selected_task(event):

    selected = task_list.selection()

    if selected:

        index = int(selected[0])

        task_entry.delete(0, tk.END)
        task_entry.insert(0, tasks[index]["title"])

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()

root.title("Modern To-Do App")
root.geometry("650x450")
root.config(bg="#1f1f2e")

# ---------------- STYLE ----------------
style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview",
    background="#2b2b3c",
    foreground="white",
    fieldbackground="#2b2b3c",
    rowheight=30,
    font=("Arial", 11)
)

style.configure(
    "Treeview.Heading",
    background="#4e73df",
    foreground="white",
    font=("Arial", 11, "bold")
)

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="✨ My To-Do List",
    font=("Arial", 22, "bold"),
    bg="#1f1f2e",
    fg="white"
)

title.pack(pady=20)

# ---------------- INPUT FRAME ----------------
input_frame = tk.Frame(root, bg="#1f1f2e")
input_frame.pack(pady=10)

# Task Entry
task_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Arial", 12),
    bg="#2b2b3c",
    fg="white",
    insertbackground="white",
    relief="flat"
)

task_entry.grid(row=0, column=0, padx=10)

# ---------------- TASK TABLE ----------------
columns = ("Task", "Status")

task_list = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=10
)

for col in columns:
    task_list.heading(col, text=col)

task_list.column("Task", width=400)
task_list.column("Status", width=150)

task_list.pack(pady=20)

task_list.bind("<<TreeviewSelect>>", load_selected_task)

# ---------------- BUTTONS ----------------
button_frame = tk.Frame(root, bg="#1f1f2e")
button_frame.pack(pady=10)

def make_button(text, color, command):

    return tk.Button(
        button_frame,
        text=text,
        bg=color,
        fg="white",
        width=14,
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2",
        command=command
    )

add_btn = make_button("Add Task", "#4CAF50", add_task)
add_btn.grid(row=0, column=0, padx=8)

update_btn = make_button("Update", "#2196F3", update_task)
update_btn.grid(row=0, column=1, padx=8)

delete_btn = make_button("Delete", "#f44336", delete_task)
delete_btn.grid(row=0, column=2, padx=8)

done_btn = make_button("Mark Done", "#9C27B0", mark_done)
done_btn.grid(row=0, column=3, padx=8)

# ---------------- START ----------------
load_tasks()
refresh_list()

root.mainloop()
