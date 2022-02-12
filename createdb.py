import os, sqlite3, csv
from random import randint

def createTables():
        if not os.path.exists("assets/db"):
                os.makedirs("assets/db")
        else:
                con = sqlite3.connect("assets/db/inns.db")
                cur = con.cursor()

                innTable = """CREATE TABLE IF NOT EXISTS inns
                        (innOwner TEXT(25),
                        innName TEXT(150),
                        innLedger INT,
                        innWealth INT
                        ); """

                patronTable = """CREATE TABLE IF NOT EXISTS actors 
                        (actorID INTEGER PRIMARY KEY AUTOINCREMENT,
                        firstName TEXT(25),
                        lastName TEXT(25),
                        innKeeper TEXT(25) NULL,
                        hitPoints INT,
                        baseDamage INT,
                        initiative INT,
                        expLevel INT,
                        goldHeld INT
                        );"""

                encountersTable = """CREATE TABLE IF NOT EXISTS encounters
                                (encounterName TEXT(25),
                                statusName TEXT(25),
                                encounterHP INT,
                                encounterDMG INT,
                                encounterInit INT,
                                expLevel INT,
                                goldHeld INT
                                );"""

                cur.execute(innTable) # Create inns table
                cur.execute(patronTable) # Create patrons table
                cur.execute(encountersTable) # Create encounters table

                con.commit()
                con.close()

def popultePatrons():
        con = sqlite3.connect("assets/db/inns.db")
        cur = con.cursor()

        firstNames = []
        lastNames = []
        with open(r"assets/text/names","r") as inFile:
                reader = csv.reader(inFile)
                for row in reader:
                        firstNames.append(row[0])
                        lastNames.append(row[1])

        i = 0
        for x in firstNames:
                sendToDB = [x, lastNames[i], randint(30, 50), randint(5, 10), randint(5, 10), 0, randint(5, 50)]
                cur.execute("INSERT INTO actors (firstName, lastName, hitPoints, baseDamage, initiative, expLevel, goldHeld) VALUES (?, ?, ?, ?, ?, ?, ?);", sendToDB)
                i += 1

        con.commit()
        con.close()

def populateEncounters():
        con = sqlite3.connect("assets/db/inns.db")
        cur = con.cursor()

        fNames = []
        lnames = []
        with open(r"assets/text/names","r") as inFile:
                reader = csv.reader(inFile)
                for row in reader:
                        fNames.append(row[0])
                        fNames.append(row[1])
        
        for x in fNames:
                sendToDB = [x, "Alive", randint(25, 40), randint(3, 8), randint(5, 10), 1, randint(10, 50)]
                cur.execute("INSERT INTO encounters (encounterName, statusName, encounterHP, encounterDMG, encounterInit, expLevel, goldHeld) VALUES (?, ?, ?, ?, ?, ?, ?);", sendToDB)

        con.commit()
        con.close()

if __name__ == "__main__":
        createTables()
        popultePatrons()
        populateEncounters()