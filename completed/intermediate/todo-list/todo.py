import json
from datetime import datetime
import re
import uuid


class Task:
    def __init__(self, description, id=None, priority=None, due_date=None):
        pattern = r'^\d{2}/\d{2}/\d{2}$'

        self.description = description
        if priority != None and priority.lower() in ["high", "medium", "low"]:
            self.priority = priority
        else:
            self.priority = None
        if re.match(pattern, due_date):
            self.due_date = due_date
        else:
            self.due_date = None
        self.completed = False
        if id != None:
            self.id = id
        else:
            self.id = str(uuid.uuid4())

    def mark_completed(self):
        self.completed = True

    def update_priority(self, new_priority):
        if self.priority == new_priority:
            print("Please enter a different priority")
            return False

        if new_priority.lower() not in ["high", "medium", "low"]:
            print("Please enter high, medium, or low for the priority")
            return False
        self.priority = new_priority
        return True

    def update_due_date(self, new_date):
        pattern = r'^\d{2}/\d{2}/\d{2}$'

        if self.due_date == new_date:
            print("Please enter a different date")
            return False

        if not re.match(pattern, new_date):
            print("Please enter a date in the format of mm/dd/yy")
            return False

        self.due_date = new_date
        return True

    def to_dict(self):
        info = {
            "id": self.id,
            "description": self.description,
            "due date": self.due_date,
            "priority": self.priority,
            "complete": self.completed
        }
        return info

    @classmethod
    def from_dict(cls, data):
        new_task = cls(data["description"], data["id"],
                       data["priority"], data["due_date"])
        return new_task


class Todolist:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not isinstance(task, Task):
            print("Please enter an actual task")
            return False
        self.tasks.append(task)
        return True

    def remove_task(self, task_id):
        if type(task_id) != str:
            print("Please enter a valid task_id")
        for i in range(len(self.tasks)):
            if self.tasks[i].id == task_id:
                del self.tasks[i]
                return True
        print("Task not in list")
        return False

    def get_task(self, task_id):
        if type(task_id) != str:
            print("Please enter a valid task_id")
        for i in range(len(self.tasks)):
            if self.tasks[i].id == task_id:
                return self.tasks[i]
        print("Task not in list")
        return None

    def list_tasks(self):
        pass

    def filter_tasks(self, priority=None, due_date=None, completed=None):
        filtered = []

        for task in self.tasks:
            add = True
            if priority != None and task.priority != priority:
                add = False
            elif due_date != None and task.due_date != due_date:
                add = False
            elif completed != None and task.completed != completed:
                add = False
            if add:
                filtered.append(task)
        return filtered

    def mark_task_completed(self, task_id):
        pass

    def update_task_priority(self, task_id, new_priority):
        pass

    def update_task_due_date(self, task_id, new_due_date):
        pass

    def save_to_file(self, filename):
        pass

    @classmethod
    def load_from_file(cls, filename):
        pass

    def sort_tasks(self, by='priority'):
        pass

    def search_tasks(self, keyword):
        pass

    def get_statistics(self):
        pass

    def get_tasks_by_priority(self):
        pass
