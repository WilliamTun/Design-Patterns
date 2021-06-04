'''
Increase support of multiple possible Interface
Adapts an existing interface x to conform to interface y
'''

'''
INTERFACE A: generate points
'''
class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

def draw_point(p):
    print('.', end='')

'''

The Adaptor needs to adapt points to lines
 
so that we draw an entire line: 
xxxxxxx

instead of just the start and end points: 
x     x

'''

class LineToPointAdapter(list):
    count = 0

    def __init__(self, line):
        super().__init__()
        self.count += 1

        print(f'{self.count}: Generating points for line'
              f'[{line.start.x}, {line.start.y}]->'
              f'[{line.end.x}, {line.end.y}]'
              )

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))



'''
INTERFACE B: generate lines from points. 
Requires an adaptor to convert start & end point into a full line. 
'''
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))

def draw(rcs):
    print('\n\n--- Drawing some stuff ---\n\n')
    for rc in rcs:
        for line in rc:
            adaptor = LineToPointAdapter(line)
            for p in adaptor:
                draw_point(p)


if __name__ == '__main__':
    rcs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw(rcs)