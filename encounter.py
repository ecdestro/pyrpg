import sqlite3
from playerModels import Actor
from playerModels import Inn
from encounterCombat import combat

def encounter(inn):
    con = sqlite3.connect("assets/db/inns.db")
    cur = con.cursor()

    enemyEncounter = """SELECT * FROM encounters WHERE statusName = "Alive" ORDER BY RANDOM() LIMIT ?;"""
    cur.execute(enemyEncounter, (1,))
    enemyRow = cur.fetchone()
    enemy = Actor(enemyRow[0], enemyRow[1], enemyRow[2], enemyRow[3], enemyRow[4], enemyRow[5], enemyRow[6])
    enemy.printActor()
    
    playerDraw = """SELECT * FROM actors WHERE innKeeper = ? ORDER BY RANDOM() LIMIT ?;"""
    cur.execute(playerDraw, (inn.getOwner(),1))
    playerRow = cur.fetchone()
    player = Actor(playerRow[1] + " " + playerRow[2], playerRow[3], playerRow[4], playerRow[5], playerRow[6], playerRow[7], playerRow[8])
    player.printActor()

    victor, defeated = combat(player, enemy)
    victor.printActor()
    defeated.printActor()
    if victor.getKeeper() == inn.getOwner():
        playerInsert = """UPDATE actors SET hitPoints = ?, expLevel = ?, goldHeld = ? WHERE actorID = ?;"""
        cur.execute(playerInsert, (victor.getHP(), victor.getExp(), victor.getWealth(), playerDraw[0])) # victor.getExp() not getting added to expLevel, not sure why
        enemyInsert = """UPDATE encounters SET statusName = ?, encounterHP = 0, goldHeld = ? WHERE encounterName = ?;"""
        cur.execute(enemyInsert, (defeated.getKeeper(), defeated.getWealth(), defeated.getName()))
    else:
        playerInsert = """UPDATE actors SET hitPoints = 0, expLevel = ?, goldHeld = ? WHERE actorID = ?;"""
        cur.execute(playerInsert, (defeated.getExp(), defeated.getWealth(), playerDraw[0]))
        enemyInsert = """UPDATE encounters SET statusName = ?, encounterHP = ?, goldHeld = ? WHERE encounterName = ?;"""
        cur.execute(enemyInsert, (victor.getKeeper(), victor.getHP(), victor.getWealth(), victor.getName()))

    con.commit()
    con.close()

if __name__ == "__main__":
    inn = Inn("Destro", "The Broken Tusk", 10, 3000)
    encounter(inn)