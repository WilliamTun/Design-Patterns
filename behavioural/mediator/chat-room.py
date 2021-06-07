'''
Mediator
A component that facilitates communication
between components.
'''

class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def recieve(self, sender, message):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

    def private_message(self, who, message):
        self.room.message(self.name, who, message)

    def say(self, message):
        self.room.broadcast(self.name, message)


class ChatRoom:
    def __init__(self):
        '''
        Initialise chatroom with empty list of individuals that are attending the chatroom
        '''
        self.people = []

    def broadcast(self, source, message):
        for p in self.people: # for all the people currently added in the chatroom
            if p.name != source: # if the person is not the actual source/sender of the message
                p.recieve(source, message) # let the person recieve the message.

    def join(self, person):
        join_msg = f'{person.name} joins the chat'
        self.broadcast(source='room', message=join_msg)
        person.room = self

        # add the person to the chatroom
        self.people.append(person)

    def message(self, source, destination, message):
        '''
        :param source: sender of the message
        :param destination: reciever of the message
        :param message: the content of the message
        :return:
        '''
        for p in self.people:
            if p.name == destination:
                p.recieve(source, message)


if __name__ == '__main__':
    room = ChatRoom()
    john = Person('John')
    jane = Person('Jane')

    room.join(john)
    room.join(jane)

    john.say('Hi room!')
    jane.say('oh, hey John')

    simon = Person('Simon')
    room.join(simon)
    simon.say('Hi everyone!')

    jane.private_message('Simon', 'glad you could join us')
