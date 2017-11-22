import pyglet

class SimObject:
    def __init__(self, posx, posy, image=None):
        self.posx = posx
        self.posy = posy
        if image is not None:
            image = pyglet.image.load(image)
            self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y=self.posy)
