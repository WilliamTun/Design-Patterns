'''
              Person

            PersonBuilder
                |
            PersonInfoBuilder
                |
            PersonJobBuilder
                |
            PersonBirthDateBuilder

'''

class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth}' +\
            f'works as  {self.position}'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    '''
    Class to initialise a person
    '''
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    '''
    Inherits from Person Builder.
    Use to give value to person.name attribute.
    '''
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    '''
    Use to give value to person.position attribute.
    '''
    def works_as_a(self, position):
        self.person.position = position
        return self

class PersonBirthDateBuilder(PersonJobBuilder):
    '''
    Use to give value to person.date_of_birth attribute.
    '''
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self

pb = PersonBirthDateBuilder()
me = pb\
    .called('Dimitry')\
    .works_as_a('Quant')\
    .born('1/1/1988')\
    .build()

print(me)