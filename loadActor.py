import os
from playerModels import Inn
from playerModels import Actor
from createActor import createChar
from createInn import createInn

def loadActor(inn):
    if not os.path.exists("inns"):
        os.makedirs("inns")
        inn = createInn()
        return inn
    elif not os.listdir("inns/" + inn.getOwner()):
        print("No customers in this inn")
        return inn
    else:
        customers = []
        for fileName in os.listdir("inns/" + inn.getOwner()):
                customers.append(fileName)
                print(fileName)
        if inn.getCustomerMax() > len(inn.getLedger()):
            for patron in range(inn.getCustomerMax()):
                with open(r"inns/" + inn.getOwner() + r"/" + customers[patron], "r") as custFile:
                    patron = custFile.read().split(",")
                    customer = Actor(patron[0], int(patron[1]), int(patron[2]), int(patron[3]), int(patron[4]), int(patron[5]))
                    customer.printActor()
                    inn.addCustomer(customer)
        return inn

if __name__ == "__main__":
    inn = Inn("Destro",8,5000)
    loadActor(inn)
    inn.getCustomers()
