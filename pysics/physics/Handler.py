import math

from pysics.math.Vector2 import Vector2
from pysics.physics.CircleCollider import CircleCollider
from pysics.physics.SquareCollider import SquareCollider


class Handler:
    def __init__(self):
        self.colliders = []

    # TODO: Revisar colisiones dependiendo del tipo de collider que tenga
    def update(self):
        for col in self.colliders:
            for other in self.colliders:
                if other == col:
                    continue
                else:
                    if col.is_colliding(other): # TODO: Hacer que se choque cuando colisiones
                        if type(other) is SquareCollider:
                            nearestX = max(other.pos.x, min(col.pos.x + col.radius, other.pos.x + other.width))
                            nearestY = max(other.pos.y, min(col.pos.y + col.radius, other.pos.y + other.height))

                            dist = Vector2(col.pos.x + col.radius - nearestX, col.pos.y + col.radius - nearestY)
                            dnormal = Vector2(-dist.y, dist.x)

                            normal_angle = math.atan2(dnormal.y, dnormal.x)
                            incoming_angle = math.atan2(col.object.aceleracion.y, col.object.aceleracion.x)
                            theta = normal_angle-incoming_angle
                            col.object.aceleracion.rotate(2*theta)
                            col.object.pos += col.object.aceleracion
                            col.pos += col.object.aceleracion
                        if type(other) is CircleCollider:
                            
