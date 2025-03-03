import random

import config
from .actions.attacks import attacks

class monster:
    def __init__(self, name, lvl, hp, df, spd, atk, TYPE):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.df = df
        self.spd = spd
        self.atk = atk
        self.TYPE = TYPE

    names = ["Goblin",
             "Wolf",
             "Hyena",
             "Karl",
             "Galactor",
             "Maelor",
             "Dalosius",
             "Gitaro",
             "Mechnyto",
             "Sven",
             "Veilshadow",
             "Nightingale",
             "Madapple",
             "Night Stalker",
             "Dreadmawh",
             "Vileheart"]

    def __str__(self):
        return f"{self.name} Level [{self.lvl}]\nHP:[{self.hp}]\nDEF:[{self.df}]\nSPD:[{self.spd}]\nATK:[{self.atk}]"

    @classmethod
    def Attack(self, monst, player):
        if monst.atk < player.df:
            attacks.ineffectiveAttack()
        else:
            attacks.effectiveAttack(player, monst.atk, monst)

    @classmethod
    def Defend(self, dmg, monst, player):
        if monst.df < dmg:
            attacks.effectiveAttack(monst, abs(monst.df - dmg), player)
        else:
            attacks.ineffectiveAttack()

    @classmethod
    def RandomOpponentE(self):
        return monster(self.names[random.randint(1, 4)], config.monstELvl, config.monstEHP, config.monstEDF, config.monstESPD, config.monstEATK, "monster")

    @classmethod
    def RandomOpponentB(self):
        return monster(self.names[random.randint(5, len(self.names) - 7)], config.monstBLvl, config.monstBHP, config.monstBDF, config.monstBSPD, config.monstBATK, "monster")

    @classmethod
    def RandomOpponentI(self):
        return monster(self.names[random.randint(8, len(self.names) - 1)], config.monstILvl, config.monstIHP, config.monstIDF, config.monstISPD, config.monstIATK, "monster")
