'''
Proxy is a class that functions as an interface to a resource
Protection proxy is a common pattern
that permits access to a resource
'''

class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car is being driven by {self.driver.name}')

'''
The proxy
'''
class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        '''
        Permit drive ONLY if age of driver is over 16
        '''
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print('Driver too young')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    driver1 = Driver('John', 20)
    car = CarProxy(driver1)
    car.drive()

    driver2 = Driver('Baby', 2)
    car2 = CarProxy(driver2)
    car2.drive()
