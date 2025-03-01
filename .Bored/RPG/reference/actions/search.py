import random
from time import sleep


class search:
    searching = True
    while searching:
        num = random.randint(1, 5)

        match num:
            case 1, 2, 3, 4:
                print("Mh.. Found nothing..\nLets try again!")
                print("Searching..")
                sleep(3.0)
            case 5:
                print("Oh no!")
                searching = False