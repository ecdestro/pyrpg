import sqlite3

def createDB():
    fileName = input("Enter the name of your innkeeper: ")
    fileNameString = fileName + ".db"
    conn=sqlite3.connect(fileNameString)
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS patrons (id INTEGER PRIMARY KEY, name text(50), xp integer, hp integer, gold integer, dmg integer)")
    cur.execute("CREATE TABLE IF NOT EXISTS monsters (id INTEGER PRIMARY KEY, type text(50), xp integer, gold integer, dmg integer)")
    cur.execute("CREATE TABLE IF NOT EXISTS equipment (id INTEGER PRIMARY KEY, name text(50), gold integer, hpBuff integer, dmgBuff integer)")
    conn.commit()
    conn.close()

createDB()