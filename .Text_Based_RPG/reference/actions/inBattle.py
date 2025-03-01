import random


class battle:
    @classmethod
    def startBattle(self, monster, player):
        if monster.spd > player.spd:
            print("Catching you off guard, the Monster takes initiative!")

            self.monsterInit(player, monster)
        elif monster.spd < player.spd:
            print("You caught the monster off guard! You take the initiative!")

            self.playerInit(player, monster)
        else:
            print("You both notice each other at the same time!")

            if random.randint(1, 4) % 2 == 0:
                print("You were just slightly faster!")
                self.playerInit(player, monster)
            else:
                print("The monster was just slightly faster!")
                self.monsterInit(player, monster)

    @classmethod
    def endBattle(self):
        def lostBattle(inBattle):
            print("Oh no! You Lost!\nExecute Order 77.")
            inBattle = False

        def wonBattle(inBattle):
            print("Yay! You Won!\nExecute Order 66.")
            inBattle = False

    @classmethod
    def playerInit(self, player, opponent):
        while player.hp != 0 and opponent.hp != 0:
            self.playerTurn()
            self.opponentTurn()
        if player.hp == 0:
            print()
        elif opponent.hp == 0:
            print()

    @classmethod
    def monsterInit(self, player, opponent):
        while player.hp != 0 and opponent.hp != 0:
            self.opponentTurn()
            self.playerTurn()
        if player.hp == 0:
            print()
        elif opponent.hp == 0:
            print()

    @classmethod
    def playerTurn(self):
        print()

    @classmethod
    def opponentTurn(self):
        print()