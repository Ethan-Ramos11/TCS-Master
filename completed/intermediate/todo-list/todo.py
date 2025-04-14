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
    
    