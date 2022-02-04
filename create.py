import os
from random import randint
from actor import Actor

if not os.path.exists("players"):
    os.makedirs("players")

def createChar():
    player = Actor()
    fName = input("Name your character\n")
    keepActor = "n"

    while keepActor == "N" or keepActor == "n":
        player.setName(fName)
        player.setHP(randint(30, 45))
        player.setDmg(randint(5, 10))
        player.setInit(randint(5, 10))
        player.printActor()
        keepActor = input("Keep this character? Y/N\n")
    
    with open(r"players/" + fName, "w") as playerFile:
        playerFile.write(player.getName() + " " + str(player.getHP()) + " " + str(player.getDmg()) + " " + str(player.getInit()))

    return player