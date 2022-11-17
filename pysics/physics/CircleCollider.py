import math
from pysics.math.Vector2 import Vector2
from pysics.physics.SquareCollider import SquareCollider


class CircleCollider:
    def __init__(self, radius:float, pos:Vector2):
        self.object = None
        self.radius = radius
        self.pos = pos
        self.static = False

    def is_colliding(self, other):
        # Revisa que el otro objeto sea circulo o cuadrado
        if type(other) is CircleCollider:
            # Mide distancia entre ambos
            sumx = (self.pos.x - other.pos.x)**2
            sumy = (self.pos.y - other.pos.y)**2
            raiz = math.sqrt(sumx + sumy)
            # Si distancia es menor a ambos radios sumados estan chocando
            if raiz < self.radius + other.radius:
                return True
            return False
        elif type(other) is SquareCollider:
            # TODO: Colisiona con cuadrado
            return
        return False # Cambiar esto
