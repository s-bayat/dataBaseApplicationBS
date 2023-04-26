import sqlite3


def connect():
    conn = sqlite3.connect("venv/books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("venv/books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("venv/books.db")
    cur = conn.cursor()
    cur.execute("select * from book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("venv/books.db")
    cur = conn.cursor()
    cur.execute("select * from book where title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("venv/books.db")
    cur = conn.cursor()
    cur.execute("delete from book where id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("venv/books.db")
    cur = conn.cursor()
    cur.execute("update book set title=? ,author=?, year=?, isbn=? where id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()
# insert("csharp", "shakoori", 2023, 5475968)
update(4, "new book", "sajjad", 2021, 784587)
print(view())
