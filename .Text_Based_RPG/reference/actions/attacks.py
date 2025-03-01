class attacks:
    @classmethod
    def ineffectiveAttack(self):
        print("The attack was Ineffective.\n")

    @classmethod
    def effectiveAttack(self, target, damage):
        target.hp -= damage
        print(f"{target.name} took {damage} damage!\n{target.name} is now at {target.hp}!\n")