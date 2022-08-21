import sqlite3

def connect():
    conn=sqlite3.connect("city.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS patrons (id INTEGER PRIMARY KEY, name text, exp integer, hp integer, gold integer)")
    conn.commit()
    conn.close()

def insert(name, exp, hp, gold):
    conn=sqlite3.connect("city.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO patrons VALUES (NULL,?,?,?,?)",(name, exp, hp, gold))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("city.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM patrons")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name="", exp="", hp="", gold=""):
    conn=sqlite3.connect("city.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM patrons WHERE name=? OR exp=? OR hp=? OR gold=?",(name, exp, hp, gold))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("city.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM patrons WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, name, exp, hp, gold):
    conn=sqlite3.connect("city.db")
    cur=conn.cursor()
    cur.execute("UPDATE patrons SET name=?, exp=?, hp=?, gold=? WHERE id=?",(name, exp, hp, gold, id))
    conn.commit()
    conn.close()

connect()