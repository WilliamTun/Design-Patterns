'''
Bridges
Connect components through abstractions
Prevents cartesian product complexity explosion

eg. If you have a function that can do task A & B, under environment conditions X & Y
.. we have 4 combinations: AX, AY, BX, BY.
.. the complexity increases exponentially with each task / environment added.
The bridge pattern solves this issue.

"Bridges are mechanisms that decouple an hierachical interface from the hierachical implementation"
'''

# hierachical interface: circle & square
# hierachical implementation: rasta & vector
from abc import ABC


'''
        Renderer
         /    \
       vector raster
'''

class Renderer(ABC):
    def render_circle(self, radius):
        pass

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')

'''
                Shape 
                /    \
Renderer -> Circle    Square  

'''


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5) # circle shape with vector renderer
    circle.draw()
    circle.resize(2)
    circle.draw()

    circle = Circle(raster, 5)  # circle shape with raster renderer
    circle.draw()
    circle.resize(2)
    circle.draw()







