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
    def RandomOpponentE(self):
        return monster(self.names[random.randint(0, 3)], config.monstELvl, config.monstEHP, config.monstEDF, config.monstESPD, config.monstEATK, "monster")

    @classmethod
    def RandomOpponentB(self):
        return monster(self.names[random.randint(4, len(self.names) - 7)], config.monstBLvl, config.monstBHP, config.monstBDF, config.monstBSPD, config.monstBATK, "monster")

    @classmethod
    def RandomOpponentI(self):
        return monster(self.names[random.randint(10, len(self.names) - 1)], config.monstILvl, config.monstIHP, config.monstIDF, config.monstISPD, config.monstIATK, "monster")


    ## UNDER DEVELOPMENT  :::  DO NOT CALL!!!! ##
    @classmethod
    def RandomOpponentP(self):
        return monster(self.names[random.randint(10, len(self.names) - 1)], config.monstILvl, config.monstIHP, config.monstIDF, config.monstISPD, config.monstIATK, "monster")

    @classmethod
    def RandomOpponentN(self):
        return monster(self.names[random.randint(10, len(self.names) - 1)], config.monstILvl, config.monstIHP, config.monstIDF, config.monstISPD, config.monstIATK, "monster")

    @classmethod
    def RandomOpponentH(self):
        return monster(self.names[random.randint(10, len(self.names) - 1)], config.monstILvl, config.monstIHP, config.monstIDF, config.monstISPD, config.monstIATK, "monster")

    @classmethod
    def RandomOpponentG(self):
        return monster(self.names[random.randint(10, len(self.names) - 1)], config.monstILvl, config.monstIHP, config.monstIDF, config.monstISPD, config.monstIATK, "monster")
