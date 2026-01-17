import random
from time import sleep

import config
from .forage import search
from ..playerDict import player
from ..monsterDict import monster


class battle:
    @staticmethod
    def startBattle(monster, player):
        if monster.spd > player.spd:
            print("Catching you off guard, the Monster takes initiative!\n")
            sleep(2.0)
            config.monsterInit = True
            battle.monsterInit(player, monster)
        elif monster.spd < player.spd:
            print("You caught the monster off guard! You take the initiative!\n")
            sleep(1.0)
            config.playerInit = True
            battle.playerInit(player, monster)
        else:
            print("You both notice each other at the same time!")

            if random.randint(1, 4) % 2 == 0:
                print("But you were just slightly faster!\n")
                sleep(1.0)
                config.playerInit = True
                battle.playerInit(player, monster)
            else:
                print("But the monster was just slightly faster!\n")
                sleep(1.0)
                config.monsterInit = True
                battle.monsterInit(player, monster)



    @classmethod
    def lostBattle(self):
        print("Oh no! You Lost!\nExecute Order 77.")
        exit(132)

    @classmethod
    def wonBattle(self):
        print("Yay! You Won!")
        self.levelUp(config.opponent)
        del config.opponent
        var = str(input("Would you like to continue playing? (Yes/No)"))
        if var.lower() == "yes":
            search()
        else:
            print("Ending Program.")
            exit(132)

    @classmethod
    def playerInit(self, player, opponent):
        while player.hp != 0 and opponent.hp != 0:
            if player.hp != 0:
                self.playerTurn()
            if opponent.hp != 0:
                self.opponentTurn()

    @classmethod
    def monsterInit(self, player, opponent):
        while player.hp != 0 and opponent.hp != 0:
            if opponent.hp != 0:
                self.opponentTurn()
            if player.hp != 0:
                self.playerTurn()

    @classmethod
    def playerTurn(self):
        config.playerDefending = False
        var = True

        while var:
            choice = str(input("It's Your Turn!\nWould you like to [Attack], [Defend], or [Observe]?\n"))
            if choice.lower() == "attack" or choice.lower() == 'a':
                player.Attack(config.opponent, config.user)
                var = False
            elif choice.lower() == "defend" or choice.lower() == "d":
                config.playerDefending = True
                if config.playerDefending and not config.monsterDefending:
                    player.Defend()
                    var = False
                else:
                    print("\nThe Monster also Defended!\n")
                    config.playerDefending = False
                    config.monsterDefending = False
                    var = False
            elif choice.lower() == "observe" or choice.lower() == "o":
                player.Observe(config.opponent)
                var = False
            elif choice.lower() == "stats" or choice.lower() == "s":
                print(f"\n{config.user}\n")
            elif choice.lower() == "end" or choice.lower() == "132":
                exit(132)
            else:
                print("Invalid Choice!")

    @classmethod
    def opponentTurn(self):
        choice = ["attack",
                  "defend"]

        print("It's The Opponent's Turn!\n")
        sleep(1.0)
        if choice[random.randint(0, 1)] == "attack":
            print("It chose to Attack!\n")
            monster.Attack(config.opponent, config.user)
        else:
            print("It chose to Defend!\n")
            config.monsterDefending = True
            if config.monsterDefending and not config.playerDefending:
                monster.Defend()
            else:
                print("\nThe Player also Defended!\n")
                config.playerDefending = False
                config.monsterDefending = False

    @classmethod
    def levelUp(self, opponent):
        leveled = False
        config.levelMeter += opponent.lvl * 0.7 if opponent.lvl >= 3 else opponent.lvl * 0.4
        while config.levelMeter >= (1.0 * config.playerLVL):
            config.playerLVL += 1
            config.levelMeter -= (1.0 * config.playerLVL)
            leveled = True
        if leveled:
            print("\nYou leveled up!")
            config.lvlStats()
            print(f"{config.user}\n")
