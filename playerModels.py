import sqlite3

class Actor:
    def __init__(self, name = "", keeper = "", hitPoints = 0, damage = 0, initiative = 0, experience = 0, wealth = 0):
        self.name = name
        self.keeper = keeper
        self.hitPoints = hitPoints
        self.damage = damage
        self.initiative = initiative
        self.experience = experience
        self.wealth = wealth

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setKeeper(self, keeper):
        self.keeper = keeper
    def getKeeper(self):
        return self.keeper

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

    def setExp(self, experience):
        self.experience = experience
    def getExp(self):
        return self.experience

    def setWealth(self, wealth):
        self.wealth = wealth
    def getWealth(self):
        return self.wealth

    def printActor(self):
        print("Name = " + self.getName())
        print("Keep = " + self.getKeeper())
        print("HP   = " + str(self.getHP()))
        print("Dmg  = " + str(self.getDmg()))
        print("Init = " + str(self.getInit()))
        print("Exp  = " + str(self.getExp()))
        print("Gold = " + str(self.getWealth()))

class Inn:
    def __init__(self, owner = "", innName = "", customerMax = 0, wealth = 0):
        self.owner = owner
        self.innName = innName
        self.customerMax = customerMax
        self.wealth = wealth
        self.customer = Actor()
        self.customerLedger = []

    def setOwner(self, owner):
        self.owner = owner
    def getOwner(self):
        return self.owner

    def setName(self, innName):
        self.innName = innName
    def getName(self):
        return self.innName

    def setCustomerMax(self, customerMax):
        self.customerMax = customerMax
    def getCustomerMax(self):
        return self.customerMax

    def setWealth(self, wealth):
        self.wealth = wealth
    def getWealth(self):
        return self.wealth

    def addCustomer(self, customer):
        self.customerLedger.append(customer)
    def removeCustomer(self, customer):
        self.customerLedger.remove(customer)
    def getCustomers(self):
        for self.customer in self.customerLedger:
            return self.customer
    def getLedger(self):
        return self.customerLedger 

    def printInn(self):
        print("Owner = " + self.getOwner())
        print("Name = " +self.getName())
        print("Max Customers = " + str(self.getCustomerMax()))
        print("Cash on Hand = " + str(self.getWealth()) + "\n")

    def printCustomers(self):
        if self.getCustomerMax() > 0:
            con = sqlite3.connect("assets/db/inns.db")
            cur = con.cursor()

            pullActors = """SELECT * FROM actors WHERE innKeeper = ?;"""
            cur.execute(pullActors, (self.getOwner(),))
            patrons = cur.fetchall()
            for patron in patrons:
                print(patron)

            con.commit()
            con.close()
        else:
            print("No customers\n")