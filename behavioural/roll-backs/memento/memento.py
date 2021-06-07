'''
Memento

For objects or systems that goes through state changes
and require saving of each state & ability rollback
- similar to command design pattern
- but simpler!
Memento saves snapshots via tokens of system at time t
Allows system to roll back to time t of token generation
'''

class Memento:
    '''
    bank account snapshot
    '''
    def __init__(self, balance):
        self.balance = balance

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento):
        self.balance = memento.balance # roll back state of system

    def __str__(self):
        return f'Balance = {self.balance}'

if __name__ == '__main__':
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    m3 = ba.deposit(200)
    print(ba)
    ba.restore(m1) # restore to m1 memento
    print(ba)
    ba.restore(m2) # restore to m2 memento
    print(ba)




