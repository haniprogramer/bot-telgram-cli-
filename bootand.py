import sqlite3

def connect():

    conn = sqlite3.connect('bookbot.db')
    cur = conn.cursor()
    cur.execute(' CREATE TABLE IF NOT EXISTS book ( id INTEGER PRIMARY KEY ,dialog text ,name text )')
    conn.commit()
    conn.close()


def insert(dialog ,name):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO book VALUES(NULL,?,?)',( dialog,name))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('bookbot.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()
    conn.close()
    return rows


def search( dialog='',name=''):
    conn = sqlite3.connect('bookbot.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book WHERE  dialog=? OR name=? ' (dialog,name))
    rows = cur.fetchall()
    conn.close()
    return rows


# def delet(id):
#     conn = sqlite3.connect('books.db')
#     cur = conn.cursor()
#     cur.execute('DELETE FROM book WHERE id=?', (id,))
#     conn.commit()
#     conn.close()



connect()