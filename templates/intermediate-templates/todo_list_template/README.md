# Todo List Template

This is a template for building a command-line todo list application. Use this as a starting point for your project.

## Project Requirements

Create a todo list application that implements:

- Task management (add, remove, update)
- Task organization (filter, sort, search)
- Task statistics
- Data persistence

### Basic Requirements

1. Create a Task class with:

   - Description
   - Priority (high/medium/low)
   - Due date
   - Completion status
   - Unique ID

2. Create a Todolist class with:

   - Task management methods
   - Filtering and sorting
   - Statistics tracking
   - File operations

3. Implement a command-line interface with:
   - Menu-driven navigation
   - Input validation
   - Clear output formatting

### Advanced Requirements (Optional)

1. Add task categories or tags
2. Implement task dependencies
3. Add recurring tasks
4. Implement task reminders
5. Add data export in different formats

## Project Structure

```
todo-list/
├── README.md           # This file
├── todo.py            # Main application implementation
└── tests/
    └── test_todo.py   # Unit tests
```

## Getting Started

1. Copy this template to your work-in-progress directory
2. Implement the task and todo list classes in `todo.py`
3. Write tests in `test_todo.py`
4. Document your code and add comments
5. Test your implementation thoroughly

## Tips

- Start with the Task class implementation
- Implement validation early
- Write tests as you develop
- Keep your code clean and well-documented
- Test edge cases (invalid dates, priorities, etc.)

## Example Usage

```python
# Example of how the application should work
todo_list = Todolist()
task = Task("Buy groceries", priority="high", due_date="03/20/24")
todo_list.add_task(task)
todo_list.list_tasks()
```

## Submission

When you're done:

1. Ensure all tests pass
2. Update this README with your implementation details
3. Move the project to the completed directory
4. Create a pull request for review
