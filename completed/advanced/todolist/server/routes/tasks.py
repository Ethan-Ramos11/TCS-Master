from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..models import db, Task
from sqlalchemy import or_
tasks = Blueprint('tasks', __name__)


@tasks.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    """
    Get all tasks for the current user.

    ---
    tags:
      - Tasks
    responses:
      200:
        description: List of tasks retrieved successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Tasks found for user
                data:
                  type: array
                  items:
                    type: object
                    properties:
                      task_id:
                        type: integer
                      name:
                        type: string
                      description:
                        type: string
                      due_date:
                        type: string
                        format: date
                      priority:
                        type: string
                      completed:
                        type: boolean
                      user_id:
                        type: integer
      401:
        description: User not authenticated
    """
    tasks = Task.query.filter_by(user_id=current_user.user_id).all()
    return jsonify({
        'message': 'Tasks found for user',
        'data': [task.to_dict() for task in tasks]
    })


@tasks.route('/tasks/<int:task_id>', methods=['GET'])
@login_required
def get_task(task_id):
    """
    Get a specific task by ID.

    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the task to retrieve
    responses:
      200:
        description: Task retrieved successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Task found
                data:
                  type: object
                  properties:
                    task_id:
                      type: integer
                    name:
                      type: string
                    description:
                      type: string
                    due_date:
                      type: string
                      format: date
                    priority:
                      type: string
                    completed:
                      type: boolean
                    user_id:
                      type: integer
      401:
        description: User not authenticated
      404:
        description: Task not found
    """
    task = Task.query.filter_by(
        task_id=task_id, user_id=current_user.user_id).first()
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({
        'message': 'Task found',
        'data': task.to_dict()
    })

# Create a new task


@tasks.route('/tasks', methods=['POST'])
@login_required
def create_task():
    """
    Create a new task.

    ---
    tags:
      - Tasks
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - name
            properties:
              name:
                type: string
                description: Name of the task
              description:
                type: string
                description: Detailed description of the task
              due_date:
                type: string
                format: date
                description: Due date of the task (YYYY-MM-DD)
              priority:
                type: string
                description: Priority level of the task
                enum: [high, medium, low]
    responses:
      201:
        description: Task created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Task successfully added
                data:
                  type: object
                  properties:
                    task_id:
                      type: integer
                    name:
                      type: string
                    description:
                      type: string
                    due_date:
                      type: string
                      format: date
                    priority:
                      type: string
                    completed:
                      type: boolean
                    user_id:
                      type: integer
      400:
        description: Invalid input data
      401:
        description: User not authenticated
    """
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    due_date = data.get("due_date")
    priority = data.get("priority")
    if not name:
        return jsonify({'error': 'expected a name'})

    new_task = Task(
        name=name,
        user_id=current_user.user_id,
        description=description,
        due_date=due_date,
        priority=priority
    )
    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        'message': 'Task successfully added',
        'data': new_task.to_dict()
    }), 201
# Update an existing task


