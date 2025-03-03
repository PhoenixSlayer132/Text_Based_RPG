from time import sleep

import config
import random

from .actions.attacks import attacks


class player:
    def __init__(self, name, lvl, hp, df, spd, atk, TYPE):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.df = df
        self.spd = spd
        self.atk = atk
        self.TYPE = TYPE

    def __str__(self):
        return f"{self.name} Level [{self.lvl}]\nHP:[{self.hp}]\nDEF:[{self.df}]\nSPD:[{self.spd}]\nATK:[{self.atk}]"

    @classmethod
    def Attack(self, target, user):
        if user.atk < target.df:
            attacks.ineffectiveAttack()
        else:
            attacks.effectiveAttack(target, user.atk, user)
    @classmethod
    def Defend(self, dmg, user, target):
        if user.df < dmg:
            attacks.effectiveAttack(user, abs(user.df - dmg), target)
        else:
            attacks.ineffectiveAttack()
    @classmethod
    def Observe(self, target):
        if random.randint(1, 10) > 3:
            print(target)
        else:
            print("Oh no! You failed at observing the enemy!")

    # For Application Development #
    def SLDFile(self):
        def saveData():
            print()

        def loadData():
            print()

        def delData():
            print()

        self.saveDat = saveData
        self.loadDat = loadData
        self.delDat = delData

    @classmethod
    def characterCreation(self):
        charName = str(input("Input a name for your character: "))

        config.user = player(charName, config.basePlayerLvl, config.basePlayerHP, config.basePlayerDF, config.basePlayerSPD, config.basePlayerATK, "player")
        print(f"\nLets check out our Stats!\n\n{config.user}\n")
        sleep(1.5)

