'''
Chaining several processes

                          Creature
                             ^
                             |
                      Creature Modifier
                   ^         ^           ^
                   |         |           |
Can be chained > NoBonuses DoubleAttack  IncreaseDefense
'''

class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'

class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

class NoBonusesModifier(CreatureModifier):
    '''
    This modifier STOPs calling super().handle()
    Thus, if applied, any other subsequent modifiers will NOT be invoked
    effectively BREAKING the chain
    '''
    def handle(self):
        print('No bonuses for you')

class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f'Doubling {self.creature.name} attack')
        self.creature.attack *= 2
        super().handle()

class IncreaseDefenseModifier(CreatureModifier):
    '''
    As long as the creatures attack attribute is less than 2,
    we can use this modifier to increase the creatures defense
    '''
    def handle(self):
        if self.creature.attack <= 2:
            print(f'Increasing {self.creature.name} defense')
            self.creature.defense += 1
        super().handle()


if __name__ == '__main__':
    goblin = Creature('Goblin', 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)

    #root.add_modifier(NoBonusesModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))


    root.handle()
    print(goblin)
