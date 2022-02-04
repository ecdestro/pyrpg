import os
from actor import Actor

def saveFile(player):
    if player.getName() == "":
        print("Nothing to save!")
    else:
        with open(r"players/" + player.getName(), "w") as playerFile:
            playerFile.write(player.getName() + " " + str(player.getHP()) + " " + str(player.getDmg()) + " " + str(player.getInit()))
            player.printActor()
            print(player.getName() + " saved!")