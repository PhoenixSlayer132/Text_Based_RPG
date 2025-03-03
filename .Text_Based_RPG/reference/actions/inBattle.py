import random
from time import sleep

import config
from .forage import search
from ..playerDict import player
from ..monsterDict import monster

userDefending = False
monstDefending = False

class battle:
    @staticmethod
    def startBattle(monster, player):
        if monster.spd > player.spd:
            print("Catching you off guard, the Monster takes initiative!")
            sleep(2.0)
            battle.monsterInit(player, monster)
        elif monster.spd < player.spd:
            print("You caught the monster off guard! You take the initiative!")
            sleep(1.0)
            battle.playerInit(player, monster)
        else:
            print("You both notice each other at the same time!")

            if random.randint(1, 4) % 2 == 0:
                print("But you were just slightly faster!")
                sleep(1.0)
                battle.playerInit(player, monster)
            else:
                print("But the monster was just slightly faster!")
                sleep(1.0)
                battle.monsterInit(player, monster)



    @classmethod
    def lostBattle(self):
        print("Oh no! You Lost!\nExecute Order 77.")
        exit()

    @classmethod
    def wonBattle(self):
        print("Yay! You Won!")
        self.levelUp(config.opponent)
        config.opponent = None
        var = str(input("Would you like to continue playing? (Yes/No)"))
        if var.lower() == "yes":
            search()
        else:
            print("Ending Program.")
            exit()

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
        global userDefending, monstDefending
        userDefending = False
        var = True

        while var:
            choice = str(input("It's Your Turn!\nWould you like to [Attack], [Defend], or [Observe]?"))
            if choice.lower() == "attack":
                player.Attack(config.opponent, config.user)
                var = False
            elif choice.lower() == "defend":
                userDefending = True
                if userDefending and not monstDefending:
                    player.Defend(config.opponent.atk, config.user, config.opponent)
                    var = False
                else:
                    print("The Monster also Defended!\n")
                    var = False
            elif choice.lower() == "observe":
                player.Observe(config.opponent)
                var = False
            else:
                print("Invalid Choice!")

    @classmethod
    def opponentTurn(self):
        global monstDefending
        monstDefending = False
        choice = ["attack",
                  "defend"]

        print("It's The Opponent's Turn!\n")
        sleep(1.0)
        if choice[random.randint(0, 1)] == "attack":
            print("It chose to Attack!\n")
            monster.Attack(config.opponent, config.user)
        else:
            print("It chose to Defend!")
            monstDefending = True
            if monstDefending and not userDefending:
                monster.Defend(config.user.atk, config.opponent, config.user)
            else:
                print("The Player also Defended!\n")

    @classmethod
    def levelUp(self, opponent):
        leveled = False
        config.levelMeter += opponent.lvl * 0.7 if opponent.lvl >= 3 else opponent.lvl * 0.4
        while config.levelMeter >= 1.0:
            config.playerLVL += 1
            config.levelMeter -= 1.0
            leveled = True
        if leveled:
            print("You leveled up!")
            config.lvlStats()
            print(f"{config.user}")
