import sqlite3

def create_connection():
    conn = sqlite3.connect("usuarios_bytes.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        password BLOB NOT NULL
    )
    """)

    conn.commit()
    conn.close()

