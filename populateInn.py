import sqlite3
from playerModels import Actor
from playerModels import Inn

def populate(inn):
    con = sqlite3.connect("assets/db/inns.db")
    cur = con.cursor()

    cur.execute("""SELECT * FROM actors WHERE innOwner IS NULL ORDER BY RANDOM() LIMIT ?""", (inn.getCustomerMax(),))

    actors = cur.fetchall()
    for row in actors:
        cur.execute("""UPDATE actors SET innOwner = ? WHERE actorID = ?""", (inn.getOwner(),row[0]))
    
    con.commit()
    con.close()

if __name__ == "__main__":
    inn = Inn("Destro", "The Broken Tusk", 5, 5000)
    populate(inn)
    inn.printInn()
    inn.printCustomers()