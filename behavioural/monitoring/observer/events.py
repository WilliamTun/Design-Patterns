'''
Listen to events and notifications send when event occurs
- who generated the event?
- what values were generated?
- ability to unsubscribe from events.
'''

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()


    def catch_a_cold(self):
        '''
        :return: notification when a person gets catch a cold event
        '''
        self.falls_ill(self.name, self.address)

def call_doctor(name, address):
    print(f'{name} needs a doctor at {address}')

if __name__ == '__main__':
    person = Person('Sherlock', '221B Baker St')

    # subscribe to event through lambda function
    person.falls_ill.append(
        lambda name, address: print(f'{name} is ill')
    )
    # subscribe to event through predefined function
    person.falls_ill.append(call_doctor)

    person.catch_a_cold() # invoke the event, call method goes through every subscriber, and calls subscriber function

    # remove subscription
    person.falls_ill.remove(call_doctor)
    print("call doctor function has been removed from event subscriptions: ")
    person.catch_a_cold()