import random
from time import sleep

import reference
import config

def search():
    print("\nLets search around for some monsters!")
    sleep(0.5)

    searchingAnim()
    counter = 0
    while config.searching:
        num = random.randint(1, 5)
        if config.user.hp < config.basePlayerHP * config.playerLVL:
            hpHeal = 1 * config.playerLVL
            config.user.hp += hpHeal
            print(f"Healed +{hpHeal} HP")
        if num <= 3:
            print("Mh..", end="")
            sleep(0.3)
            print("Found nothing..")
            sleep(0.3)
            print("Lets try again!\n")
            sleep(0.5)
            searchingAnim()
        else:
            print("Oh no!")
            config.searching = False
            if config.playerLVL == 1:
                config.randomizeE()
                config.opponent = reference.monsterDict.monster.RandomOpponentE()
            elif config.playerLVL <= 3:
                config.randomizeB()
                config.opponent = reference.monsterDict.monster.RandomOpponentB()
            else:
                config.randomizeI()
                config.opponent = reference.monsterDict.monster.RandomOpponentI()
            print(f"A monster has appeared!\n\n{config.opponent.name} [Level {config.opponent.lvl}]")
            reference.actions.inBattle.battle.startBattle(config.opponent, config.user)

        if counter == 10:
            print("You gave up on the search.\nTime to go home.")
            exit(132)

        counter += 1

def searchingAnim():
    print("Sear", end="")
    sleep(0.3)
    print("ching", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    print(".\n")
    sleep(1.5)