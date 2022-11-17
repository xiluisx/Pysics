import os
from pysics.game import GameHandler
from pysics.math.Vector2 import Vector2
from pysics.physics.CircleCollider import CircleCollider
from pysics.physics.SquareCollider import SquareCollider

game = GameHandler.Game("Test", 600, 800)
game.start()
obj = game.add_object(os.path.dirname(__file__) + "\img\RedBall.png", CircleCollider(10, Vector2(0, 0)), Vector2(400,300))
obj.col.object = obj
pared1 = game.add_object(os.path.dirname(__file__) + "\img\Background.png", SquareCollider(Vector2(0, 0), 30,1000))
pared1.col.static = True
obj.add_aceleracion(Vector2(0, -10))
