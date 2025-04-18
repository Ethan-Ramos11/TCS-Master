import unittest
import json
import os
from todo import Task, Todolist


class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task("Test task", priority="high", due_date="03/20/24")

    def test_task_creation(self):
        self.assertEqual(self.task.description, "Test task")
        self.assertEqual(self.task.priority, "high")
        self.assertEqual(self.task.due_date, "03/20/24")
        self.assertFalse(self.task.completed)
        self.assertIsNotNone(self.task.id)

    def test_mark_completed(self):
        self.task.mark_completed()
        self.assertTrue(self.task.completed)

    def test_update_priority(self):
        self.assertTrue(self.task.update_priority("medium"))
        self.assertEqual(self.task.priority, "medium")
        self.assertFalse(self.task.update_priority("invalid"))

    def test_update_due_date(self):
        self.assertTrue(self.task.update_due_date("03/21/24"))
        self.assertEqual(self.task.due_date, "03/21/24")
        self.assertFalse(self.task.update_due_date("invalid-date"))

    def test_to_dict(self):
        task_dict = self.task.to_dict()
        self.assertEqual(task_dict["description"], "Test task")
        self.assertEqual(task_dict["priority"], "high")
        self.assertEqual(task_dict["due_date"], "03/20/24")
        self.assertFalse(task_dict["completed"])
        self.assertEqual(task_dict["id"], self.task.id)

    def test_from_dict(self):
        task_dict = self.task.to_dict()
        new_task = Task.from_dict(task_dict)
        self.assertEqual(new_task.description, self.task.description)
        self.assertEqual(new_task.priority, self.task.priority)
        self.assertEqual(new_task.due_date, self.task.due_date)
        self.assertEqual(new_task.completed, self.task.completed)
        self.assertEqual(new_task.id, self.task.id)


class TestTodolist(unittest.TestCase):
    def setUp(self):
        self.todo_list = Todolist()
        self.task1 = Task("Task 1", priority="high", due_date="03/20/24")
        self.task2 = Task("Task 2", priority="medium", due_date="03/21/24")
        self.task3 = Task("Task 3", priority="low", due_date="03/22/24")
        self.todo_list.add_task(self.task1)
        self.todo_list.add_task(self.task2)
        self.todo_list.add_task(self.task3)

    def test_add_task(self):
        new_task = Task("New task")
        self.assertTrue(self.todo_list.add_task(new_task))
        self.assertIn(new_task, self.todo_list.tasks)
        self.assertFalse(self.todo_list.add_task("not a task"))

    def test_remove_task(self):
        self.assertTrue(self.todo_list.remove_task(self.task1.id))
        self.assertNotIn(self.task1, self.todo_list.tasks)
        self.assertFalse(self.todo_list.remove_task("invalid-id"))

    def test_get_task(self):
        task = self.todo_list.get_task(self.task1.id)
        self.assertEqual(task, self.task1)
        self.assertIsNone(self.todo_list.get_task("invalid-id"))

    def test_filter_tasks(self):
        # Filter by priority
        filtered = self.todo_list.filter_tasks(priority="high")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0], self.task1)

        # Filter by due date
        filtered = self.todo_list.filter_tasks(due_date="03/21/24")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0], self.task2)

        # Filter by completion
        self.task1.mark_completed()
        filtered = self.todo_list.filter_tasks(completed=True)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0], self.task1)

    def test_sort_tasks(self):
        # Sort by priority
        self.todo_list.sort_tasks("priority")
        self.assertEqual(self.todo_list.tasks[0], self.task1)  # high
        self.assertEqual(self.todo_list.tasks[1], self.task2)  # medium
        self.assertEqual(self.todo_list.tasks[2], self.task3)  # low

        # Sort by description
        self.todo_list.sort_tasks("description")
        self.assertEqual(self.todo_list.tasks[0].description, "Task 1")

    def test_search_tasks(self):
        results = self.todo_list.search_tasks("Task 1")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], self.task1)

        results = self.todo_list.search_tasks("nonexistent")
        self.assertEqual(len(results), 0)

    def test_get_statistics(self):
        self.task1.mark_completed()
        stats = self.todo_list.get_statistics()
        self.assertEqual(stats["Total tasks"], 3)
        self.assertEqual(stats["Completed"], 1)
        self.assertEqual(stats["Incomplete"], 2)
        self.assertEqual(stats["With due date"], 3)
        self.assertEqual(stats["Without due date"], 0)
        self.assertAlmostEqual(stats["completion rate"], 33.33, places=2)

    def test_save_and_load(self):
        # Save to file
        filename = "test_todo.json"
        self.assertTrue(self.todo_list.save_to_file(filename))

        # Load from file
        loaded_list = Todolist.load_from_file(filename)
        self.assertIsNotNone(loaded_list)
        self.assertEqual(len(loaded_list.tasks), 3)
        self.assertEqual(
            loaded_list.tasks[0].description, self.task1.description)

        # Clean up
        os.remove(filename)

    def test_get_tasks_by_priority(self):
        priorities = self.todo_list.get_tasks_by_priority()
        self.assertEqual(priorities["high"], 1)
        self.assertEqual(priorities["medium"], 1)
        self.assertEqual(priorities["low"], 1)
        self.assertEqual(priorities["None"], 0)


if __name__ == "__main__":
    unittest.main()
