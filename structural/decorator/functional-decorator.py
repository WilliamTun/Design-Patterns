'''
Decorators

Add extra functionality to an object
So we do not add additional responsibilities to the underlying object

'''
import time


def time_it(func):
    def wrapper():
        '''
        time measurement wrapper
        '''
        start = time.time()
        result = func()
        end = time.time()
        total_time = (end - start) * 1000
        print(f'{func.__name__} took {total_time} ms')
        return result
    return wrapper()

# here we apply the time_it wrapper to some_op
@time_it
def some_op():
    print('Starting op')
    time.sleep(1)
    print('We are done')
    return 123

if __name__ == '__main__':
    # because the time_it decorator is applied,
    # the decorator is automatically called when we call some_op
    some_op