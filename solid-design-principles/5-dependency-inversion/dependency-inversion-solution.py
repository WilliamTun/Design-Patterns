'''
Depedency inversion principle
High level classes should not depend on low level modules
High level classes should depend on abstraction (abstract classes/methods)
Relying on abstraction interfaces allowing easy switching & flexibility
'''
from abc import abstractmethod
from enum import Enum

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

'''
Solution - add in a abstract method to give flexibility to interface
'''

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    '''
    Note how the find children of module is now in the Relationship class which inherits from the abstract class
    '''
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name



'''
Note how the research interface is completely decoupled from the internal workings of the .find_all_children_of() method
The research module will not break if low level mechanics are changed.
eg. if self.relations = [] 
    is changed to something other than a list ... eg. storage is switched to a database. 
'''
class Research:
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# Build relationships
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)