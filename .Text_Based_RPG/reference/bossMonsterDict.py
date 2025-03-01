from .actions.attacks import attacks

class bossMonsterDict:
    def __init__(self, name, lvl, hp, df, spd, atk):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.df = df
        self.spd = spd
        self.atk = atk

    names = ["The Interspacial Galactor",
             "The Draconic Maelor",
             "The Gawd Dalosius",
             "The Dwarf Gitaro",
             "The Android Mechnyto",
             "The Furry Sven",
             "The Dark Veilshadow",
             "The Holy Nightingale",
             "The Demonic Madapple",
             "The Vermilion Night Stalker",
             "The Necrotic Dreadmawh",
             "The Evil Vileheart",
             "The Pretty Normal Guy Karl"]

    def __str__(self):
        return f"{self.name} Level [{self.lvl}]\nHP:[{self.hp}]\nDEF:[{self.df}]\nSPD:[{self.spd}]\nATK:[{self.atk}]"

    def Attack(self, target):
        if self.atk < target.df:
            attacks.ineffectiveAttack()
        else:
            attacks.effectiveAttack(target, self.atk)

    def Defend(self, dmg):
        if self.df < dmg:
            attacks.effectiveAttack(self.hp, (self.df - dmg))
        else:
            attacks.ineffectiveAttack()
