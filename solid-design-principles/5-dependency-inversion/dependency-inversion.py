'''
Depedency inversion principle
High level classes should not depend on low level modules
High level classes should depend on abstraction (abstract classes/methods)
Relying on abstraction interfaces allowing easy switching & flexibility
'''
from enum import Enum

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name


'''
Problem. Look at how self.relations is defined. 
It is assigned a list [] 
What if later, we want to change the data stucture to a dictionary? 
This causes inefficiency as the research class ALSO has direcly referenced list methods
so if we change self.relations, we ALSO have to change class research. 
'''
class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

class Research:
    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                print(f'John has a child called {r[2].name}')

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# Build relationships
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)