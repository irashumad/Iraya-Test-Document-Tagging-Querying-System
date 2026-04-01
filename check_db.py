
import sqlite3

conn = sqlite3.connect("documents.db")
cursor = conn.cursor()

print("\nTABLES:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

print("\nSCHEMA:")
cursor.execute("PRAGMA table_info(documents);")
for row in cursor.fetchall():
    print(row)

print("\nROWS:")
cursor.execute("SELECT id, filename, generated_tags, created_at FROM documents;")
for row in cursor.fetchall():
    print(row)

conn.close()