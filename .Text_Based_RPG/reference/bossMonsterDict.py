import random

from .actions.attacks import attacks
import config

class bossMonster:
    def __init__(self, name, lvl, hp, df, spd, atk, TYPE):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.df = df
        self.spd = spd
        self.atk = atk
        self.TYPE = TYPE

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
        return f"{self.name} Level [{self.lvl}]\nHP:[{self.hp}]\nDEF:[{self.df}]\nSPD:[{self.spd}]\nATK:[{self.atk}]\n[[BOSS]]"
    @classmethod
    def Attack(self, monst, player):
        config.monsterDefending = False
        if not config.playerDefending:
            if monst.atk < player.df:
                attacks.ineffectiveAttack()
            elif monst.atk == player.df:
                attacks.neutralAttack(player, monst, monst)
            else:
                attacks.effectiveAttack(player, monst.atk, monst)
        else:
            config.playerDefending = False
            if player.df < monst.atk:
                attacks.neutralAttack(player, monst, monst)
            else:
                attacks.ineffectiveAttack()

    @classmethod
    def Defend(self):
        if config.monsterInit:
            config.monsterDefending = True
            config.monsterInit = False
    @classmethod
    def RandomOpponentP(self):
        return bossMonster(self.names[random.randint(0, len(self.names) - 1)], config.bossMonstLvl, config.bossMonstHP, config.bossMonstDF, config.bossMonstSPD, config.bossMonstATK, "boss")