@tasks.route('/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    """
    Update an existing task.

    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the task to update
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
                description: New name of the task
              description:
                type: string
                description: New description of the task
              due_date:
                type: string
                format: date
                description: New due date of the task (YYYY-MM-DD)
              priority:
                type: string
                description: New priority level of the task
                enum: [high, medium, low]
    responses:
      200:
        description: Task updated successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Task updated successfully
                data:
                  type: object
                  properties:
                    task_id:
                      type: integer
                    name:
                      type: string
                    description:
                      type: string
                    due_date:
                      type: string
                      format: date
                    priority:
                      type: string
                    completed:
                      type: boolean
                    user_id:
                      type: integer
      400:
        description: Invalid input data
      401:
        description: User not authenticated
      404:
        description: Task not found
    """
    task = Task.query.filter_by(
        task_id=task_id, user_id=current_user.user_id).first()
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No update data provided'}), 404

    allowed_fields = ['name', 'description', 'due_date', 'priority']
    for field in allowed_fields:
        if field in data:
            setattr(task, field, data[field])

    db.session.commit()
    return jsonify({
        'message': 'Task updated successfully',
        'data': task.to_dict()
    })
# Delete a task


@tasks.route('/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    """
    Delete a task.

    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the task to delete
    responses:
      200:
        description: Task deleted successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Task deleted successfully
      401:
        description: User not authenticated
      404:
        description: Task not found
    """
    task = Task.query.filter_by(
        task_id=task_id,
        user_id=current_user.user_id
    ).first()
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({
        'message': 'Task deleted successfully'
    })

# Mark task as complete/incomplete


@tasks.route('/tasks/<int:task_id>/toggle', methods=['POST'])
@login_required
def toggle_task(task_id):
    """
    Toggle the completion status of a task.

    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the task to toggle
    responses:
      200:
        description: Task completion status updated
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Task completion status updated
                data:
                  type: object
                  properties:
                    task_id:
                      type: integer
                    name:
                      type: string
                    description:
                      type: string
                    due_date:
                      type: string
                      format: date
                    priority:
                      type: string
                    completed:
                      type: boolean
                    user_id:
                      type: integer
      401:
        description: User not authenticated
      404:
        description: Task not found
    """
    task = Task.query.filter_by(
        task_id=task_id,
        user_id=current_user.user_id
    ).first()
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    task.flip_completed()
    db.session.commit()
    return jsonify({
        'message': 'Task completion status updated',
        'data': task.to_dict()
    })

# Filter tasks by priority


@tasks.route('/tasks/priority/<string:priority>', methods=['GET'])
@login_required
def get_tasks_by_priority(priority):
    """
    Get tasks filtered by priority level.

    ---
    tags:
      - Tasks
    parameters:
      - name: priority
        in: path
        required: true
        schema:
          type: string
          enum: [high, medium, low]
        description: Priority level to filter tasks by
    responses:
      200:
        description: Tasks retrieved successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Tasks with priority high found
                data:
                  type: array
                  items:
                    type: object
                    properties:
                      task_id:
                        type: integer
                      name:
                        type: string
                      description:
                        type: string
                      due_date:
                        type: string
                        format: date
                      priority:
                        type: string
                      completed:
                        type: boolean
                      user_id:
                        type: integer
      401:
        description: User not authenticated
    """
    tasks = Task.query.filter_by(
        priority=priority,
        user_id=current_user.user_id
    ).all()
    return jsonify({
        'message': f'Tasks with priority {priority} found',
        'data': [task.to_dict() for task in tasks]
    })

# Get tasks due before a specific date


@tasks.route('/tasks/due/<string:date>', methods=['GET'])
@login_required
def get_tasks_by_due_date(date):
    """
    Get tasks due before a specific date.

    ---
    tags:
      - Tasks
    parameters:
      - name: date
        in: path
        required: true
        schema:
          type: string
          format: date
        description: Date to filter tasks by (YYYY-MM-DD)
    responses:
      200:
        description: Tasks retrieved successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Tasks due by 2023-12-31
                data:
                  type: array
                  items:
                    type: object
                    properties:
                      task_id:
                        type: integer
                      name:
                        type: string
                      description:
                        type: string
                      due_date:
                        type: string
                        format: date
                      priority:
                        type: string
                      completed:
                        type: boolean
                      user_id:
                        type: integer
      400:
        description: Invalid date format
      401:
        description: User not authenticated
    """
    try:
        tasks = Task.query.filter(
            Task.due_date < date,
            Task.user_id == current_user.user_id
        ).all()
        return jsonify({
            'message': f'Tasks due by {date}',
            'data': [task.to_dict() for task in tasks]
        })
    except Exception as e:
        return jsonify({'error': 'Invalid date format or database error'}), 400

    # Search tasks by name or description


@tasks.route('/tasks/search', methods=['GET'])
@login_required
def search_tasks():
    """
    Search tasks by name or description.

    ---
    tags:
      - Tasks
    parameters:
      - name: q
        in: query
        required: true
        schema:
          type: string
        description: Search term to look for in task names and descriptions
    responses:
      200:
        description: Tasks retrieved successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Tasks retrieved
                data:
                  type: array
                  items:
                    type: object
                    properties:
                      task_id:
                        type: integer
                      name:
                        type: string
                      description:
                        type: string
                      due_date:
                        type: string
                        format: date
                      priority:
                        type: string
                      completed:
                        type: boolean
                      user_id:
                        type: integer
      400:
        description: Search term is required
      401:
        description: User not authenticated
    """
    search_term = request.args.get('q', '')
    if not search_term:
        return jsonify({'error': 'Search term is required'}), 400

    tasks = Task.query.filter(
        Task.user_id == current_user.user_id,
        or_(
            Task.name.ilike(f'%{search_term}%'),
            Task.description.ilike(f'%{search_term}%')
        )
    ).all()
    return jsonify({
        'message': 'Tasks retrieved',
        'data': [task.to_dict() for task in tasks]})

    # Get tasks sorted by different criteria


@tasks.route('/tasks/sorted/<string:sort_by>', methods=['GET'])
@login_required
def get_sorted_tasks(sort_by='date'):
    """
    Get tasks sorted by different criteria.

    ---
    tags:
      - Tasks
    parameters:
      - name: sort_by
        in: path
        required: true
        schema:
          type: string
          enum: [date, priority, name, completed]
        description: Field to sort tasks by
    responses:
      200:
        description: Tasks retrieved successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Tasks sorted by due_date
                data:
                  type: array
                  items:
                    type: object
                    properties:
                      task_id:
                        type: integer
                      name:
                        type: string
                      description:
                        type: string
                      due_date:
                        type: string
                        format: date
                      priority:
                        type: string
                      completed:
                        type: boolean
                      user_id:
                        type: integer
      401:
        description: User not authenticated
    """
    sort_fields = {
        'date': Task.due_date,
        'priority': Task.priority,
        'name': Task.name,
        'completed': Task.completed
    }

    sort_field = sort_fields.get(sort_by, Task.due_date)

    tasks = Task.query.filter_by(
        user_id=current_user.user_id).order_by(sort_field).all()
    return jsonify({
        'message': f'Tasks sorted by {sort_field}',
        'data': [task.to_dict() for task in tasks]
    })
