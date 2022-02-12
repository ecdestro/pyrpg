import sqlite3
from playerModels import Inn

def loadInn():
    con = sqlite3.connect("assets/db/inns.db")
    cur = con.cursor()

    listInns = """SELECT * FROM inns"""
    cur.execute(listInns)
    innList = cur.fetchall()
    for inn in innList:
        print(inn[0])
    con.commit()

    innOwner = input("\nEnter the name of an Innkeeper:\n")

    findInn = """SELECT * FROM inns WHERE innOwner = ?;"""
    cur.execute(findInn, (innOwner,))

    innRow = cur.fetchone()
    inn = Inn(innRow[0], innRow[1], innRow[2], innRow[3])
    return inn

if __name__ == "__main__":
    inn = loadInn()
    inn.printInn()
    inn.printCustomers()