import random
from time import sleep

from reference.playerDict import player
from reference.actions import inBattle
from reference.monsterDict import monsterDict
from reference.actions import search

battling = False

class main:

    charName = str(input("Input a name for your character: "))

    user = player(charName, 1, 20, random.randint(1, 5), random.randint(1, 5), random.randint(3, 7))
    print(user)

    print("Lets start searching!")
    sleep(3.0)

    search.search()
    opponent = monsterDict.RandomOpponent()
    print(f"A monster has appeared!\n{opponent.name} [{opponent.lvl}]")

    inBattle.battle.startBattle(opponent, user)

