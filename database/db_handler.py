import sqlite3

class DatabaseHandler:
    def __init__(self, db_name='price_tracker.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                title TEXT,
                price REAL,
                date TEXT
            )
        ''')
        self.conn.commit()

    def insert_product(self, title, price, date):
        self.cursor.execute('''
            INSERT INTO products (title, price, date)
            VALUES (?, ?, ?)
        ''', (title, price, date))
        self.conn.commit()

    def get_product_history(self, title):
        self.cursor.execute('''
            SELECT price, date FROM products
            WHERE title = ?
            ORDER BY date DESC
        ''', (title,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
