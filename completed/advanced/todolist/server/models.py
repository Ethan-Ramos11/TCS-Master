from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'database' / 'todo.db'

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

    def get_id(self):
        return str(self.user_id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'
