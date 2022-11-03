from pysics.math.Vector2 import Vector2


class CircleCollider:
    def __init__(self, radius:float, pos:Vector2):
        self.radius = radius
        self.pos = pos

    # TODO: Revisar colisiones con otros circulos dependiendo de la distancia entre los dos
    def is_colliding(self,other):
        return False # Cambiar esto