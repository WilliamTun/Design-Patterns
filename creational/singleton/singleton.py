'''
Singletons

There are cases when we only want to initialise an object ONCE.
Eg. a Database or spark framework.
You want to be able to initialise this object lazily and ONLY when needed.
'''

def singleton(class_):
    instances = {}
    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)

        return instances[class_]

    return get_instance

@singleton
class Database:
    def __init__(self):
        print('Loading database')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)




'''
# How NOT to create a singleton class
class Database:
    _instance = None

    def __init__(self):
        print('Loading database from file')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)

        return cls._instance


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
'''

