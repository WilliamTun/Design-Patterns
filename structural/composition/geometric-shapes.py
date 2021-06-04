'''
Composites
treat individual components in a uniform fashion
providing an indentical interface
over aggregates of components

Key points:
Composition allows making compound objects
eg. Person object with parameters name (string) & address (address object)
eg.

Motivation:
If we have objects which use other objects properties & members
through inheritance and composition, we have a mechanism
to treat them all through a uniform manner
'''


'''
                GraphicObject
                /          \
            Circle       Square 
'''


# The Graphic object can act as a scalar base class OR a collection

class GraphicObject:
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = '\n Ok, lets move onto groups:'

    @property
    def name(self):
        return self._name

    # utlity method
    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color: # if a colour exists. Note first item has color is false so will skip.
            items.append(self.color)
            # ^ append specified color to either Circle class or Square class,
            # which both inherit from graphic object

        items.append(f'{self.name}\n') # First item has color == false, so this is what is printed first

        for child in self.children: # print all the coloured objects stored in children list
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)



class Circle(GraphicObject):
    @property
    def name(self):
        return 'Circle'

class Square(GraphicObject):
    @property
    def name(self):
        return 'Square'




if __name__ == '__main__':
    drawing = GraphicObject()
    drawing._name = 'Here is my Graphic Object. Lets start with single scalars:'
    drawing.children.append(Square('Red'))
    drawing.children.append(Circle('Yellow'))

    group = GraphicObject()
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))

    group2 = GraphicObject()  # does a resent to change GraphicObject.__name initiated above back to original .__name
    group2._name = '\n Here is another group: '
    group2.children.append(Circle('Red'))
    group2.children.append(Square('Yellow'))
    group2.children.append(Square('Green'))

    drawing.children.append(group)
    drawing.children.append(group2)

    print(drawing)





