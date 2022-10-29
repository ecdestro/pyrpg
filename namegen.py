import random
from random import randint

fileA = open("assets/text/digrams.txt", "r")
fileB = open("assets/text/trigrams.txt", "r")
Names = open("assets/text/names.txt", "w")

digrams = fileA.read().splitlines()
trigrams = fileB.read().splitlines()

n = len(digrams)
m = len(trigrams)
uniqueList = []
duplicateList = []

def chooser():
    pattern = []
    for counter in range(0, n*m):
        for choice in range(0,3):
            if choice == 0:
                word = random.choice(trigrams) + random.choice(digrams)
                pattern.append(word.lower())
            elif choice == 1:
                word = random.choice(digrams) + random.choice(trigrams) + random.choice(trigrams)
                pattern.append(word.lower())
            elif choice == 2:
                word = random.choice(digrams) + random.choice(trigrams) + random.choice(digrams)
                pattern.append(word.lower())
    return pattern
    
for word in chooser():
    Names.write(word.capitalize())
    Names.write("\n")

fileA.close()
fileB.close()
Names.close()