import sqlite3

def connect():
    """
    initial connect database
    
    """
    return sqlite3.connect("library.db")


def create_table(conn):

    """
    all required tables are created here
    """
    cursor= conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_name TEXT NOT NUll,
            available_quantity INTEGER NOT NULL CHECK (available_quantity>=0)
        )
    """
    )
    cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS student(
            sid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS lend_record(
            id INTEGER PRIMARY KEY,
            book_id INTEGER NOT NULL,
            student_id INTEGER NOT NULL,
            return_status BOOLEAN DEFAULT 0,
            FOREIGN KEY (book_id) REFERENCES books(id),
            FOREIGN KEY (student_id) REFERENCES student(sid)
        )
    """
    )
    conn.commit()

