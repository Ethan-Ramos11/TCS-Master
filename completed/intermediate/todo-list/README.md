# Todo List Application

A command-line todo list application that allows you to manage tasks with priorities, due dates, and completion status.

## Features

- **Task Management**

  - Add new tasks with description, priority, and due date
  - Mark tasks as completed
  - Update task priority and due date
  - Remove tasks
  - View all tasks in a nicely formatted display

- **Task Organization**

  - Filter tasks by priority, due date, or completion status
  - Sort tasks by priority, due date, completion status, or description
  - Search tasks by keyword

- **Statistics**

  - View total number of tasks
  - Track completed and incomplete tasks
  - Monitor tasks with and without due dates
  - View completion rate
  - See priority breakdown

- **Data Persistence**
  - Save todo list to a file
  - Load todo list from a file
  - JSON format for easy data exchange

## Usage

1. Run the application:

   ```bash
   python todo.py
   ```

2. Main Menu Options:

   - `1`: Add new task
   - `2`: List all tasks
   - `3`: Search tasks
   - `4`: Filter tasks
   - `5`: Sort tasks
   - `6`: Update task
   - `7`: View statistics
   - `8`: Save todo list
   - `9`: Load todo list
   - `0`: Exit

3. Task Properties:
   - **Description**: Text describing the task
   - **Priority**: high, medium, low, or none
   - **Due Date**: Format mm/dd/yy
   - **Completion Status**: Complete or Incomplete

## Examples

### Adding a Task

```
Enter task description: Buy groceries
Enter priority (high/medium/low/none): high
Enter due date (mm/dd/yy) or leave empty: 03/20/24
```

### Filtering Tasks

```
Filter by:
1. Priority
2. Due Date
3. Completion Status
Enter your choice (1-3): 1
Enter priority (high/medium/low/none): high
```

### Viewing Statistics

```
=== Statistics ===
Total tasks: 5
Completed: 2
Incomplete: 3
With due date: 4
Without due date: 1
Completion rate: 40.00%

Priority breakdown:
high: 2
medium: 1
low: 1
None: 1
```

## Requirements

- Python 3.x
- No external dependencies required

## File Format

The todo list is saved in JSON format with the following structure:

```json
{
  "list_name": "My list",
  "tasks": [
    {
      "id": "unique-uuid",
      "description": "Task description",
      "priority": "high",
      "due_date": "03/20/24",
      "completed": false
    }
  ]
}
```

## Error Handling

The application includes error handling for:

- Invalid input
- File operations
- Task operations
- Date format validation
- Priority validation
