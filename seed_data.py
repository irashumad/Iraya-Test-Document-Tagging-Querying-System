
import sqlite3
from datetime import datetime

def create_connection():
    return sqlite3.connect("documents.db")

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

    conn.commit()
    conn.close()

def fetch_latest_document():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT filename, extracted_text, generated_tags, created_at
    FROM documents
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()
    return row

def update_tags(filename, tags):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE documents
    SET generated_tags = ?
    WHERE id = (
        SELECT id FROM documents
        WHERE filename = ?
        ORDER BY id DESC
        LIMIT 1
    )
    """, (tags, filename))

    conn.commit()
    conn.close()

def document_exists(filename):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 1 FROM documents
    WHERE filename = ?
    LIMIT 1
    """, (filename,))

    row = cursor.fetchone()
    conn.close()

    return row is not None