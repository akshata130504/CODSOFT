from tkinter import Tk
from gui import TodoApp
from task_manager import TaskManager

if __name__ == "__main__":
    root = Tk()
    task_manager = TaskManager()
    app = TodoApp(root, task_manager)
    root.mainloop()
