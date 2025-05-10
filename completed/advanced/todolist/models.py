from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import CheckConstraint

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    user_id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(
        80), unique=True, nullable=False)
    email = db.Column('email', db.String(120), unique=True, nullable=False)
    password = db.Column('password', db.String(128), nullable=False)
    first_name = db.Column('first_name', db.String(80))
    last_name = db.Column('last_name', db.String(80))
    tasks = db.relationship('Task', backref='user', lazy=True)

    def get_id(self):
        return str(self.user_id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Task(db.Model):
    __tablename__ = 'tasks'

    task_id = db.Column('task_id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'))
    name = db.Column('name', db.String(100), nullable=False)
    description = db.Column('description', db.Text)
    due_date = db.Column('due_date', db.DateTime)
    completed = db.Column('completed', db.String(10), default='incomplete')
    priority = db.Column('priority', db.String(10), default='medium')

    __table_args__ = (
        CheckConstraint(completed.in_(
            ['completed', 'incomplete']), name='check_completed'),
        CheckConstraint(priority.in_(
            ['high', 'medium', 'low']), name='check_priority'),
    )

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'completed': self.completed,
            'priority': self.priority
        }

    def flip_completed(self):
        if self.completed == "incomplete":
            self.completed = "completed"
        else:
            self.completed = "incomplete"
