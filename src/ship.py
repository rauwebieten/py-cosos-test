from cocos.sprite import Sprite
import src.movements


class Ship(Sprite):
    def __init__(self):
        super(Ship, self).__init__("assets/ship.png")

        self.scale = 0.25

        self.rotation = 0
        self.position = (100, 100)
        self.velocity = (0, 0)
        self.acceleration = (0, 0)
        self.gravity = 0

        self.move = src.movements.MoveShip()

        self.do(self.move)
