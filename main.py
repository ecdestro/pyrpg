import os
from random import randint
from playerClasses import Inn
from playerClasses import Actor
from createInn import createInn
from loadInn import loadInn
from saveInn import saveInn

inn = Inn()

menuChoice = "1"

while menuChoice != "5":
    print("\nRPG v0.0.6\n")
    print("Current owner: " + inn.getOwner())
    print("\n\t1 - Play")
    print("\t2 - Load Inn")
    print("\t3 - Save Inn")
    print("\t4 - New Inn")
    print("\t5 - Quit\n")
    menuChoice = input("Please make a selection:\n")
    if menuChoice == "1":
        if inn.getOwner() == "":
            if not os.listdir("inns"):
                inn = createInn()
        else:
            inn.printInn()
            inn.printCustomers()
    elif menuChoice == "2":
        inn = loadInn()
    elif menuChoice == "3":
        saveInn(inn)
    elif menuChoice == "4":
        inn = createInn()