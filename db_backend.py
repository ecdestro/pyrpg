import sqlite3
import createdb as createdb

file = createdb.connect()

def insert(name, xp, hp, gold, dmg):
    conn=sqlite3.connect(file)
    cur=conn.cursor()
    cur.execute("INSERT INTO patrons VALUES (NULL,?,?,?,?,?)",(name, xp, hp, gold, dmg))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect(file)
    cur=conn.cursor()
    cur.execute("SELECT * FROM patrons")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name="", xp="", hp="", gold="", dmg=""):
    conn=sqlite3.connect(file)
    cur=conn.cursor()
    cur.execute("SELECT * FROM patrons WHERE name=? OR xp=? OR hp=? OR gold=? OR dmg=?",(name, xp, hp, gold, dmg))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect(file)
    cur=conn.cursor()
    cur.execute("DELETE FROM patrons WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, name, xp, hp, gold, dmg):
    conn=sqlite3.connect(file)
    cur=conn.cursor()
    cur.execute("UPDATE patrons SET name=?, xp=?, hp=?, gold=?, dmg=? WHERE id=?",(name, xp, hp, gold, dmg, id))
    conn.commit()
    conn.close()

# connect()