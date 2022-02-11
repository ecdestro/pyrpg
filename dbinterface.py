import os
import sqlite3
from playerModels import Actor
from playerModels import Inn

def createDB():
    if not os.path.exists("assets/db"):
        os.makedirs("assets/db")
    else:
        conn = sqlite3.connect("assets/db/inns.db")

        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS PATRONS")
        makePatronTable = """ CREATE TABLE PATRONS 
                        (firstName TEXT(25),
                        lastName TEXT(25),
                        innKeeper TEXT(25),
                        hitPoints INT,
                        damage INT,
                        initiative INT,
                        experience INT,
                        patronWealth INT
                        ); """

        cursor.execute(makePatronTable)
        print("PATRONS table is ready")
        cursor.execute("DROP TABLE IF EXISTS INNKEEPERS")
        makeKeeperTable = """ CREATE TABLE INNKEEPERS
                        (keeperName TEXT(25),
                        innName TEXT(150),
                        patronLevel INT,
                        innWealth INT
                        );"""
        cursor.execute(makeKeeperTable)
        print("INNKEEPERS table is ready"
        )
        conn.close()

if __name__ == "__main__":
    createDB()