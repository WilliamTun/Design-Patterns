'''
Can call multiple commands in a chain
'''

import unittest
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
    def __init__(self):
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass

class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount):
        super().__init__()
        self.amount = amount
        self.action = action
        self.account = account

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



'''
Composite command
'''
class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=[]):
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        for x in self:
            x.invoke()

    def undo(self):
        for x in reversed(self):
            x.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acct, to_acct, amount):
        super().__init__([
            BankAccountCommand(from_acct, BankAccountCommand.Action.WITHDRAW, amount),
            BankAccountCommand(to_acct, BankAccountCommand.Action.DEPOSIT, amount)
        ])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok



class TestSuite(unittest.TestCase):
#    def test_composite_deposit(self):
#        print("Running test composite deposit:")
#
#        ba = BankAccount()
#
#        '''
#        Create two separate commands
#        '''
#        deposit1 = BankAccountCommand(
#            ba, BankAccountCommand.Action.DEPOSIT, 100
#        )
#        deposit2 = BankAccountCommand(
#            ba, BankAccountCommand.Action.DEPOSIT, 50
#        )
#
#        '''
#        Put the separate commands into a list
#        put list as input into composite command
#        & invoke composite command
#        '''
#        composite = CompositeBankAccountCommand(
#            [deposit1, deposit2]
#        )
#        composite.invoke()
#        print(ba)
#        composite.undo()
#        print(ba)

#    def test_transfer_fail(self):
#        print("\nRunning test transfer fail:")
#        ba1 = BankAccount(100)
#        ba2 = BankAccount(0)
#
#        amount = 100
#        wc = BankAccountCommand(
#            ba1, BankAccountCommand.Action.WITHDRAW, amount
#        )
#        dc = BankAccountCommand(
#            ba2, BankAccountCommand.Action.DEPOSIT, amount
#        )
#
#        transfer = CompositeBankAccountCommand([wc, dc])
#
#        transfer.invoke()
#        print(f'ba1: {ba1}, ba2: {ba1}')
#        transfer.undo()
#        print(f'ba1: {ba1}, ba2: {ba1}')


    def test_better_transfer(self):
        print("\nRunning test better transfer:")
        ba1 = BankAccount(100)
        ba2 = BankAccount(0)

        amount = 100

        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print(f'ba1: {ba1}, ba2: {ba2}')
        transfer.undo()
        print(transfer.success)
        print(f'ba1: {ba1}, ba2: {ba2}')


if __name__ == '__main__':
    unittest.main()