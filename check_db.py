
from db import create_table
create_table()

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "documents.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("DB PATH:")
print(DB_PATH)

print("\nTABLES:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

print("\nSCHEMA:")
cursor.execute("PRAGMA table_info(documents);")
for row in cursor.fetchall():
    print(row)

print("\nROWS:")
cursor.execute("""
SELECT id, filename, substr(extracted_text, 1, 200), generated_tags, created_at
FROM documents;
""")
for row in cursor.fetchall():
    print(row)

conn.close()
