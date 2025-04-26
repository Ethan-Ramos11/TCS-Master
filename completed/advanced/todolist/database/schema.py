SCHEMA = {
    "users":
    {
        "columns": {
            "user_id": 'INTEGER PRIMARY KEY',
            "username": 'TEXT UNIQUE NOT NULL',
            "email": 'TEXT UNIQUE NOT NULL',
            "password": 'TEXT NOT NULL',
            "first_name": 'TEXT',
            "last_name": 'TEXT',
        }
    },
    "tasks":
    {
        "columns": {
            "task_id": "INTEGER PRIMARY KEY",
            "user_id": "INTEGER",
            "name": "TEXT NOT NULL",
            "description": "TEXT",
            "due_date": "TIMESTAMP",
            "priority": "TEXT CHECK(priority IN ('high', 'medium', 'low'))"
        },
        "foreign_keys": {
          "user_id": "users(user_id)"
        }
    }
}
