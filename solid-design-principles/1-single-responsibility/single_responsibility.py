



'''
SINGLE RESPONSIBILITY PRINCIPLE:
We do not want to overload a single class with too many methods that handle too many responsibilities.

In this example, we have a create a journal object
and we SEPARATE the functionality of MANIPULATING properties
to the functionality of PERSITANCE (saving and loading)
'''

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


# Adding Entries
j = Journal()
j.add_entry('i exercised')
j.add_entry('i had a shower')
print(f'Journal entries:\n{j}')

# Persistance
file = r'/Users/williamtun/Documents/Code/DesignPattern/solid-design-principles/1-single-responsibility/journal.txt'
PersistanceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
