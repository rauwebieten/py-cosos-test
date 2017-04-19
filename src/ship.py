from cocos.sprite import Sprite
import src.movements


class Ship(Sprite):
    def __init__(self):
        super(Ship, self).__init__("assets/ship.png")

        self.scale = 0.25

        self.x = 200
        self.y = 200
        self.rotation = 180
        self.speed = 100

        self.move = src.movements.MoveShip()

        self.do(self.move)
