import os
import random
from actor import Actor
from inn import Inn

def createChar(innFile):
    with open (r"assets/text/names", "r") as merdenoms:
        names = merdenoms.read().split()

    player = Actor()
    custMax = innFile.getCustomerMax()

    for customers in range(1, custMax):
        player.setName(random.choice(names))
        player.setHP(random.randint(30, 45))
        player.setDmg(random.randint(5, 10))
        player.setInit(random.randint(5, 10))
        player.setExp(random.randint(1, 10))
        player.setWealth(random.randint(10, 100))
        player.printActor()
        
        with open(r"inns/" + innFile.getOwner() + r"/" + player.getName(), "w") as playerFile:
            playerFile.write(player.getName() + " " + str(player.getHP()) + " " + str(player.getDmg()) + " " + str(player.getInit()) + " " + str(player.getExp()) + " " + str(player.getWealth()))

if __name__ == "__main__":
    inn = Inn("Destro",6,5000)