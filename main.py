from playerModels import Inn
from loadsave import loadInn
from loadsave import saveInn
from new import newInn

inn = Inn()

menuChoice = "1"

while menuChoice != "4":
    print("\nRPG v0.0.7\n")
    print("Current owner: " + inn.getOwner())
    print("\n\t1 - Play")
    print("\t2 - Load Inn")
    print("\t3 - New Inn")
    print("\t4 - Quit\n")
    menuChoice = input("Please make a selection:\n")
    if menuChoice == "1":
        if inn.getOwner() == "":
            inn = loadInn()
        else:
            inn.printInn()
            inn.printCustomers()
    elif menuChoice == "2":
        inn = loadInn()
    elif menuChoice == "3":
        inn = newInn()