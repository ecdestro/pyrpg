import os
import random
from playerModels import Inn
from populateInn import populate

def createInn():
    innFile = Inn()
    innFile.setOwner(input("\nName the owner of this Inn:\n"))
    innFile.setCustomerMax(random.randint(3, 10))
    innFile.setWealth(5000)

    if not os.path.exists("inns"):
        os.makedirs("inns")
    
    if not os.path.exists("inns/" + innFile.getOwner()):
        os.makedirs("inns/" + innFile.getOwner())

    with open(r"inns/" + innFile.getOwner() + r".inn", "w") as innManifest:
        innManifest.write(innFile.getOwner() + "," + str(innFile.getCustomerMax()) + "," + str(innFile.getWealth()))
        
    populate(innFile)
    return innFile

if __name__ == "__main__":
    inn = createInn()
    inn.printInn()