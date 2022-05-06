import sqlite3
from playerModels import Inn
from playerModels import Actor

def loadInn():
    con = sqlite3.connect("assets/db/inns.db")
    cur = con.cursor()

    listInns = """SELECT * FROM inns"""
    cur.execute(listInns)
    innList = cur.fetchall()
    for inn in innList:
        print(inn[1])
    con.commit()

    innOwner = input("\nEnter the name of an Innkeeper:\n")

    findInn = """SELECT * FROM inns WHERE innOwner = ?;"""
    cur.execute(findInn, (innOwner,))

    innRow = cur.fetchone()
    inn = Inn(innRow[0], innRow[1], innRow[2], innRow[3])

    con.commit()
    con.close()
    
    return inn

# def saveInn(inn):
#     con = sqlite3.connect("assets/db/inns.db")
#     cur = con.cursor()

#     saveInn = """UPDATE inns SET innLedger = ?, innWealth = ? WHERE innOwner = ?;"""

#     cur.execute(saveInn, (inn.getCustomerMax(), inn.getWealth(), inn.getOwner()))
#     print("\nInn Saved!\n")
    
#     savePatrons = """UPDATE actors SET innOwner = ? WHERE innOwner = ?;"""

#     cur.execute(savePatrons, (inn.getOwner(), inn.getOwner())) # This will not work in current version
#     print("\nPatrons saved!\n")

#     con.commit()
#     con.close()

if __name__ == "__main__":
    inn = loadInn()
    inn.printInn()
    inn.printCustomers()