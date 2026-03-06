
import sqlite3
import bcrypt
from database import create_connection

def create_user(usuarios, password):
    conn = create_connection()
    cursor = conn.cursor()


    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor.execute(
        "INSERT INTO usuarios (usuario, password) VALUES (?, ?)",
        (usuarios, hashed)
    )

    conn.commit()
    conn.close()


def get_user(usuarios):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = ?",
        (usuarios,)
    )

    user = cursor.fetchone()

    conn.close()
    return user