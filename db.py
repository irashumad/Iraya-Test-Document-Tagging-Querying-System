import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "documents.db")

def create_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        extracted_text TEXT,
        generated_tags TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_document(filename, extracted_text, generated_tags=""):
    conn = create_connection()
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO documents (filename, extracted_text, generated_tags, created_at)
    VALUES (?, ?, ?, ?)
    """, (filename, extracted_text, generated_tags, created_at))

    doc_id = cursor.lastrowid

    conn.commit()
    conn.close()
    return doc_id

def update_tags_by_id(doc_id, tags):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE documents
    SET generated_tags = ?
    WHERE id = ?
    """, (tags, doc_id))

    conn.commit()
    conn.close()

def fetch_latest_document():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, filename, extracted_text, generated_tags, created_at
    FROM documents
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()
    return row
