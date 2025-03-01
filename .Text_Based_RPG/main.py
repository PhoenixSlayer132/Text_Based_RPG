import random
from time import sleep

import config
from reference.playerDict import player
from reference.actions.forage import search
from reference.actions import inBattle


class RPG:
    charName = str(input("Input a name for your character: "))

    config.user = player(charName, 1, 20, random.randint(1, 5), random.randint(1, 5), random.randint(3, 7))
    print(f"\nLets check out our Stats!\n\n{config.user}\n")
    sleep(1.5)

    search()

    inBattle.battle.startBattle(config.opponent, config.user)