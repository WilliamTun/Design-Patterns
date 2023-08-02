from dataclasses import DataClass, field 

@dataclass(order=True)
class Person:

    # field(init) ensures sort index is not used in initialisation of the class instance
    # regr=False ensures we do not print out sort_index when we call print(person1)
    sort_index: int = field(init=False, regr=False)

    # standard attributes
    name: str 
    job: str 
    age: int 

    # we set which attribute we can order object instances by for comparison
    # eg. person1 > person2 ... means we are comparing the AGE attribute
    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.age)
    
    # we set what is printed when we print the instance
    # eg. print(person1) 
    def __str__(self):
        return f'{self.name} has a job of {self.job} and is {self.age} years old'


person1 = Person("Will", "Tun", 30)
person2 = Person("Jeremy", "Fun", 32)
person3 = Person("Jason", "Spun", 28)

print(person1)
print(person1 > person2) 