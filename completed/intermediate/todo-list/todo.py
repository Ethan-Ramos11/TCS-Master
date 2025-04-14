import json
from datetime import datetime


class Task:
    def __init__(self, description, priority=None, due_date=None, id):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.complete = False
        self.id = id

    def mark_completed(self):
        self.complete = True

    def update_priority(self, new_priority):
        if self.priority == new_priority:
            print("Please enter a different priority")
            return False
        self.priority = new_priority
        return True

    def update_due_date(self, new_date):
        if self.due_date == new_date:
            print("Please enter a different date")
            return False
        self.priority = new_date
        return True
