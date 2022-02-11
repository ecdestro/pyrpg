import os
from playerModels import Inn
from saveActor import saveActor

def saveInn(inn):
    if inn.getOwner() == "":
        print("\nNo Inn to save!\n")
    else:
        with open(r"inns/" + inn.getOwner() + r".inn", "w") as innFile:
            innFile.write(inn.getOwner() + "," + str(inn.getCustomerMax()) + "," + str(inn.getWealth()))
            inn.printInn()
            print(inn.getOwner() + "'s inn saved!!\n")
        saveActor(inn)