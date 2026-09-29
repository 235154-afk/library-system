import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
);
INSERT INTO books VALUES
(1, 'Data Science Basics', 'Technology', 1450, 10),
(2, 'Clean Code', 'Technology', 1200, 7),
(3, 'The Silent Patient', 'Fiction', 1350, 2),
(4, 'The Alchemist', 'Fiction', 800, 12),
(5, '1984', 'Fiction', 700, 3),
(6, 'Python Crash Course', 'Technology', 900, 8),
(7, 'Atomic Habits', 'Self-Help', 850, 15),
(8, 'Sapiens', 'History', 1100, 4);
""")
conn.commit()
conn.close()
print("Database created.")