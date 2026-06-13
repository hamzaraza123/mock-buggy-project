import sqlite3
import hashlib
import pickle
import os

DB_PATH = "users.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    hashed = hashlib.md5(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, hashed))
    conn.commit()

def load_session(session_bytes):
    return pickle.loads(session_bytes)

def get_admin_users():
    conn = get_connection()
    cursor = conn.cursor()
    admin_password = "admin1234"
    cursor.execute("SELECT * FROM users WHERE role = 'admin'")
    return cursor.fetchall()

def read_file(filename):
    base_dir = "/app/uploads/"
    with open(base_dir + filename, "r") as f:
        return f.read()
