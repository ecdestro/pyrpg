import os
import sqlite3
from random import randint
from classes import *

for file in os.listdir("assets/db"):
    print("Saved Innkeepers:")
    print(file.rstrip(".db") + "\n")

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
    cur.execute("""SELECT * FROM patrons WHERE stat = 5 ORDER BY RANDOM()""")
    patronTup = cur.fetchone()
    conn.commit()
    conn.close()
    patron = Patron(patronTup[0], patronTup[1], patronTup[2], patronTup[3], patronTup[4], patronTup[5], patronTup[6], patronTup[7])
    print(patron)
    return patron

def pullMonster():
    conn=sqlite3.connect(fileNameString)
    cur=conn.cursor()
    cur.execute("""SELECT * FROM monsters ORDER BY RANDOM()""")
    monsterTup = cur.fetchone()
    conn.commit()
    conn.close()
    monster = Monster(monsterTup[0], monsterTup[1], monsterTup[2], monsterTup[3], monsterTup[4], monsterTup[5])
    print(monster)
    return monster

fighter = pullPatron()
monster = pullMonster()

def hitChance():
    return randint(0, 1)

def encounter(fighter, monster):
    if fighter.xp >= monster.level:
        while fighter.hp > 0 and monster.hp > 0:
            monster.hp = (monster.hp - fighter.dmg * hitChance())
            if monster.hp <= 0:
                pass
            else:
                fighter.hp = (fighter.hp - monster.dmg * hitChance())
    else:
        while fighter.hp > 0 and monster.hp > 0:
            fighter.hp = (fighter.hp - monster.dmg * hitChance())
            if fighter.hp <= 0:
                pass
            else:
                monster.hp = (monster.hp - fighter.dmg * hitChance())
    
    print(fighter.hp)
    print(monster.hp)

    if fighter.hp > 0 and monster.hp <= 0:
        victor = fighter
        return victor
    elif monster.hp > 0 and fighter.hp <= 0:
        victor = monster
        return victor
victor = encounter(fighter, monster)
print(victor.name)