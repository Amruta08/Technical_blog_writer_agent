import sqlite3

DB_NAME = "blogs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS blogs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        filename TEXT,
        markdown TEXT
    )
    """)
    
    conn.commit()
    conn.close()


def save_blog(title, filename, markdown):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        """
        INSERT INTO blogs 
        (title, filename, markdown)
        VALUES (?, ?, ?)
        """,
        (title, filename, markdown)
    )
    
    conn.commit()
    conn.close()
    
    
def get_all_blogs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT filename FROM blogs
        ORDER BY id DESC
        """)
    
    rows = cursor.fetchall()
    conn.close()
    
    return [row[0] for row in rows]


def get_blog_by_filename(filename):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT markdown FROM blogs 
        WHERE filename=?
        """,
        (filename,)
    )
    
    row = cursor.fetchone()
    conn.close()
    
    return row[0] if row else None