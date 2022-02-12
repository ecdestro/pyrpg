import sqlite3
from playerModels import Actor
from playerModels import Inn
from populateInn import populate

def saveInn(inn):
    con = sqlite3.connect("assets/db/inns.db")
    cur = con.cursor()

    saveInn = """UPDATE inns SET innLedger = ?, innWealth = ? WHERE innOwner = ?;"""

    cur.execute(saveInn, (inn.getCustomerMax(), inn.getWealth(), inn.getOwner()))
    print("\nInn Saved!\n")
    
    savePatrons = """UPDATE actors SET innKeeper = ? WHERE innKeeper = ?;"""

    cur.execute(savePatrons, (inn.getOwner(), inn.getOwner()))
    print("\nPatrons saved!\n")

    con.commit()
    con.close()