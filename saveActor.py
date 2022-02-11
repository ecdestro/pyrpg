import os
from playerModels import Actor
from playerModels import Inn

def saveActor(inn):
    if len(inn.getLedger()) == 0:
        print("No customers to save!")
    else:
        for customer in inn.getLedger():
            with open(r"inns/" + inn.getOwner() + "/" + customer.getName(), "w") as playerFile:
                playerFile.write(customer.getName() + "," + str(customer.getHP()) + "," + str(customer.getDmg()) + "," + str(customer.getInit()) + "," + str(customer.getExp()) + "," + str(customer.getWealth()))
                customer.printActor()
                print(customer.getName() + " saved!")