import cocos
from cocos.director import director


class Game(cocos.layer.Layer):
    def __init__(self):
        super(Game, self).__init__()


director.init()
director.run(cocos.scene.Scene(Game()))
