from gettext import find
import sqlite3
from playerModels import Inn
from random import randint

def newInn():
    con = sqlite3.connect("assets/db/inns.db")
    cur = con.cursor()

    inn = Inn()
    choice = "N"
    while choice == "N" or choice == "n":
        ownerInput = input("\nEnter the innkeeper's name:\n")
        cur.execute("""SELECT EXISTS(SELECT * FROM inns WHERE innOwner = ?)""", (ownerInput,))
        ownerList = cur.fetchall()
        if ownerList[0][0]:
            print("\nThat owner already exists!\n")
            choice = "N"
        else:
            inn.setOwner(ownerInput)
            inn.setName(input("\nName your inn:\n"))
            inn.setCustomerMax(randint(10, 15))
            inn.setWealth(randint(2, 5) * 1000)
            inn.printInn()
            choice = input("\nKeep this inn? Y/N\n")

    newInn = """INSERT INTO inns VALUES (?, ?, ?, ?);"""
    cur.execute(newInn, (inn.getOwner(), inn.getName(), inn.getCustomerMax(), inn.getWealth()))
    con.commit()

    pullActors = """SELECT * FROM actors WHERE innOwner IS NULL ORDER BY RANDOM() LIMIT ?"""
    cur.execute(pullActors, (inn.getCustomerMax(),))
    con.commit()

    actorMod = """UPDATE actors SET innOwner = ? WHERE actorID = ?"""
    patrons = cur.fetchall()
    for row in patrons:
        cur.execute(actorMod, (inn.getOwner(), row[0]))

    con.commit()
    con.close()
    return inn

if __name__ == "__main__":
    inn = newInn()
    inn.printInn()
    inn.printCustomers()