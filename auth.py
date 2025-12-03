import hashlib
from db import get_connection

def hashed_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username: str, password: str, role: str) -> None:
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO users(username, hashed_password, role) VALUES(?, ?, ?)",
               (username, hashed_password(password), role))
    conn.commit()
    conn.close()

def verify_user(username: str, password: str):
    conn = get_connection()
    c= conn.cursor()
    c.execute("SELECT role FROM users WHERE username=? AND hashed_password=?",
    (username, hashed_password(password)))
    data = c.fetchone()
    conn.close()
    return data[0] if data else None