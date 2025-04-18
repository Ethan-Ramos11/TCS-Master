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
    def __init__(self, list_name="My list"):
        self.list_name = list_name
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
        for task in self.tasks:
            description = task.description
            priority = task.priority if task.priority else "None"
            due_date = task.due_date if task.due_date else "None"
            status = "✅ Complete" if task.completed else "⬜ Incomplete"

            max_length = max(len(description), len(priority),
                             len(due_date), len(status)) + 2
            box_width = max_length + 4  # Add padding for borders

            top_border = "┌" + "─" * (box_width - 2) + "┐"
            bottom_border = "└" + "─" * (box_width - 2) + "┘"
            separator = "├" + "─" * (box_width - 2) + "┤"

            desc_line = f"│ Task: {description.ljust(max_length)} │"
            priority_line = f"│ Priority: {priority.ljust(max_length - 9)} │"
            due_line = f"│ Due Date: {due_date.ljust(max_length - 10)} │"
            status_line = f"│ Status: {status.ljust(max_length - 8)} │"

            print(top_border)
            print(desc_line)
            print(separator)
            print(priority_line)
            print(due_line)
            print(status_line)
            print(bottom_border)
            print()

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
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return True
        print("Task not found")
        return False

    def update_task_priority(self, task_id, new_priority):
        for task in self.tasks:
            if task.id == task_id:
                task.update_priority(new_priority)
                return True
        print("Task not found")
        return False

    def update_task_due_date(self, task_id, new_due_date):
        for task in self.tasks:
            if task.id == task_id:
                task.update_due_date(new_due_date)
                return True
        print("Task not found")
        return False

    def save_to_file(self, filename):
        try:
            data = {"list_name": self.list_name,
                    "tasks": [task.to_dict() for task in self.tasks]}
            with open(filename, "w") as file:
                json.dump(data, file)
            return True
        except FileNotFoundError:
            print("File not found")
            return False
        except PermissionError:
            print("No permission to write to file")
            return False
        except IOError as e:
            print(f"Error writing to file: {e}")
            return False

    @classmethod
    def load_from_file(cls, filename):
        try:

            with open(filename, "r") as file:
                info = json.load(file)
                new_lst = cls(info["list_name"])
                for task_data in info["tasks"]:
                    task = Task.from_dict(task_data)
                    new_lst.add_task(task)
                return new_lst
        except FileNotFoundError:
            print("File not found")
            return None
        except json.JSONDecodeError:
            print("Invalid JSON format")
            return None

    def sort_tasks(self, by='priority'):
        if by == 'priority':
            priority_order = {"high": 0, "medium": 1, "low": 2, "None": 3}
            self.tasks.sort(key=lambda task: priority_order.get(
                task.priority if task.priority else "None", 3))
        elif by == 'due_date':
            self.tasks.sort(key=lambda task:
                            (task.due_date is None,
                             task.due_date if task.due_date else ''))
        elif by == 'completion':
            self.tasks.sort(key=lambda task: task.completed)
        elif by == 'description':
            self.tasks.sort(key=lambda task: task.description)
        else:
            print(f"Invalid entry for sort: {by}")
            return False
        return True

    def search_tasks(self, keyword):
        tasks_with_keyword = []
        for task in self.tasks:
            if keyword.lower() in task.description:
                tasks_with_keyword.append(task)
        return tasks_with_keyword

    def get_statistics(self):
        stats = {}
        stats["Total tasks"] = len(self.tasks)
        stats["Completed"] = 0
        stats["Incomplete"] = 0
        stats["With due date"] = 0
        stats["Without due date"] = 0
        for task in self.tasks:
            if task.completed:
                stats["Completed"] += 1
            else:
                stats["Incomplete"] += 1
            if task.due_date:
                stats["With due date"] += 1
            else:
                stats["Without due date"] += 1
        stats["priority breakdown"] = self.get_tasks_by_priority()
        if stats["Total tasks"] > 0:
            stats["completion rate"] = stats["Completed"] / \
                stats["Total tasks"] * 100
        else:
            stats["completion rate"] = 0
        return stats

    def get_tasks_by_priority(self):
        task_priorities = {
            "high": 0,
            "medium": 0,
            "low": 0,
            "None": 0
        }
        for task in self.tasks:
            if task.priority == None:
                task_priorities["None"] += 1
            else:
                task_priorities[task.priority] += 1
        return task_priorities


