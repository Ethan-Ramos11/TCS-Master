import sqlite3


def create_connection():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    return conn, cursor


def create_tables():
      