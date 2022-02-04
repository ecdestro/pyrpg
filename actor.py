class Actor:
    def __init__(self, name = "", hitPoints = 0, damage = 0, initiative = 0):
        self.name = name
        self.hitPoints = hitPoints
        self.damage = damage
        self.initiative = initiative
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setHP(self, hitPoints):
        self.hitPoints = hitPoints
    def getHP(self):
        return self.hitPoints
    def setDmg(self, damage):
        self.damage = damage
    def getDmg(self):
        return self.damage
    def setInit(self, initiative):
        self.initiative = initiative
    def getInit(self):
        return self.initiative
    def printActor(self):
        print("Name = " + self.getName())
        print("HP   = " + str(self.getHP()))
        print("Dmg  = " + str(self.getDmg()))
        print("Init = " + str(self.getInit()))