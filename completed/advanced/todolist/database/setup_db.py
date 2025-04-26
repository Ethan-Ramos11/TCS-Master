import sqlite3
from .schema import SCHEMA


def create_connection():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    return conn, cursor


def convert_to_sql_columns(info):
    s = ""
    for key, val in info.items():
        s += f"{key} {val},"
    return s[:-1]


