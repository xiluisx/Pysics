import math

from pysics.math.Vector2 import Vector2
from pysics.physics.CircleCollider import CircleCollider
from pysics.physics.SquareCollider import SquareCollider

compass = [Vector2(0, 1), Vector2(1, 0), Vector2(0, -1), Vector2(-1, 0)]


def get_vector_direction(target:Vector2):
    max = 0
    best_match = -1
    for i in range(4):
        dot_product = Vector2.dot_product(target.normalized(), compass[i])
        if dot_product>max:
            max = dot_product
            best_match = i
            print(best_match)

    return best_match

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
                        if type(col) is SquareCollider:
                            continue

                        if type(other) is SquareCollider:
                            # 0 is colliding, 1 is VectorDirection, 2 is difference
                            # TODO: Get center of circle
                            center = Vector2(col.pos.x + col.radius, col.pos.y + col.radius)
                            # TODO: Get center and half-extents of rect
                            rectHalfExtents = Vector2(other.width/2, other.height/2)
                            rectCenter = other.pos + rectHalfExtents
                            # TODO: Get difference off centers and clamp
                            difference = center - rectCenter
                            clamped = Vector2.clamp(difference, -rectHalfExtents, rectHalfExtents)
                            # TODO: Get closest by addign center and clamp
                            closest = rectCenter + clamped
                            # TODO: Find difference and check if its less than radius
                            difference = closest - center

                            dir = get_vector_direction(difference)
                            if dir == 1 or dir == 3:
                                col.object.aceleracion.x = -col.object.aceleracion.x
                                penetration = col.radius - abs(difference.x)
                                col.object.pos += col.object.aceleracion
                                col.pos += col.object.aceleracion
                                print(penetration)
                                if dir == 1:
                                    col.object.pos.x += penetration
                                    col.pos.x += penetration
                                else:
                                    col.object.pos.x -= penetration
                                    col.pos.x -= penetration
                            else:
                                col.object.aceleracion.y = -col.object.aceleracion.y
                                col.object.pos += col.object.aceleracion
                                col.pos += col.object.aceleracion
                                penetration = col.radius - abs(difference.y)
                                print(penetration)

                                if dir == 0:
                                    col.object.pos.y -= penetration
                                    col.pos.y -= penetration
                                else:
                                    col.object.pos.y += penetration
                                    col.pos.y += penetration


                            """
                            nearestX = max(other.pos.x, min(col.pos.x + col.radius, other.pos.x + other.width))
                            nearestY = max(other.pos.y, min(col.pos.y + col.radius, other.pos.y + other.height))

                            dist = Vector2(col.pos.x + col.radius - nearestX, col.pos.y + col.radius - nearestY)
                            dnormal = Vector2(-dist.y, dist.x)

                            if Vector2.dot_product(col.object.aceleracion, dist) < 0:
                                normal_angle = math.atan2(dnormal.y, dnormal.x)
                                incoming_angle = math.atan2(col.object.aceleracion.y, col.object.aceleracion.x)
                                theta = normal_angle-incoming_angle
                                print(normal_angle*180/math.pi, incoming_angle*180/math.pi, 2*theta*180/math.pi)
                                col.object.aceleracion.rotate(2*theta)
                                col.object.pos += col.object.aceleracion
                                col.pos += col.object.aceleracion
                            else:
                                penetrationDepth = col.radius - dist.magnitude()
                                penetrationVector = Vector2.float_mult(penetrationDepth, dist.normalized())
                                col.object.pos = col.object.pos - penetrationVector
                                col.pos = col.pos - penetrationVector
                                """
                        if type(other) is CircleCollider:
                            a1 = col.object.aceleracion
                            a2 = other.object.aceleracion
                            x1 = col.pos + Vector2(col.radius, col.radius)
                            x2 = other.pos + Vector2(other.radius, other.radius)

                            v1 = a1 - Vector2.float_mult(((2*other.mass) / (col.mass + other.mass)) * (
                                    Vector2.dot_product(a1-a2, x1-x2)/((x1-x2).magnitude()**2)), (x1-x2))
                            col.object.aceleracion = v1
                            col.object.pos += col.object.aceleracion
                            col.pos += col.object.aceleracion
                            v2 = a2 - Vector2.float_mult(((2 * col.mass) / (col.mass + other.mass)) * (
                                        Vector2.dot_product(a2 - a1, x2 - x1) / ((x2 - x1).magnitude() ** 2)),
                                                         (x2 - x1))
                            other.object.aceleracion = v2
                            other.object.pos += other.object.aceleracion
                            other.pos += other.object.aceleracion