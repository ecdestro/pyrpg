import os
from actor import Actor
from create import createChar

def loadFile():
    if not os.path.exists("players"):
        os.makedirs("players")
        player = createChar()
        return player
    elif not os.listdir("players"):
        player = createChar()
        return player
    else:
        for fileName in os.listdir("players"):
                print(fileName)
        fName = input("Choose a character\n")
        with open(r"players/" + fName, "r") as playerFile:
            playerString = playerFile.read().split()
            player = Actor(playerString[0], int(playerString[1]), int(playerString[2]), int(playerString[3]))
            player.printActor()
            return player
