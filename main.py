from cocos import scene
from cocos.layer import Layer
from cocos.director import director
import src.ship

class Game(Layer):
    def __init__(self):
        super(Game, self).__init__()

        ship = src.ship.Ship()
        self.add(ship)


director.init()
director.run(scene.Scene(Game()))
