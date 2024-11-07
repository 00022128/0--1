import tkinter as tk
from tkinter import ttk, messagebox

class ToDoList:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To Do List")
        self.root.geometry("200x200")

        self.tasks = []  # List to store tasks

        # Welcome label
        welcome_label = ttk.Label(self.root, text="Welcome to To Do List")
        welcome_label.grid(row=0, column=0)

        # Buttons
        view_tasks = ttk.Button(self.root, text="View Tasks", command=self.view_tasks)
        view_tasks.grid(row=1, column=0)

        add_task = ttk.Button(self.root, text="Add Task", command=self.add_task)
        add_task.grid(row=2, column=0)

        remove_task = ttk.Button(self.root, text="Remove Task", command=self.remove_task)
        remove_task.grid(row=3, column=0)

    def add_task(self):
        add_task_window = tk.Toplevel(self.root)
        add_task_window.title("Add Task")

        add_entry = ttk.Entry(add_task_window)
        add_entry.grid(row=0, column=0)

        def check_new_task():
            new_task = add_entry.get()
            if new_task in self.tasks:
                messagebox.showerror(title="Error", message="Task already exists")
            else:
                self.tasks.append(new_task)
                messagebox.showinfo(title="Success", message="Task added successfully")

        submit_new_button = ttk.Button(add_task_window, text="Submit", command=check_new_task)
        submit_new_button.grid(row=1, column=0)

    def remove_task(self):
        remove_task_window = tk.Toplevel(self.root)
        remove_task_window.title("Remove Task")

        remove_entry = ttk.Entry(remove_task_window)
        remove_entry.grid(row=0, column=0)

        def check_remove_task():
            task_to_remove = remove_entry.get()
            if task_to_remove in self.tasks:
                self.tasks.remove(task_to_remove)
                messagebox.showinfo(title="Success", message="Task removed successfully")
            else:
                messagebox.showerror(title="Error", message="Task does not exist")

        submit_remove_button = ttk.Button(remove_task_window, text="Submit", command=check_remove_task)
        submit_remove_button.grid(row=1, column=0)

    def view_tasks(self):
        view_tasks_window = tk.Toplevel(self.root)
        view_tasks_window.title("View Tasks")

        # Grid the label
        view_tasks_label = ttk.Label(view_tasks_window, text="Tasks")
        view_tasks_label.grid(row=0, column=0, pady=10)

        # Create the Treeview widget
        view_tasks_tree = ttk.Treeview(view_tasks_window)
        view_tasks_tree['columns'] = ['No', 'Task']

        # Define columns for Treeview
        view_tasks_tree.column("#0", width=0, stretch=tk.NO)
        view_tasks_tree.column("No", anchor=tk.CENTER, width=50)
        view_tasks_tree.column("Task", anchor=tk.W, width=200)

        # Define headings for Treeview
        view_tasks_tree.heading("#0", text="ID", anchor="w")
        view_tasks_tree.heading("No", text="No", anchor=tk.CENTER)
        view_tasks_tree.heading("Task", text="Task", anchor=tk.CENTER)

        # Grid the Treeview
        view_tasks_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Insert tasks into Treeview
        for index, task in enumerate(self.tasks, start=1):
            view_tasks_tree.insert("", tk.END, values=(index, task))

        # Configure grid to expand with window resizing
        view_tasks_window.grid_rowconfigure(1, weight=1)
        view_tasks_window.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.root.mainloop()
