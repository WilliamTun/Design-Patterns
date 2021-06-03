from abc import ABC
from enum import Enum
from enum import auto

'''
Factory is any entity that can take care of object creation. 
Creating separate static methods for building an object allows
creation of a hierachy of factories via abstract factory 
'''


'''
HotDrink Abstract base class 
    /    \
  Tea    Coffee
'''
class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')

class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')



'''
HotDrink Factory Abstract Base Class
     /         \
Tea-factory    Coffee-factoru
'''

class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind coffee beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()

'''
method to call factory methods based on conditional
'''

def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


'''
One can create a class that can que a set of factories
'''
class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = [] # que factories into this list
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))
                # ^ to factory list, append tuples of (factory name, factory instance)

    def make_drink(self):
        print('Available drinks:')
        # loop through all of qued factories, and print the name
        for f in self.factories:
            print(f[0])

        s = input(f'Please pick drink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)
        # call the factory at the desired index & call the prepare method.


if __name__ == '__main__':

    ''' 
    part 1. - offer user choice to make either tea / coffee & call factory method. 
    '''
    #entry = input('What kind of drink would you like')
    #drink = make_drink(entry)
    #drink.consume()

    '''
    part 2. - Calling the class where users can choose specific factory to call upon
    '''
    hdm = HotDrinkMachine()
    hdm.make_drink()



