'''
# Problem
# This is BAD code.
# If we add more attributes, we'll have to change the ENTIRE set of properties
# The code is INFLEXIBLE

class Creature:
    def __init__(self):
        self.strength = 10
        self.agility = 10
        self.intelligence = 10

    @property
    def sum_of_stats(self):
        return self.strength + self.intelligence + self.agility

    @property
    def max_stat(self):
        return max(
            self.strength, self.intelligence, self.agility
        )

    @property
    def average_stat(self):
        return self.sum_of_stats / 3.0
'''

# SOLUTION:
class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[Creature.strength]

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value

    @property
    def agility(self):
        return self.stats[Creature.agility]

    @agility.setter
    def agility(self, value):
        self.stats[Creature._agility] = value

    @property
    def intelligence(self):
        return self.stats[Creature.intelligence]

    @strength.setter
    def intelligence(self, value):
        self.stats[Creature._intelligence] = value


    '''
    Note how these properties do NOT need to be changed 
    when new attributes are added. 
    Conclusion:
    Use list backed properties, if you expect alot of new attributes
    to be added to a class over time 
    ... and if you do not want to keep changing methods that operate
        on all the attributes
    '''

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def average_stat(self):
        return float(sum(self.stats) / len(self.stats))
