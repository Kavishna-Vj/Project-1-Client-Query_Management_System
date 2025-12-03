import sqlite3

db_name = "query.db"

def get_connection():
  conn =  sqlite3.connect(db_name, check_same_thread=False)
  return conn

def setup_database():
    conn = get_connection()
    c = conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS users(
              username TEXT PRIMARY KEY,
              hashed_password TEXT,
              role TEXT)""")
    
    c.execute(""" CREATE TABLE IF NOT EXISTS queries(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                mobile TEXT,
                heading TEXT,
                description TEXT,
                created_time TEXT,
                closed_time TEXT,
                status TEXT)""")
    conn.commit()
    conn.close()