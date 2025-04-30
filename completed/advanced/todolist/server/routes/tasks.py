from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..models import db, Task

tasks = Blueprint('tasks', __name__)


@tasks.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    tasks = Task.query.filter_by(user_id=current_user.user_id).all()
    return jsonify({
        'message': 'Tasks found for user',
        'data': [task.to_dict() for task in tasks]
    })


@tasks.route('/tasks/<int:task_id>', methods=['GET'])
@login_required
def get_task(task_id):
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
    pass

# Get tasks sorted by different criteria


@tasks.route('/tasks/sorted/<string:sort_by>', methods=['GET'])
@login_required
def get_sorted_tasks(sort_by):
    pass
