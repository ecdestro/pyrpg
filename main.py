from random import randint
from actor import Actor
from combat import combat
from create import createChar

Player = createChar()
# Opponent = Actor("Enemy", randint(30, 45), 10, 10)
Opponent = Actor("Enemy", randint(30, 45), randint(1, 10), randint(1, 10))

victor = combat(Player, Opponent)

print(victor.getName() + " WINS!")