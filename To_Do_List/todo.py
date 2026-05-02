import json
FILE = "tasks.json"


tasks=[]


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

    

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i,task in enumerate(tasks,1):
            print(f"{i}. {task}")

def add_task():
    task=input("Enter a new task: ")
    tasks.append(task)
    save_tasks()
    print("Task added")

def delete_task():
    show_tasks()
    try:
        num=int(input("Enter task number to delete: "))
        removed=tasks.pop(num-1)
        save_tasks()
        print(f"Deleted: {removed}")
    except:
        print("Invalid Input!")

def update_task():
    show_tasks()
    try:
        num = int(input("Enter task number to update: "))
        new_task = input("Enter new task: ")
        tasks[num-1] = new_task
        save_tasks()
        print("Task updated")
    except:
        print("Invalid Input!")


def main():
    load_tasks() 
    while True:
        print("\n 1. Show Tasks \n 2. Add Task \n 3. Delete Task \n 4. Update Task \n 5. Exit ")
        choice=input("Choose: ")

        if choice=="1":
            show_tasks()
        elif choice=="2":
            add_task()
        elif choice=="3":
            delete_task()
        elif choice=="4":
             update_task()
        elif choice=="5":
            break
        else:
            print("Invalid Choice")



    
main()
