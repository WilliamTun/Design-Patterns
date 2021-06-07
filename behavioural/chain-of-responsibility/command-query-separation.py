'''
Command = asking for an action eg. setting/changing an attribute variable
Query = asking for information eg. what is the value of an attribute
'''

# event broker (observer)
# command - query separation
from enum import Enum
from abc import ABC

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2

class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature_name = creature_name

class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)

class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass

    '''
    Allows with key word to call modifier within scope of with: 
    '''
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)

class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2




class Creature:
    '''
    game: central event broker, which takes care of chain of responsibility
    '''
    def __init__(self, game, name, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.name = name
        self.game = game

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'

if __name__ == '__main__':
    game = Game()
    goblin = Creature(game, 'Strong Goblin', 2, 2)
    print(goblin)

    '''
    Calling modifier within scope of "with" keyword 
    '''
    with DoubleAttackModifier(game, goblin):
        print(goblin)
    print(goblin)

    '''
    Calling modifier directly. 
    '''
    #dam = double attack modifier
    dam = DoubleAttackModifier(game, goblin)
    print(goblin)
