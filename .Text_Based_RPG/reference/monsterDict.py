import random

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

    names = ["Galactor",
            "Maelor",
            "Daelon",
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
    def RandomOpponent(self):
        return monster(self.names[random.randint(0, len(self.names) - 1)], random.randint(1, 10), random.randint(20, 100), random.randint(3, 7), random.randint(3, 7), random.randint(3, 7), "monster")
