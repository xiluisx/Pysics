from pysics.math.Vector2 import Vector2


class SquareCollider:
    def __init__(self, pos: Vector2, height: float, width: float):
        self.pos = pos
        self.height = height
        self.width = width
        self.static = False

    # TODO: Revisar colisiones con otros cuadrados dependiendo de la distancia entre los dos
    def is_colliding(self, other):
        # TODO: Revisa que el otro objeto sea circulo o cuadrado
        if type(other) is SquareCollider:
            points = [
                self.pos,
                self.pos + Vector2(self.width, 0),
                self.pos + Vector2(0, self.height),
                self.pos + Vector2(self.width, self.height)
            ]
            for point in points:
                if other.x < point.x < other.x + other.width and other.y < point.y < other.y + other.height:
                    return True

            return False
        return False
