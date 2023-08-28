import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create the main window
app = tk.Tk()
app.title("Task List App")
app.geometry("300x400")

# Create the UI components
task_entry = tk.Entry(app, width=25)
add_button = tk.Button(app, text="Add Task", width=20, command=add_task)
delete_button = tk.Button(app, text="Delete Task", width=20, command=delete_task)
clear_button = tk.Button(app, text="Clear All Tasks", width=20, command=clear_tasks)
task_listbox = tk.Listbox(app, width=35, height=15)

# Place the UI components on the window
task_entry.pack(pady=10)
add_button.pack(pady=10)
delete_button.pack(pady=10)
clear_button.pack(pady=10)
task_listbox.pack(pady=10)

app.mainloop()
