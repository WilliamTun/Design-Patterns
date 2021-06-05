class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {self.filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')

class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        '''
        LOADING of image only happens ONCE upon first invocation
        '''
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing')

if __name__ == '__main__':
    '''
    The problem with the following invocation
    is that if we do not call draw_image(bmp)
    we are still REDUNDANTLY loading the image 
    via Bitmap('image.jpg')
    '''
    #bmp = Bitmap('image.jpg')
    #draw_image(bmp)


    '''
    LazyBitmap solves the problem above
    so that smile.jpg is not loaded
    UNLESS we call draw_image.
    
    Note also, that when we call draw_image twice
    that smile.jpg is loaded only once. 
    '''
    bmp = LazyBitmap('smile.jpg')
    draw_image(bmp)
    draw_image(bmp)