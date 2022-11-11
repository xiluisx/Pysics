import os
from pysics.game import GameHandler
from pysics.math.Vector2 import Vector2

game = GameHandler.Game("Test", 600, 800)
game.start()
obj = game.add_object(os.path.dirname(__file__) + "\img\RedBall.png")


def update():
    obj.pos.x += 1


game.add_update(update)
