import os
from playerModels import Inn
from createInn import createInn
from loadActor import loadActor

def loadInn():
    if not os.path.exists("inns"):
        os.makedirs("inns")
        inn = createInn()
        return inn
    elif not os.listdir("inns/"):
        inn = createInn()
        return inn
    else:
        for fileName in os.listdir("inns"):
                print(fileName)
        fName = input("Choose an Owner\n")
        with open(r"inns/" + fName + r".inn", "r") as ownerFile:
            innString = ownerFile.read().split(",")
            inn = Inn(innString[0], int(innString[1]), int(innString[2]))

        inn = loadActor(inn)
        return inn



if __name__ == "__main__":
    inn = loadInn()
