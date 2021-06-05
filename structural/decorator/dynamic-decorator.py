'''
File with logging decorator
'''

class FileWithLogging:
    def __init__(self, file):
        # store file in attribute upon initialisation
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f'wrote {len(strings)} lines')


    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()

    # let all attribute requests be delegated to underlying file
    # to point into file we store
    def __getattr__(self, item):
        return getattr(self.__dict__['file'], item)

    # determine whether or not we want to access underlying file
    # based on key given
    def __setattr__(self, key, value):
        if key == 'file':
            self.__dict__[key] = value
        else:
            # get dictionary of file value and set name
            setattr(self.__dict__['file'], key)

    # delete attribute of what ever it is on the file.
    def __delattr__(self, item):
        delattr(self.__dict__['file'], item)

if __name__ == '__main__':
    file = FileWithLogging(open('hello.txt', 'w'))
    file.writelines(['hello', ' ' ,'world'])
    file.write('\ntesting')
    file.close()