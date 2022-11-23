import os
from pysics.game import GameHandler
from pysics.math.Vector2 import Vector2
from pysics.physics.CircleCollider import CircleCollider

game = GameHandler.Game("Test", 600, 800)
game.start()
obj = game.add_object(os.path.dirname(__file__) + "\img\RedBall.png", CircleCollider(10, Vector2(0,0)))
obj2 = game.add_object(os.path.dirname(__file__) + "\img\BlueBall.png", CircleCollider(10, Vector2(100,0)), Vector2(100,0))
obj.col.object = obj
obj.name = "Bola Roja"
obj2.col.object = obj2
obj2.name= "bola Azul"
obj2.col.mass = 20
obj.add_aceleracion(Vector2(1, 0))

