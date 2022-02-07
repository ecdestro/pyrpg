import random

class Actor:
    def __init__(self, name = "", hitPoints = 0, damage = 0, initiative = 0, experience = 0, wealth = 0):
        self.name = name
        self.hitPoints = hitPoints
        self.damage = damage
        self.initiative = initiative
        self.experience = experience
        self.wealth = wealth

    # def __iter__(self):
    #     self.index = 0
    #     return self

    # def __next__(self):
    #     self.index += 1
    #     return self

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
        print("HP   = " + str(self.getHP()))
        print("Dmg  = " + str(self.getDmg()))
        print("Init = " + str(self.getInit()))
        print("Exp  = " + str(self.getExp()))
        print("Gold = " + str(self.getWealth()))

class Inn:
    def __init__(self, owner = "", customerMax = 0, wealth = 0):
        self.owner = owner
        self.customerMax = customerMax
        self.wealth = wealth
        self.customer = Actor()
        self.customerLedger = []

    def setOwner(self, owner):
        self.owner = owner
    def getOwner(self):
        return self.owner

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
        print("Max Customers = " + str(self.getCustomerMax()))
        print("Cash on Hand = " + str(self.getWealth()) + "\n")

    def printCustomers(self):
        if len(self.customerLedger) > 0:
            for x in self.customerLedger:
                x.printActor()
        else:
            print("No customers\n")

if __name__ == "__main__":
    with open(r"assets/text/names", "r") as merDeNoms:
        name = merDeNoms.read().split()

    inn = Inn("Destro",4,5000)

    i = 0
    while i < inn.getCustomerMax():
        customer = Actor(random.choice(name), random.randint(35, 50), random.randint(5, 10), random.randint(5, 10), 0, random.randint(10, 50))
        inn.addCustomer(customer)
        i += 1

    inn.printInn()
    for customer in inn.getLedger():
        customer.printActor()
    