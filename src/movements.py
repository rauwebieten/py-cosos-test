from cocos.actions import Action
import math
from pyglet.window import key


class MoveShip(Action):
    def step(self, dt):
        super(MoveShip, self).step(dt)

        if key.LEFT in self.target.keys:
            self.target.rotation -= 5

        if key.RIGHT in self.target.keys:
            self.target.rotation += 5

        if key.UP in self.target.keys:
            self.target.speed += 2

        if key.DOWN in self.target.keys:
            self.target.speed -= 1

        rads = math.radians(self.target.rotation)
        vx = math.sin(rads) * self.target.speed
        vy = math.cos(rads) * self.target.speed

        self.target.x += vx * dt
        self.target.y += vy * dt