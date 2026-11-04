import sqlite3

from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_FILE = BASE_DIR / "todos.db"


def get_connection():
    return sqlite3.connect(DB_FILE)
def init_db():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY,
        title TEXT,
        completed INTEGER
    )
    """)

    conn.commit()

    conn.close()

def get_todos():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM todos"
    )

    rows = cursor.fetchall()

    conn.close()

    todos = []

    for row in rows:
        todo = {
            "id": row[0],
            "title": row[1],
            "completed": bool(row[2])
        }

        todos.append(todo) 
    return todos    

def add_todo(title):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO todos(title, completed)
        VALUES (?, ?)
        """,
        (title, 0)
    )

    conn.commit()

    conn.close()
def complete_todo(todo_id):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE todos
        SET completed = ?
        WHERE id = ?
        """,
        (1, todo_id)
    )

    conn.commit()

    conn.close()
def delete_todo(todo_id):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM todos
        WHERE id = ?
        """,
        (todo_id,)
    )

    conn.commit()

    conn.close()

   