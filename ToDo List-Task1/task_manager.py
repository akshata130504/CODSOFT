import json
from datetime import datetime

class Task:
    def __init__(self, title, description, completed=False, priority='Medium', due_date=None, history=None):
        self.title = title
        self.description = description
        self.completed = completed
        self.priority = priority
        self.due_date = due_date
        self.history = history if history else []

    def __str__(self):
        status = "✔" if self.completed else "✗"
        return f"{status} {self.title} (Priority: {self.priority}, Due: {self.due_date}): {self.description}"

    def add_history(self, action):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.history.append(f"{action} at {timestamp}")

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                return [Task(**task) for task in json.load(file)]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)

    def add_task(self, title, description, priority, due_date):
        new_task = Task(title, description, priority=priority, due_date=due_date)
        new_task.add_history("Task added")
        self.tasks.append(new_task)
        self.save_tasks()

    def update_task(self, task_id, title=None, description=None, completed=None, priority=None, due_date=None):
        if 0 <= task_id < len(self.tasks):
            task = self.tasks[task_id]
            if title:
                task.title = title
            if description:
                task.description = description
            if completed is not None:
                task.completed = completed
            if priority:
                task.priority = priority
            if due_date:
                task.due_date = due_date
            task.add_history("Task updated")
            self.save_tasks()

    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks.pop(task_id)
            self.save_tasks()

    def get_task_list(self, completed=None):
        if completed is None:
            return self.tasks
        return [task for task in self.tasks if task.completed == completed]

    def sort_tasks_by_due_date(self):
        self.tasks.sort(key=lambda task: task.due_date or "9999-12-31")
        self.save_tasks()
