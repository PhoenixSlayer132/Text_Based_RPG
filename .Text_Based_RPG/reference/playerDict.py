import random

from .actions.attacks import attacks

class player:
    def __init__(self, name, lvl, hp, df, spd, atk):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.df = df
        self.spd = spd
        self.atk = atk

    def __str__(self):
        return f"{self.name} Level [{self.lvl}]\nHP:[{self.hp}]\nDEF:[{self.df}]\nSPD:[{self.spd}]\nATK:[{self.atk}]"

    @classmethod
    def Attack(self, target, user):
        if user.atk < target.df:
            attacks.ineffectiveAttack()
        else:
            attacks.effectiveAttack(target, user.atk)
    @classmethod
    def Defend(self, dmg, user):
        if user.df < dmg:
            attacks.effectiveAttack(user, abs(user.df - dmg))
        else:
            attacks.ineffectiveAttack()
    @classmethod
    def Observe(self, target):
        if random.randint(1, 10) > 3:
            print(target)
        else:
            print("Oh no! You failed at observing the enemy!")