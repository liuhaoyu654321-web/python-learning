import sqlite3


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "chat.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY,
            question TEXT,
            summary TEXT,
            category TEXT,
            urgent INTEGER,
            confidence REAL
        )
    """)

    conn.commit()
    conn.close()


def save_analysis(question, result):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analyses (
            question,
            summary,
            category,
            urgent,
            confidence
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            question,
            result.summary,
            result.category,
            result.urgent,
            result.confidence
        )
    )

    conn.commit()
    conn.close()


def get_analyses():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM analyses")

    rows = cursor.fetchall()

    conn.close()

    return rows