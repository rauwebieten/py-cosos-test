from cocos.actions import Move


class MoveShip(Move):

    def step(self, dt):
        super(MoveShip, self).step(dt)

        velocity_x = 100 * 1
        velocity_y = 100 * 0

        # Set the object's velocity.
        self.target.velocity = (velocity_x, velocity_y)