def main():
    todo_list = Todolist()

    while True:
        print("\n=== Todo List Manager ===")
        print("1. Add new task")
        print("2. List all tasks")
        print("3. Search tasks")
        print("4. Filter tasks")
        print("5. Sort tasks")
        print("6. Update task")
        print("7. View statistics")
        print("8. Save todo list")
        print("9. Load todo list")
        print("0. Exit")

        choice = input("\nEnter your choice (0-9): ")

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter priority (high/medium/low/none): ").lower()
            if priority not in ["high", "medium", "low", "none"]:
                priority = None
            due_date = input("Enter due date (mm/dd/yy) or leave empty: ")
            if not due_date:
                due_date = None
            task = Task(description, priority=priority, due_date=due_date)
            if todo_list.add_task(task):
                print("Task added successfully!")
            else:
                print("Failed to add task.")

        elif choice == "2":
            if not todo_list.tasks:
                print("No tasks in the list.")
            else:
                todo_list.list_tasks()

        elif choice == "3":
            keyword = input("Enter search keyword: ")
            results = todo_list.search_tasks(keyword)
            if not results:
                print("No tasks found.")
            else:
                for task in results:
                    print(f"\nTask: {task.description}")
                    print(
                        f"Priority: {task.priority if task.priority else 'None'}")
                    print(
                        f"Due Date: {task.due_date if task.due_date else 'None'}")
                    print(
                        f"Status: {'Complete' if task.completed else 'Incomplete'}")

        elif choice == "4":
            print("\nFilter by:")
            print("1. Priority")
            print("2. Due Date")
            print("3. Completion Status")
            filter_choice = input("Enter your choice (1-3): ")

            if filter_choice == "1":
                priority = input(
                    "Enter priority (high/medium/low/none): ").lower()
                if priority not in ["high", "medium", "low", "none"]:
                    print("Invalid priority.")
                    continue
                filtered = todo_list.filter_tasks(priority=priority)
            elif filter_choice == "2":
                due_date = input("Enter due date (mm/dd/yy): ")
                filtered = todo_list.filter_tasks(due_date=due_date)
            elif filter_choice == "3":
                completed = input(
                    "Show completed tasks? (y/n): ").lower() == "y"
                filtered = todo_list.filter_tasks(completed=completed)
            else:
                print("Invalid choice.")
                continue

            if not filtered:
                print("No tasks found.")
            else:
                for task in filtered:
                    print(f"\nTask: {task.description}")
                    print(
                        f"Priority: {task.priority if task.priority else 'None'}")
                    print(
                        f"Due Date: {task.due_date if task.due_date else 'None'}")
                    print(
                        f"Status: {'Complete' if task.completed else 'Incomplete'}")

        elif choice == "5":
            print("\nSort by:")
            print("1. Priority")
            print("2. Due Date")
            print("3. Completion Status")
            print("4. Description")
            sort_choice = input("Enter your choice (1-4): ")

            if sort_choice == "1":
                todo_list.sort_tasks("priority")
            elif sort_choice == "2":
                todo_list.sort_tasks("due_date")
            elif sort_choice == "3":
                todo_list.sort_tasks("completion")
            elif sort_choice == "4":
                todo_list.sort_tasks("description")
            else:
                print("Invalid choice.")
                continue

            print("Tasks sorted successfully!")

        elif choice == "6":
            task_id = input("Enter task ID: ")
            task = todo_list.get_task(task_id)
            if not task:
                print("Task not found.")
                continue

            print("\nUpdate:")
            print("1. Priority")
            print("2. Due Date")
            print("3. Completion Status")
            update_choice = input("Enter your choice (1-3): ")

            if update_choice == "1":
                new_priority = input(
                    "Enter new priority (high/medium/low/none): ").lower()
                if todo_list.update_task_priority(task_id, new_priority):
                    print("Priority updated successfully!")
                else:
                    print("Failed to update priority.")
            elif update_choice == "2":
                new_date = input("Enter new due date (mm/dd/yy): ")
                if todo_list.update_task_due_date(task_id, new_date):
                    print("Due date updated successfully!")
                else:
                    print("Failed to update due date.")
            elif update_choice == "3":
                if todo_list.mark_task_completed(task_id):
                    print("Task marked as completed!")
                else:
                    print("Failed to update task status.")
            else:
                print("Invalid choice.")

        elif choice == "7":
            stats = todo_list.get_statistics()
            print("\n=== Statistics ===")
            print(f"Total tasks: {stats['Total tasks']}")
            print(f"Completed: {stats['Completed']}")
            print(f"Incomplete: {stats['Incomplete']}")
            print(f"With due date: {stats['With due date']}")
            print(f"Without due date: {stats['Without due date']}")
            print(f"Completion rate: {stats['completion rate']:.2f}%")
            print("\nPriority breakdown:")
            for priority, count in stats['priority breakdown'].items():
                print(f"{priority}: {count}")

        elif choice == "8":
            filename = input("Enter filename to save: ")
            if todo_list.save_to_file(filename):
                print("Todo list saved successfully!")
            else:
                print("Failed to save todo list.")

        elif choice == "9":
            filename = input("Enter filename to load: ")
            loaded_list = Todolist.load_from_file(filename)
            if loaded_list:
                todo_list = loaded_list
                print("Todo list loaded successfully!")
            else:
                print("Failed to load todo list.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
