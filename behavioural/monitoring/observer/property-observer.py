'''
Tells you when property has been changed

  PropertyObervable [Event]
        |
       Inherit
        |
        V
      Person  ---As input upon initialisation --> Traffic Authority [Which interacts Person with Event]
      - age


'''

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()

class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        self.property_changed('age', value)

class TrafficAuthority:
    def __init__(self, person):
        self.person = person
        person.property_changed.append(
            self.person_changed
        )

    def person_changed(self, name, value):
        if name == 'age':
            if value < 16:
                print('Sorry, persons under age 16 cannot drive')
            else:
                print('Person can now drive! Congrats. I will now unsubscribe')
                # Once person is age 16, remove that person as a subscriber.
                self.person.property_changed.remove(
                    self.person_changed
                )
                # Thus after unsubscription, no more "person_changed" notifications
                # will be printed onto screen

if __name__ == '__main__':
    p = Person()
    ta = TrafficAuthority(p)
    for age in range(14, 20):
        print(f'Setting age to {age}')
        p.age = age
