'''
flyweights
Aim: reduce redundancy when storing data
What?
A space optimization technique to reduce memory usage
How?
store data externally and make reference pointers
and call references only when needed

Example:
eg. Plenty of users with identitcal names
    No sense in storing names over and over again
    Instead, store a list & make references to them.
'''
import string
import random

class User:
    def __init__(self, name):
        self.name = name

class User2:
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x) for x in full_name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names]) # joins the first and last name

def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for x in range(8)]) # joins all 8 characters to produce one string

if __name__ == '__main__':
    users = []
    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    for first in first_names:
        for last in last_names:
            users.append(User2(f'{first} {last}'))

    print(users[0])