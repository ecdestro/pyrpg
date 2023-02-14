import os
import sqlite3

if not os.path.exists("assets/db"):
    os.makedirs("assets/db")
else:
    for file in os.listdir("assets/db"):
        print(file.rstrip(".db") + "\n")

def getSave():
    fileName = input("Enter the name of your innkeeper or enter ! to quit: ")
    if fileName == "!":
        quit()
    else:
        fileNameString = "assets/db/" + fileName + ".db"
        return fileName, fileNameString;

fileName, fileNameString = getSave()

if os.path.isfile(fileNameString):
    print("That save already exists! Exiting.")
    quit()
else:
    innName = input("Enter the name of your Inn: ")

def createDB():
    conn=sqlite3.connect(fileNameString)
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS inns (id INTEGER PRIMARY KEY, innKeeper text(50), innName text(150), level integer, gold integer, patronCap integer)")
    cur.execute("CREATE TABLE IF NOT EXISTS monsters (id INTEGER PRIMARY KEY, type text(50), xp integer, hp integer, gold integer, dmg integer)")
    cur.execute("CREATE TABLE IF NOT EXISTS equipment (id INTEGER PRIMARY KEY, name text(50), gold integer, hpBuff integer, dmgBuff integer, goldBuff integer)")
    cur.execute("CREATE TABLE IF NOT EXISTS patrons (id INTEGER PRIMARY KEY, name text(50), xp integer, hp integer, gold integer, dmg integer, stat integer, equip integer, FOREIGN KEY(stat) REFERENCES inns(id), FOREIGN KEY(equip) REFERENCES equipment(id))")
    conn.commit()
    conn.close()

def populateInns():
    conn=sqlite3.connect(fileNameString)
    cur=conn.cursor()
    cur.execute("""INSERT INTO inns VALUES (1, "Deceased", "NoInn", 0, 0, 65535)""")
    cur.execute("""INSERT INTO inns VALUES (2, "Business", "NoInn", 0, 0, 65535)""")
    cur.execute("""INSERT INTO inns VALUES (3, "Adventuring", "NoInn", 0, 0, 65535)""")
    cur.execute("""INSERT INTO inns VALUES (4, ?, ?, 1, 500, 6)""", (fileName, innName))
    cur.execute("""INSERT INTO inns VALUES (5, "Unassigned", "NoInn", 0, 0, 65535)""")
    conn.commit()
    conn.close()

def populateMonsters():
    conn=sqlite3.connect(fileNameString)
    cur=conn.cursor()
    cur.execute("""INSERT INTO monsters VALUES (NULL, "small goblin", 0, 10, 5, 2)""")
    cur.execute("""INSERT INTO monsters VALUES (NULL, "small kobold", 0, 12, 7, 3)""")
    cur.execute("""INSERT INTO monsters VALUES (NULL, "dragon whelp", 1, 14, 10, 4)""")
    cur.execute("""INSERT INTO monsters VALUES (NULL, "skeleton", 2, 15, 10, 4)""")
    conn.commit()
    conn.close()

def populateEquipment():
    conn=sqlite3.connect(fileNameString)
    cur=conn.cursor()
    cur.execute("""INSERT INTO equipment VALUES (NULL, "mysterious club", 1, 0, 1, 0)""")
    cur.execute("""INSERT INTO equipment VALUES (NULL, "mysterious blade", 2, 0, 3, 0)""")
    cur.execute("""INSERT INTO equipment VALUES (NULL, "mysterious mail", 2, 3, 0, 0)""")
    cur.execute("""INSERT INTO equipment VALUES (NULL, "mysterious amulet", 4, 0, 0, 10)""")
    cur.execute("""INSERT INTO equipment VALUES (NULL, "mysterious wand", 5, 0, 4, 0)""")
    conn.commit()
    conn.close()

def populatePatrons():
    conn=sqlite3.connect(fileNameString)
    cur=conn.cursor()
    patronFile = open("assets/text/names.txt","r")
    patronNames = patronFile.read().splitlines()
    for patronName in patronNames:
        cur.execute("""INSERT INTO patrons VALUES (NULL, ?, 1, 20, 50, 10, 5, 0)""", (patronName,))
    conn.commit()
    conn.close()

createDB()
populateInns()
populateMonsters()
populateEquipment()
populatePatrons()