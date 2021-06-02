from enum import Enum

'''
Open Close Principle:
- classes are OPEN for extension
- classes are CLOSED for modification

After you have written & tested a class
you should not modify it, only extend it. 
'''


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size =size

#class ProductFilter:
#    def filter_by_color(self, products, color):
#        for p in products:
#            if p.color == color:
#                yield p

'''
BASE CLASSES
'''
class Specification:
    '''
    Base class used to create extensions that deal with adding some sort of specification on what to filter
    '''
    def is_satisfied(self, item):
        pass

    ''' 
    BONUS 
    overriding the & ampersand 
    see: Example Filter 4. 
    Note. You need to write the AndSpecification class before implementing the ampersand override.
    This allows you to call the AndSpecification class as "&"... which is neat! 
    '''
    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    '''
    Base class used to create extensions that deal with filtering
    '''
    def filter(self, items, spec):
        pass

'''
EXTENSION CLASSES FOR SPECIFICATION
'''
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

'''
EXTENSION CLASSES FOR SPECIFICATION: COMBINATOR
- permits combining various specification objects together
'''
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):

        # If every specification is satisfied in the map-lambda, then true is returned & combinator is satisfied
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

'''
EXTENSION CLASSES FOR FILTER
'''

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    bf = BetterFilter()

    # Example Filter 1: Filter out green products only
    print('Green products: ')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')


    # Example Filter 2: Filter out large products
    print('Large products: ')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    # Example Filter 3: COMBINATOR
    print('Large AND blue products: ')
    large = SizeSpecification(Size.LARGE)
    blue = ColorSpecification(Color.BLUE)
    large_blue = AndSpecification(large, blue)
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')

    # Example Filter 4: Combinator with the BONUS, overriding & ampersand
    print('Large AND green products: ')
    large_green = large & green
    for p in bf.filter(products, large_green):
        print(f' - {p.name} is large and green')


