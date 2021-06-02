'''
Interface segregation

Do not stick into many methods into an interface.

'''

'''
A) This is BAD
'''
# WE DO NOT WANT TO DO THIS:
class Machine:
    def printer(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def printer(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass




'''
B) This is GOOD
'''
# We want to SEGREGATE all the interface methods as such:
'''
1. Define abstract method classes
'''
class Printer:
    @abstractmethod
    def printer(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

''' 
2. Define interfaces that inherits from abstract method classes
'''
class MyPrint(Printer):
    def printer(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def printer(self, document):
        pass

    def scan(self, document):
        pass



'''
C) This is BEST
'''
'''
3. Alternatively we can create a abstract method class which is inherited itself into the interface.
'''
class MultiFunctionalDevice(Printer, Scanner):
    @abstractmethod
    def printer(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionalDevice):
    # Note that you do not have to list the abstract method classes like Photocopier class in section 2
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def printer(self, document):
        self.printer.printer(document)

    def scan(self, document):
        self.scanner.scan(document)
