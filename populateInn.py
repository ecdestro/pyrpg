import os
import random
from playerClasses import Actor
from playerClasses import Inn

def populate(inn):
    with open(r"assets/text/names", "r") as merDeNoms:
        name = merDeNoms.read().split()

    i = 0
    while i < inn.getCustomerMax():
        customer = Actor(random.choice(name), random.randint(35, 50), random.randint(5, 10), random.randint(5, 10), 0, random.randint(10, 50))
        inn.addCustomer(customer)
        i += 1
    
    for customer in inn.getLedger():
        customer.printActor()