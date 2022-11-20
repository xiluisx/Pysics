import math
from pysics.math.Vector2 import Vector2
from pysics.physics.SquareCollider import SquareCollider

class CircleCollider:
    def __init__(self, radius:float, pos:Vector2):
        self.object = None
        self.radius = radius
        self.pos = pos
        self.static = False
        self.mass = 10

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
            # TODO: Mide distancia de centros
            centroCirculo = Vector2(self.pos.x + self.radius, self.pos.y + self.radius)
            centroCuadrado = Vector2(other.pos.x + (other.width/2), other.pos.y + (other.height/2))
            sumx = (centroCirculo.x - centroCuadrado.x) ** 2
            sumy = (centroCirculo.y - centroCuadrado.y) ** 2
            dist = math.sqrt(sumx + sumy)
            circleDistance = Vector2(abs(centroCirculo.x - centroCuadrado.x), abs(centroCirculo.y - centroCuadrado.y))

            if circleDistance.x > (other.width / 2 + self.radius):
                return False
            if circleDistance.y > (other.height / 2 + self.radius):
                return False

            if circleDistance.x <= (other.width / 2):
                return True
            if circleDistance.y <= (other.height / 2):
                return True

            cornerDistance_sq = (circleDistance.x - other.width / 2) ^ 2 + (circleDistance.y - other.height / 2) ^ 2

            return cornerDistance_sq <= (self.radius ^ 2)
        return False
