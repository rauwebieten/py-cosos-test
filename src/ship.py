from cocos.sprite import Sprite
from cocos.director import director
import src.movements
from pyglet.window import key

class Ship(Sprite):
    def __init__(self):
        super(Ship, self).__init__("assets/ship.png")
        self.keys = set()
        director.window.push_handlers(self)

        self.scale = 0.25

        self.x = 200
        self.y = 200
        self.rotation = 180
        self.speed = 100

        self.move = src.movements.MoveShip()

        self.do(self.move)

    def on_key_press(self, symbol, modifiers):
        self.keys.add(symbol)
        print('on_key_press',self.keys)

    def on_key_release(self, symbol, modifiers):
        self.keys.remove(symbol)
        print('on_key_press',self.keys)