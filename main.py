from cocos import scene
from cocos.layer import Layer
from cocos.director import director
import src.ship


class Game(Layer):
    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__()
        self.keys_pressed = set()

        self.ship = src.ship.Ship()
        self.add(self.ship)

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)


director.init()
director.run(scene.Scene(Game()))
