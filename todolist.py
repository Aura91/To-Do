import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List!")

#Adding task
def add_task():
    task = entry_task.get()
    #Only add task if it's not blank
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

#Deleting tasks by getting the index
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

#Loading the task from tasks.dat in read binary mode
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

#Save the taks in tasks.dat using pickle module in write binary mode
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

# Create Frame
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

#Create Listbox
listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50, bg="#181818", fg="White" )
listbox_tasks.pack(side=tkinter.LEFT)

#Create scrollbar
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

#Make scrollbar scroll
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

#Make entry widget to enter tasks
entry_task = tkinter.Entry(root, width=50)
entry_task.insert(tkinter.END, "Enter your task here")
entry_task.pack()

#Buttons
button_add_task = tkinter.Button(root, text="Add task", width=46, bg="Grey", command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", bg="Grey", width=46, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Load tasks", bg="Grey", width=46, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks", bg="Grey", width=46, command=save_tasks)
button_save_tasks.pack()

root.mainloop()
