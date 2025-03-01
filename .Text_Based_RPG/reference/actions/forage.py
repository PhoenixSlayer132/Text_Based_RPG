import random
from time import sleep
from reference.monsterDict import monster
import config

def search():
    print("Lets start searching!")
    sleep(0.5)

    searchingAnim()

    while config.searching:
        num = random.randint(1, 5)

        if num <= 4:
            print("Mh.. Found nothing..\nLets try again!")
            sleep(0.5)

            searchingAnim()
        else:
            print("Oh no!")
            config.searching = False
            config.opponent = monster.RandomOpponent()
            print(f"A monster has appeared!\n\n{config.opponent.name} [Level {config.opponent.lvl}]")

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