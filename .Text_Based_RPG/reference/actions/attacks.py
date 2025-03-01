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
                    config.opponent = None
                    actions.inBattle.battle.wonBattle()