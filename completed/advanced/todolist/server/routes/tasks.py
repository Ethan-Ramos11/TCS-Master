from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from ..models import db, Task
from sqlalchemy import or_

tasks = Blueprint('tasks', __name__)

# Initialize the limiter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Apply rate limits to all routes


@tasks.before_request
def before_request():
    limiter.check()


@tasks.route('/tasks', methods=['GET'])
@login_required
@limiter.limit("10 per minute")
def get_tasks():
    """
    Get all tasks for the current user.
    ---
    responses:
      200: List of tasks
      401: Not authenticated
      429: Too many requests
    """
    tasks = Task.query.filter_by(user_id=current_user.user_id).all()
    return jsonify({
        'message': 'Tasks found for user',
        'data': [task.to_dict() for task in tasks]
    })


@tasks.route('/tasks/<int:task_id>', methods=['GET'])
@login_required
@limiter.limit("20 per minute")
def get_task(task_id):
    """
    Get a specific task by ID.
    ---
    parameters:
      - name: task_id
        in: path
        required: true
        type: integer
    responses:
      200: Task found
      401: Not authenticated
      404: Task not found
      429: Too many requests
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
@limiter.limit("5 per minute")
def create_task():
    """
    Create a new task.
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            required: [name]
            properties:
              name: string
              description: string
              due_date: string (YYYY-MM-DD)
              priority: string (high/medium/low)
    responses:
      201: Task created
      400: Invalid input
      401: Not authenticated
      429: Too many requests
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
@limiter.limit("10 per minute")
def update_task(task_id):
    """
    Update an existing task.
    ---
    parameters:
      - name: task_id
        in: path
        required: true
        type: integer
    requestBody:
      content:
        application/json:
          schema:
            properties:
              name: string
              description: string
              due_date: string (YYYY-MM-DD)
              priority: string (high/medium/low)
    responses:
      200: Task updated
      400: Invalid input
      401: Not authenticated
      404: Task not found
      429: Too many requests
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
@limiter.limit("5 per minute")
def delete_task(task_id):
    """
    Delete a task.
    ---
    parameters:
      - name: task_id
        in: path
        required: true
        type: integer
    responses:
      200: Task deleted
      401: Not authenticated
      404: Task not found
      429: Too many requests
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
@limiter.limit("20 per minute")
def toggle_task(task_id):
    """
    Toggle task completion status.
    ---
    parameters:
      - name: task_id
        in: path
        required: true
        type: integer
    responses:
      200: Status updated
      401: Not authenticated
      404: Task not found
      429: Too many requests
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
@limiter.limit("10 per minute")
def get_tasks_by_priority(priority):
    """
    Get tasks by priority level.
    ---
    parameters:
      - name: priority
        in: path
        required: true
        type: string
        enum: [high, medium, low]
    responses:
      200: Tasks found
      401: Not authenticated
      429: Too many requests
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
@limiter.limit("10 per minute")
def get_tasks_by_due_date(date):
    """
    Get tasks due before date.
    ---
    parameters:
      - name: date
        in: path
        required: true
        type: string
        format: date
    responses:
      200: Tasks found
      400: Invalid date
      401: Not authenticated
      429: Too many requests
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
@limiter.limit("10 per minute")
def search_tasks():
    """
    Search tasks by name/description.
    ---
    parameters:
      - name: q
        in: query
        required: true
        type: string
    responses:
      200: Tasks found
      400: Missing search term
      401: Not authenticated
      429: Too many requests
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
@limiter.limit("10 per minute")
def get_sorted_tasks(sort_by='date'):
    """
    Get tasks sorted by field.
    ---
    parameters:
      - name: sort_by
        in: path
        required: true
        type: string
        enum: [date, priority, name, completed]
    responses:
      200: Tasks found
      401: Not authenticated
      429: Too many requests
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
