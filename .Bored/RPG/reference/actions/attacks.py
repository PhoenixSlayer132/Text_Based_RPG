class attacks:
    def ineffectiveAttack(self):
        print("the attack was Ineffective.")

    @classmethod
    def effectiveAttack(self, target, damage):
        target.hp -= damage
        print(f"{target.name} took {damage} damage!\n{target.name} is now at {target.hp}!")