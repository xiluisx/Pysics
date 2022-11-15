import math
from pysics.math.Vector2 import Vector2


class CircleCollider:
    def __init__(self, radius:float, pos:Vector2):
        self.radius = radius
        self.pos = pos

    # TODO: Revisar colisiones con otros circulos dependiendo de la distancia entre los dos
    def is_colliding(self, other):
        # TODO: Revisa que el otro objeto sea circulo o cuadrado
        if other is CircleCollider:
            # TODO: Mide distancia entre ambos
            sumx = (self.x - other.x)**2
            sumy = (self.y - other.y)**2
            raiz = math.sqrt(sumx + sumy)

            # TODO: Si distancia es menor a ambos radios sumados estan chocando
            if raiz < self.radius + other.radius:
                return True
            return
        return False # Cambiar esto
