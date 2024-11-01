import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        # List to store tasks
        self.tasks = []

        # Task input area
        self.task_entry = tk.Entry(self.root, font=("Arial", 14), width=24)
        self.task_entry.pack(pady=10)

        # Add Task button
        add_button = tk.Button(self.root, text="Add Task", font=("Arial", 14), command=self.add_task)
        add_button.pack(pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(self.root, font=("Arial", 12), selectmode="single", width=30, height=10)
        self.task_listbox.pack(pady=10)

        # Buttons for managing tasks
        delete_button = tk.Button(self.root, text="Delete Task", font=("Arial", 14), command=self.delete_task)
        delete_button.pack(pady=5)
        
        clear_button = tk.Button(self.root, text="Clear All Tasks", font=("Arial", 14), command=self.clear_all_tasks)
        clear_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_all_tasks(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to delete all tasks?"):
            self.tasks.clear()
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
