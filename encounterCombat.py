from random import randint
from playerModels import Actor

def combat(player, opponent):
    victor, initTop, initBot = Actor(), Actor(), Actor()
    round = 1

    if player.getInit() > opponent.getInit():
        initTop = player
        initBot = opponent
    elif opponent.getInit() > player.getInit():
        initTop = opponent
        initBot = player
    else:
        if randint(0, 1):
            initTop = player
            initBot = opponent
            print(player.getName() + " won the coin toss.")
        else:
            initTop = opponent
            initBot = player
            print(opponent.getName() + " won the coin toss.")
    
    print(initTop.getName() + " starts the fight. (Initiative " + initTop.getName() + " " + str(initTop.getInit()) + " versus " + initBot.getName() + " " + str(initBot.getInit()) + ")")

    while ((initTop.getHP() > 0) and (initBot.getHP() > 0)):
        print("Round " + str(round) + " FIGHT!")
        if randint(0, 1):
            initBot.setHP(initBot.getHP() - initTop.getDmg())
            print(initBot.getName() + " was HIT for " + str(initTop.getDmg()))
        else:
            print(initTop.getName() + " MISSED!")
        if randint(0, 1) and initBot.getHP() > 0:
            initTop.setHP(initTop.getHP() - initBot.getDmg())
            print(initTop.getName() + " was HIT for " + str(initBot.getDmg()))
        elif initBot.getHP() > 0:
            print(initBot.getName() + " MISSED!")
        else:
            print(initBot.getName() + " was DEFEATED!")
        round += 1
    
    if initTop.getHP() > 0:
        initTop.setExp(initTop.getExp() + 1)
        initTop.setWealth(initTop.getWealth() + int(initBot.getWealth()/2))
        initBot.setWealth(int(initBot.getWealth()/2))
        initBot.setKeeper("Dead")
        victor = initTop
        defeated = initBot
    elif initBot.getHP() > 0:
        initBot.setExp(initBot.getExp() + 1)
        initBot.setWealth(initBot.getWealth() + int(initTop.getWealth()/2))
        initTop.setWealth(int(initTop.getWealth()/2))
        initTop.setKeeper("Dead")
        victor = initBot
        defeated = initTop
    return victor, defeated