from reference import actions
import config

class attacks:
    @classmethod
    def ineffectiveAttack(self):
        print("The attack was Ineffective.\n")

    @classmethod
    def effectiveAttack(self, target, damage, dealer):
            target.hp -= damage
            if target.hp >= 1:
                print(f"{target.name} took {damage} damage!\n{target.name} is now at {target.hp} HP!\n")
            else:
                print(f"{target.name} took {damage} damage!\n{target.name} has fallen victim to {dealer.name}!\n")
                if target.TYPE == "player":
                    actions.inBattle.battle.lostBattle()
                else:
                    config.searching = True
                    actions.inBattle.battle.wonBattle()

    @classmethod
    def neutralAttack(self, target, opponent, dealer):
        damage = int(opponent.atk / 2)
        target.hp -= damage
        dealer.hp -= int(damage / 2)
        if target.hp >= 1 and dealer.hp >= 1:
            print(f"{target.name} took {damage} damage!\n{target.name} is now at {target.hp} HP!\n{dealer.name} took {int(damage / 2)} damage!\n{dealer.name} is now at {dealer.hp} HP!\n")
        else:
            if target.hp <= 0 and opponent.hp <= 0:
                print(f"{target.name} and {dealer.name} took {damage} damage!\nBoth of you have fallen victim to each other!\n")
                actions.inBattle.battle.lostBattle()
            else:
                if target.hp <= 0:
                    print(f"{target.name} took {damage} damage!\n{target.name} has fallen victim to {dealer.name}!\n")
                    if target.TYPE == "player":
                        actions.inBattle.battle.lostBattle()
                    else:
                        config.searching = True
                        actions.inBattle.battle.wonBattle()
                if opponent.hp <= 0:
                    print(f"{opponent.name} took {damage} damage!\n{opponent.name} has fallen victim to {target.name}!\n")
                    if opponent.TYPE == "player":
                        actions.inBattle.battle.lostBattle()
                    else:
                        config.searching = True
                        actions.inBattle.battle.wonBattle()