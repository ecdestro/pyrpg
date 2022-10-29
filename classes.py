# 
# classes.py: a definition of Inn objects, patron objects, monster objects, and equipment objects
# Author: ecdestro
# Date: 29 Oct 2022
#

# Inn: inn(id, innKeeper, level, gold, patronCap)
#   id - index in Inn table of the database
#   innKeeper - name of the save file
#   innName - name of the Inn
#   level - prestige level of the inn (used to attach businesses)
#   gold - wealth of the inn
#   patronCap - capacity of the inn for overnight stays

class Inn:
    def __init__(self, id = 0, innKeeper = "", innName = "", level = 0, gold = 0, patronCap = 0) -> None:
        self.id = id
        self.innKeeper = innKeeper
        self.innName = innName
        self.level = level
        self.gold = gold
        self.patronCap = patronCap

    def setID(self, id):
        self.id = id

    def getID(self) -> int:
        return self.id

    def setKeeper(self, innKeeper):
        self.innKeeper = innKeeper

    def getKeeper(self) -> str:
        return self.innKeeper

    def setName(self, innName):
        self.innName = innName

    def getName(self) -> str:
        return self.innName

    def setXp(self, level):
        self.level = level
    
    def getXp(self) -> int:
        return self.level
    
    def setGold(self, gold):
        self.gold = gold
    
    def getGold(self) -> int:
        return self.gold

    def setPatronCap(self, patronCap):
        self.patronCap = patronCap
    
    def getPatronCap(self) -> int:
        return self.patronCap

    def print(self):
        print(str(self.getID()) + " " + str(self.getKeeper()) + " " + str(self.getName()) + " " + str(self.getXp()) + " " + str(self.getGold()) + " " + str(self.getPatronCap))

# Patron: patron(id, name, xp, hp, gold, dmg, stat, equipment)
#   id - index in the patrons table
#   name - name of the patron
#   xp - experience level of the patron (modifies effects of initiative)
#   hp - hitpoints (health)
#   gold - wealth held by patron
#   dmg - base damage
#   stat - status (unknown, away (business), away (adventure), boarded, deceased)
#   equip - index of the piece of equipment from the equipment table

class Patron:
    def __init__(self, id = 0, name = "", xp = 0, hp = 0, gold = 0, dmg = 0, stat = 0, equip = 0) -> None:
        self.id = id
        self.name = name
        self.xp = xp
        self.hp = hp
        self.gold = gold
        self.dmg = dmg

    def setID(self, id):
        self.id = id

    def getID(self) -> int:
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self) -> str:
        return self.name

    def setXp(self, xp):
        self.xp = xp
    
    def getXp(self) -> int:
        return self.xp

    def setHp(self, hp):
        self.hp = hp

    def getHp(self) -> int:
        return self.hp
    
    def setGold(self, gold):
        self.gold = gold
    
    def getGold(self) -> int:
        return self.gold

    def setDmg(self, dmg):
        self.dmg = dmg
    
    def getDmg(self) -> int:
        return self.dmg

    def print(self):
        print(str(self.getID()) + " " + str(self.getName()) + " " + str(self.getXp()) + " " + str(self.getHp()) + " " + str(self.getGold()) + " " + str(self.getDmg()))

class Equipment:
    def __init__(self, id = 0, name = "", gold = 0, hpBuff = 0, dmgBuff = 0) -> None:
        self.id = id
        self.name = name
        self.gold = gold
        self.hpBuff = hpBuff
        self.dmgBuff = dmgBuff

    def setID(self, id):
        self.id = id

    def getID(self) -> int:
        return self.id
    
    def setName(self, name):
        self.name = name
    
    def getName(self) -> str:
        return self.name
    
    def setGold(self, gold):
        self.gold = gold

    def getGold(self) -> int:
        return self.gold
    
    def setHpBuff(self, hpBuff):
        self.hpBuff = hpBuff
    
    def getHpBuff(self) -> int:
        return self.hpBuff

    def setDmgBuff(self, dmgBuff):
        self.dmgBuff = dmgBuff
    
    def getDmgBuff(self) -> int:
        return self.dmgBuff

    def print(self):
        print(str(self.getID()) + " " + str(self.getName()) + " " + str(self.getGold()) + " " + str(self.getHpBuff()) + " " + str(self.getDmgBuff()))

class Monster:
    def __init__(self, id = 0, type = "", level = 0, gold = 0, dmg = 0) -> None:
        self.id = id
        self.type = type
        self.level = level
        self.gold = gold
        self.dmg = dmg

    def setID(self, id):
        self.id = id

    def getID(self) -> int:
        return self.id

    def setType(self, type):
        self.type = type

    def getType(self) -> str:
        return self.type

    def setXp(self, level):
        self.level = level
    
    def getXp(self) -> int:
        return self.level
    
    def setGold(self, gold):
        self.gold = gold
    
    def getGold(self) -> int:
        return self.gold

    def setDmg(self, dmg):
        self.dmg = dmg
    
    def getDmg(self) -> int:
        return self.dmg
    
    def print(self):
        print(str(self.getID()) + " " + str(self.getType()) + " " + str(self.getXp()) + " " + str(self.getGold()) + " " + str(self.getDmg()))