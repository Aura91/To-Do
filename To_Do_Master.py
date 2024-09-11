import tkinter as tk
from tkinter import ttk, messagebox
import json


root = tk.Tk()
root.title("To-Do Master")
root.geometry("400x400")
root.configure(bg="#333333")

# Adding task
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task) # Insert the task text into the entry widget
        entry_task.delete(0, tk.END) # Clear the entry widget  
    else:
        messagebox.showwarning(title="Warning!", message="You must enter a task.")

# Deleting tasks
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning(title="Warning!", message="You must select a task.")

# Loading tasks
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        listbox_tasks.delete(0, tk.END)
        for task in tasks:
            listbox_tasks.insert(tk.END, task)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning!", message="Cannot find tasks.json.")

# Saving tasks
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    status_var.set("Tasks saved!")

# Editing a task
def edit_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(task_index) # Get the task text
        entry_task.delete(0, tk.END) # Clear the entry widget  
        entry_task.insert(tk.END, task) # Insert the task text into the entry widget
        delete_task()
    except IndexError:
        messagebox.showwarning(title="Warning!", message="You must select a task.")

# Keyboard shortcuts
def add_task_shortcut(event):
    add_task()

def delete_task_shortcut(event):
    delete_task()

def save_tasks_shortcut(event):
    save_tasks()

def clear_placeholder(event):
    entry_task.delete(0, 'end')

# Create Frame
frame_tasks = tk.Frame(root, bg="#333333")
frame_tasks.pack(pady=10)

# Create Listbox
listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, bg="#444444", fg="white", selectbackground="#888888")
listbox_tasks.pack(side=tk.LEFT)

# Create scrollbar
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# Make scrollbar scroll
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Make entry widget to enter tasks
entry_task = ttk.Entry(root, width=50)
entry_task.insert(0, "Enter your task here")
entry_task.bind("<FocusIn>", clear_placeholder)
entry_task.pack(pady=10)

# Buttons
button_add_task = tk.Button(root, text="Add Task", width=46, bg="#666666", fg="white", command=add_task)
button_add_task.pack(pady=2)

button_delete_task = tk.Button(root, text="Delete Task", width=46, bg="#666666", fg="white", command=delete_task)
button_delete_task.pack(pady=2)

button_edit_task = tk.Button(root, text="Edit Task", width=46, bg="#666666", fg="white", command=edit_task)
button_edit_task.pack(pady=2)

button_load_tasks = tk.Button(root, text="Load Tasks", width=46, bg="#666666", fg="white", command=load_tasks)
button_load_tasks.pack(pady=2)

button_save_tasks = tk.Button(root, text="Save Tasks", width=46, bg="#666666", fg="white", command=save_tasks)
button_save_tasks.pack(pady=2)

# Status bar
status_var = tk.StringVar()
status_bar = tk.Label(root, textvariable=status_var, bg="#333333", fg="white", anchor='w')
status_bar.pack(fill='x')

# Bind keyboard shortcuts
root.bind('<Return>', add_task_shortcut)
root.bind('<Delete>', delete_task_shortcut)
root.bind('<Control-s>', save_tasks_shortcut)

root.mainloop()
