import random

from .actions.attacks import attacks

class monsterDict:
    def __init__(self, name, lvl, hp, df, spd, atk):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.df = df
        self.spd = spd
        self.atk = atk

    names = ["Galactor",
            "Maelor",
            "Daelon",
            "Gitaro",
            "Mechnyto",
            "Sven",
            "Veilshadow",
            "Nighting Gale",
            "Madapple",
            "The Vermillion Night Stalker",
            "Dreadmawh",
            "Vile Heart"]

    def __str__(self):
        return f"{self.name} Level [{self.lvl}]\nHP:[{self.hp}]\nDEF:[{self.df}]\nSPD:[{self.spd}]\nATK:[{self.atk}]"

    @classmethod
    def Attack(self, target):
        if self.atk < target.df:
            attacks.ineffectiveAttack()
        else:
            attacks.effectiveAttack(target, self.atk)
    @classmethod
    def Defend(self, dmg):
        if self.df < dmg:
            attacks.effectiveAttack(self.hp, (self.df - dmg))
        else:
            attacks.ineffectiveAttack()

    @classmethod
    def RandomOpponent(self):
        global names
        return monsterDict(names[random.randint(0, len(names))], random.randint(1, 10), random.randint(20, 100), random.randint(3, 7), random.randint(3, 7), random.randint(3, 7))
