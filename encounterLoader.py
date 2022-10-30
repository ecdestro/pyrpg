import os
import sqlite3
from classes import *

fileName = input("Enter an Innkeeper's name: ")
fileNameString = "assets/db/" + fileName + ".db"
if os.path.isfile(fileNameString):
    pass
else:
    print("That file does not exist!")
    quit()

def pullPatron():
    conn=sqlite3.connect(fileNameString)
    cur=conn.cursor()
    cur.execute("""SELECT * FROM patrons WHERE stat = 5""")
    patronTup = cur.fetchone()
    conn.commit()
    conn.close()
    patron = Patron(patronTup[0], patronTup[1], patronTup[2], patronTup[3], patronTup[4], patronTup[5], patronTup[6], patronTup[7])
    return patron

def pullMonster():
    conn=sqlite3.connect(fileNameString)
    cur=conn.cursor()
    cur.execute("""SELECT * FROM monsters""")
    monsterTup = cur.fetchone()
    conn.commit()
    conn.close()
    monster = Monster(monsterTup[0], monsterTup[1], monsterTup[2], monsterTup[3], monsterTup[4], monsterTup[5])
    return monster

fighter = pullPatron()
monster = pullMonster()

def encounter(fighter, monster):
    if fighter.getXp() == monster.getXp():
        print("Tied for Initiative!")
        print(fighter.getName() + " goes first!")
        while fighter.getHP() > 0 and monster.getHp() > 0:
            monster.setHp(monster.getHp() - fighter.getDmg())
            fighter.setHP(fighter.getHp() - monster.getDmg())
    elif fighter.getXp() > monster.getXp():
        while fighter.getHp() > 0 and monster.getHp() > 0:
            monster.setHp(monster.getHp() - fighter.getDmg())
            fighter.setHp(fighter.getHp() - monster.getDmg())
    elif monster.getXp() > fighter.getXp():
        while monster.getHp() > 0 and fighter.getHp() > 0:
            fighter.setHp(fighter.getHp() - monster.getDmg())
            monster.setHp(monster.getHp() - fighter.getDmg())
    
    print(fighter.getHp())
    print(monster.getHp())

    if fighter.getHp() > 0 and monster.getHp() <= 0:
        victor = fighter
        return victor
    elif monster.getHp() > 0 and fighter.getHp() <= 0:
        victor = monster
        return victor

victor = encounter(fighter, monster)
print(victor.getName())