'''
A Builder is a component that provides an API for constructing an object
step by step!

Building out objects in stages can be cumbersome
For example, building an object with 10+ initialisation arguments
Example problem:
obj = NewObject(a=A, b=B, c=C, d=D, e=E, f=F, g=G, h=H, i=I, j=J, k=K)

Example solution:
Opt for piece wise construction - where you call different components of builder methods.

'''

class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)


    '''
    Part 3. Bonus. 
    To hint to end user that one builds HtmlElement with HtmlBuilder
    add a static method that utlises HtmlBuilder to create HtmlElement
    '''
    @staticmethod
    def create(name):
        return HtmlBuilder(name)



class HtmlBuilder:
    def __init__(self, root_name):
        '''
        :param root_name: name parameter to initialise the HtmlElement
        '''
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    '''
    Part 1. Basic interface 
    '''
    def add_child(self, child_name, child_text):
        '''
        Builder method to add to HtmlElement.elements
        :param child_name: *
        :param child_text: *
        '''
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    '''
    Part 2. Fluent interfaces allow chaining of methods
    '''

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self # <-- THIS return self makes a method FLUENT

    def __str__(self):
        return str(self.__root)


builder = HtmlBuilder('ul')
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
print('Ordinary Builder: ')
print(builder)

print('\n')
builder2 = HtmlElement.create('ul') # From bonus part 3
builder2.add_child_fluent('li', 'goodbye').add_child_fluent('li', 'farewell') # Thanks to code from part 2
print('Fluent Builder: ')
print(builder2)

