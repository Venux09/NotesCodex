#python file to store the data 

import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("notecodex.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        filename TEXT,
        type TEXT,
        summary TEXT
    )""")
    conn.commit()
    conn.close()

def save_to_db(filename, choice, result):
    conn = sqlite3.connect("notecodex.db")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    type_ = "Summary" if choice == "1" else "Notes"
    conn.execute("INSERT INTO history VALUES (NULL, ?, ?, ?, ?)",
                (date, filename, type_, result))
    conn.commit()
    conn.close()