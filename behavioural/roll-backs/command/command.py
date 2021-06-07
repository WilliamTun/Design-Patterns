'''
Command is an object that can represent an instruction to perform an action
and contains ALL information necessary for the action to be taken
and contains information to ROLL BACK / UNDO
'''
from abc import ABC
from enum import Enum

class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, balance = {self.balance}')

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount}, balance = {self.balance}')
            return True # true if withdraw method succeeded
        return False # false if no withdraw took place

    def __str__(self):
        return f'Balance = {self.balance}'


class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass

class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount):
        self.amount = amount
        self.action = action
        self.account = account
        self.success = None #success flag to track if operation succeeded

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            #withdraw methods return true or false based on success of operation
            self.success = self.account.withdraw(self.amount)


    def undo(self):
        # can only undo if operation succeeded
        if not self.success:
            return #do nothing if no operation success

        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        if self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == '__main__':
    ba = BankAccount() #0
    cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.DEPOSIT, 100
    )
    cmd.invoke()
    print(f'After $100 deposit: {ba}')

    cmd.undo()
    print(f'Undo $100 deposit: {ba}')


    illegal_cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.WITHDRAW, 1000
    )
    illegal_cmd.invoke()
    print(f'After impossible $1000 withdrawal: {ba}')
    illegal_cmd.undo()
    print(f'After undo: {ba}')







