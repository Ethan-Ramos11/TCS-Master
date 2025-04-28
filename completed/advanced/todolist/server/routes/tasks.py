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
# Get a single task by ID


@tasks.route('/tasks/<int:task_id>', methods=['GET'])
@login_required
def get_task(task_id):
    pass

# Create a new task


@tasks.route('/tasks', methods=['POST'])
@login_required
def create_task():
    pass

# Update an existing task


@tasks.route('/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    pass

# Delete a task


@tasks.route('/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    pass

# Mark task as complete/incomplete


@tasks.route('/tasks/<int:task_id>/toggle', methods=['POST'])
@login_required
def toggle_task(task_id):
    pass


# Filter tasks by priority


@tasks.route('/tasks/priority/<string:priority>', methods=['GET'])
@login_required
def get_tasks_by_priority(priority):
    pass

# Get tasks due before/after a specific date


@tasks.route('/tasks/due/<string:date>', methods=['GET'])
@login_required
def get_tasks_by_due_date(date):
    pass

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

# Bulk update task priorities


@tasks.route('/tasks/bulk-priority', methods=['PUT'])
@login_required
def bulk_update_priority():
    pass
