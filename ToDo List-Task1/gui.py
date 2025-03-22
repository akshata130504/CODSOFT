import tkinter as tk
from tkinter import messagebox
from task_manager import TaskManager

class TodoApp:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager
        self.root.title("To-Do List")

        self.task_listbox = tk.Listbox(root, height=8, width=50, font=("Arial", 10))
        self.task_listbox.pack(pady=10)

        self.title_label = tk.Label(root, text="Task Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.pack()

        self.description_label = tk.Label(root, text="Task Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(root, width=40)
        self.description_entry.pack()

        self.priority_label = tk.Label(root, text="Priority:")
        self.priority_label.pack()
        self.priority_var = tk.StringVar(root)
        self.priority_var.set('Medium')
        self.priority_menu = tk.OptionMenu(root, self.priority_var, 'Low', 'Medium', 'High')
        self.priority_menu.pack()

        self.due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
        self.due_date_label.pack()
        self.due_date_entry = tk.Entry(root, width=40)
        self.due_date_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.show_all_button = tk.Button(root, text="Show All Tasks", command=self.show_all_tasks)
        self.show_all_button.pack()

        self.show_completed_button = tk.Button(root, text="Show Completed Tasks", command=self.show_completed_tasks)
        self.show_completed_button.pack()

        self.show_pending_button = tk.Button(root, text="Show Pending Tasks", command=self.show_pending_tasks)
        self.show_pending_button.pack()

        self.sort_button = tk.Button(root, text="Sort by Due Date", command=self.sort_tasks)
        self.sort_button.pack()

        self.refresh_task_list()

    def refresh_task_list(self, tasks=None):
        self.task_listbox.delete(0, tk.END)
        tasks = tasks or self.task_manager.get_task_list()
        for idx, task in enumerate(tasks, 1):
            self.task_listbox.insert(tk.END, f"{idx}. {task}")

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_var.get()
        due_date = self.due_date_entry.get()
        if title and description:
            self.task_manager.add_task(title, description, priority, due_date)
            self.refresh_task_list()
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Both title and description are required!")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_id = selected_index[0]
            title = self.title_entry.get()
            description = self.description_entry.get()
            completed = messagebox.askyesno("Mark as Completed", "Mark this task as completed?")
            priority = self.priority_var.get()
            due_date = self.due_date_entry.get()
            self.task_manager.update_task(task_id, title, description, completed, priority, due_date)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Selection Error", "Select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_manager.delete_task(selected_index[0])
            self.refresh_task_list()
        else:
            messagebox.showwarning("Selection Error", "Select a task to delete.")

    def show_all_tasks(self):
        self.refresh_task_list(self.task_manager.get_task_list())

    def show_completed_tasks(self):
        self.refresh_task_list(self.task_manager.get_task_list(completed=True))

    def show_pending_tasks(self):
        self.refresh_task_list(self.task_manager.get_task_list(completed=False))

    def sort_tasks(self):
        self.task_manager.sort_tasks_by_due_date()
        self.refresh_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager()
    app = TodoApp(root, task_manager)
    root.mainloop()
