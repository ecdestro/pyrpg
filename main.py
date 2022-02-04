import os
from random import randint
from actor import Actor
from combat import combat
from create import createChar
from save import saveFile
from load import loadFile

player = Actor()
opponent = Actor("Enemy", randint(30, 45), randint(1, 10), randint(1, 10))
menuChoice = "1"

while menuChoice != "5":
    print("\nRPG v0.0.5\n")
    print("Current character: " + player.getName())
    print("\n\t1 - Play")
    print("\t2 - Load")
    print("\t3 - Save")
    print("\t4 - New")
    print("\t5 - Quit\n")
    menuChoice = input("Please make a selection:\n")
    if menuChoice == "1":
        if player.getName() == "":
            if not os.listdir("players"):
                player = createChar()
            else:
                player = loadFile()
        else:
            player = combat(player, opponent)
    elif menuChoice == "2":
        player = loadFile()
    elif menuChoice == "3":
        saveFile(player)
    elif menuChoice == "4":
        player = createChar()