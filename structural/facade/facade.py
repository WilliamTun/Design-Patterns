'''
Facade
prefers Simple and easy to understand API
'''
class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' '] * (width * height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text

class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index+self.offset]

    def append(self, text):
        self.buffer.write(text)

'''
This is the facade
A simplified API over a set of classes
'''
class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text):
        # easy access to buffer class
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index):
        # easy access to Viewport class
        return self.current_viewport.get_char_at(index)



if __name__ == '__main__':
    c = Console()
    c.write('hello')
    ch = c.get_char_at(0)