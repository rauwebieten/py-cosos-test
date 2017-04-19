from cocos.actions import Action
import math
from pyglet.window import key
import pyglet

import cocos.actions.move_actions

class MoveShip(Action):
    def step(self, dt):
        super(MoveShip, self).step(dt)

        self.target.rotation += 2

        rads = math.radians(self.target.rotation)
        vx = math.sin(rads) * self.target.speed
        vy = math.cos(rads) * self.target.speed

        self.target.x += vx * dt
        self.target.y += vy * dt
