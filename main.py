import sqlite3

conn = sqlite3.connect("project_utn_ba.db")

cursor = conn.cursor()

conn.commit()

conn.close()
