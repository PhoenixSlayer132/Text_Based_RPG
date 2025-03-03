import random
from time import sleep

import reference
import config

def search():
    print("Lets start searching!")
    sleep(0.5)

    searchingAnim()
    counter = 0
    while config.searching:
        num = random.randint(1, 5)
        if config.user.hp < config.basePlayerHP * config.playerLVL:
            config.user.hp += 1 * config.playerLVL
        if num <= 3:
            print("Mh.. Found nothing..\nLets try again!")
            sleep(0.5)
            searchingAnim()
        else:
            print("Oh no!")
            config.searching = False
            if config.playerLVL == 1:
                config.opponent = reference.monsterDict.monster.RandomOpponentE()
            elif config.playerLVL <= 3:
                config.opponent = reference.monsterDict.monster.RandomOpponentB()
            else:
                config.opponent = reference.monsterDict.monster.RandomOpponentI()
            print(f"A monster has appeared!\n\n{config.opponent.name} [Level {config.opponent.lvl}]")
            reference.actions.inBattle.battle.startBattle(config.opponent, config.user)

        if counter == 10:
            print("You gave up on the search.\nTime to go home.")
            exit()

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