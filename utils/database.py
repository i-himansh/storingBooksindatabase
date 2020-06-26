from .database_connection import DatabaseConnection

def create_book_table():
    with DatabaseConnection('data.db')as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')



def add_books(name, author):
    with DatabaseConnection('data.db')as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name,author))



def list_all_books():
    with DatabaseConnection('data.db')as connection:
        cursor= connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = [{"name": row[0],"author": row[1], "read" : row[2]} for row in cursor.fetchall()]
    return books



def read_books(name):
    with DatabaseConnection('data.db')as connection:

        cursor = connection.cursor()

        cursor.execute("UPDATE books SET read = 1 WHERE name=? ", (name, ))



def delete_books(name):
    with DatabaseConnection('data.db')as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM books WHERE name=? ", (name,))


