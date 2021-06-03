'''
Reiterate existing designs
- predefined design
- ask factory to customise the design

'''
import copy

class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'

class EmployeeFactory:
    main_office_employee = Employee('', Address('123 East Drive', 0, 'London'))
    aux_office_employee = Employee('', Address('123B East Drive', 0, 'London'))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )


john = EmployeeFactory.new_main_office_employee('John', 101)
jane = EmployeeFactory.new_aux_office_employee('Jane', 500)

print(john)
print(jane)

