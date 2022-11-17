from pysics.math.Vector2 import Vector2


class Handler:
    def __init__(self):
        self.colliders = []

    def update(self):
        for col in self.colliders:
            for other in self.colliders:
                if other == col:
                    continue
                else:
                    if col.is_colliding(other) and not col.static:
                        if not other.static:
                            other.object.aceleracion += col.object.aceleracion
                        col.object.aceleracion = Vector2(-col.object.aceleracion.x, -col.object.aceleracion.y)
