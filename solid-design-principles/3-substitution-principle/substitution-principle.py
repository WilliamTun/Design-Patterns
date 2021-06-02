'''
Liskov Subtitution principle
If you have an interface
that takes a base class
you should be able to stick a derived class in that interface too
and everything should work as before
'''

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


    # Calculate area
    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'width: {self.width}, height: {self.height}'



''' 
Square inherits from rectangle
but there is an extra rule imposed
such that width == height
'''
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectangle(2, 3)
print(rc)
use_it(rc)

sq = Square(5)
use_it(sq)  # We VIOLATE the substitution principle. As square inherits from rectangle... but use_it cannot be applied to square