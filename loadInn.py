import os
from playerClasses import Inn
from createInn import createInn

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
            inn.printInn()
            
            return inn



if __name__ == "__main__":
    inn = loadInn()