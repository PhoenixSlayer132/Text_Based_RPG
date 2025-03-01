import random
from time import sleep
from reference.monsterDict import monster
import config

searching = True

def search():
    global searching
    print("Lets start searching!")
    sleep(0.5)

    print("Searching", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    print(".", end="")
    sleep(0.5)
    print(".\n")
    sleep(1.5)

    while searching:
        num = random.randint(1, 5)

        if num <= 4:
            print("Mh.. Found nothing..\nLets try again!")
            sleep(0.5)

            print("Searching", end="")
            sleep(0.5)
            print(".", end="")
            sleep(0.5)
            print(".", end="")
            sleep(0.5)
            print(".\n")
            sleep(1.5)
        else:
            print("Oh no!")
            searching = False
            config.opponent = monster.RandomOpponent()
            print(f"A monster has appeared!\n\n{config.opponent.name} Level [{config.opponent.lvl}]")