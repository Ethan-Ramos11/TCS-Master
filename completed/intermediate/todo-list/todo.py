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

