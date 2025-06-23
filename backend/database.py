import sqlite3
from datetime import datetime

def save_attendance(attendance_list):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS attendance (
                      name TEXT, date TEXT, time TEXT)""")
    now = datetime.now()
    for name in attendance_list:
        cursor.execute("INSERT INTO attendance VALUES (?, ?, ?)", 
                       (name, now.date(), now.time()))
    conn.commit()
    conn.close()
