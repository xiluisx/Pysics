import os
import random

from pysics.game import GameHandler
from pysics.math.Vector2 import Vector2
from pysics.physics.CircleCollider import CircleCollider
from pysics.physics.SquareCollider import SquareCollider

game = GameHandler.Game("Test", 600, 800)
game.start()
pared1 = game.add_object(os.path.dirname(__file__) + "\img\Background.png", SquareCollider(Vector2(0,0), 30,1000))
pared1.col.static = True
pared1.col.object = pared1
pared1.name = "pared"

pared2 = game.add_object(os.path.dirname(__file__) + "\img\Background.png", SquareCollider(Vector2(0,500), 30, 1000), Vector2(0,500))
pared2.col.static = True
pared2.col.object = pared2

pared3 = game.add_object(os.path.dirname(__file__) + "\img\Background2.png", SquareCollider(Vector2(0,0), 1000, 30))
pared3.col.static = True
pared3.col.object = pared3

pared4 = game.add_object(os.path.dirname(__file__) + "\img\Background2.png", SquareCollider(Vector2(800,0), 1000, 30), Vector2(800,0))
pared4.col.static = True
pared4.col.object = pared4

for i in range(0,50):
    randX = random.randint(400, 500)
    randY = random.randint(200,300)
    newObj = game.add_object(os.path.dirname(__file__) + "\img\RedBall.png", CircleCollider(10, Vector2(randX,randY)), Vector2(randX,randY))
    newObj.col.object = newObj
    newObj.add_aceleracion(Vector2(random.randint(0,10), random.randint(0,5)))