import os
from pysics.game import GameHandler
from pysics.math.Vector2 import Vector2
from pysics.physics.CircleCollider import CircleCollider

game = GameHandler.Game("Test", 600, 800)
game.start()
obj = game.add_object(os.path.dirname(__file__) + "\img\RedBall.png", CircleCollider(10, Vector2(0,0)))
obj2 = game.add_object(os.path.dirname(__file__) + "\img\RedBall.png", CircleCollider(10, Vector2(100,0)), Vector2(100,0))

def update():
    obj.pos += Vector2(1, 0)


game.add_update(update)
