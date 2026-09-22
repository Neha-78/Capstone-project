"""
database.py
SQLite CRUD layer for the Book capstone project (OOP style,
same pattern as O01_basics_sqllite.py -> EmployeeDatabase).
"""

import sqlite3


class BookDatabaseManager:
    def __init__(self, db_name="books.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                price REAL,
                                in_stock TEXT,
                                rating INTEGER)''')
        self.conn.commit()

# ---------- CREATE ----------
    def insert_book(self, title, price, in_stock, rating):
        self.cursor.execute(
            "INSERT INTO books (title, price, in_stock, rating) VALUES (?,?,?,?)",
            (title, price, in_stock, rating))
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_many(self, books):
        self.cursor.executemany(
            "INSERT INTO books (title, price, in_stock, rating) VALUES (?,?,?,?)",
             books)
        self.conn.commit()

# ---------- READ ----------
    def get_all_books(self):
        self.cursor.execute("SELECT id, title, price, in_stock, rating FROM books")
        return self.cursor.fetchall()

    def get_book_by_id(self, book_id):
        self.cursor.execute(
            "SELECT id, title, price, in_stock, rating FROM books WHERE id=?", (book_id,))
        return self.cursor.fetchone()

# ---------- UPDATE ----------
    def update_book(self, book_id, title=None, price=None, in_stock=None, rating=None):
        if title is not None:
            self.cursor.execute("UPDATE books SET title=? WHERE id=?", (title, book_id))
        if price is not None:
            self.cursor.execute("UPDATE books SET price=? WHERE id=?", (price, book_id))
        if in_stock is not None:
            self.cursor.execute("UPDATE books SET in_stock=? WHERE id=?", (in_stock, book_id))
        if rating is not None:
            self.cursor.execute("UPDATE books SET rating=? WHERE id=?", (rating, book_id))
        self.conn.commit()

# ---------- DELETE ----------
    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()