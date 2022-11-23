import math


class Vector2:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector2(self.x + otro.x, self.y + otro.y)

    def __sub__(self,otro):
        return Vector2(self.x - otro.x, self.y - otro.y)

    def __mul__(self, otro):
        return Vector2(self.x * otro.x, self.y * otro.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __str__(self):
        return "x: " + str(self.x) + ", y:" + str(self.y)

    def rotate(self, angle):
        cos = math.cos(angle)
        sin = math.sin(angle)
        self.x = cos * self.x - sin * self.y
        self.y = sin * self.x - cos * self.y

    @staticmethod
    def dot_product(vec1, vec2):
        return vec1.x * vec2.x + vec1.y * vec2.y

    @staticmethod
    def float_mult(float, vec):
        return Vector2(vec.x * float, vec.y * float)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self):
        if self.magnitude() == 0:
            return Vector2(0,0)
        return Vector2(self.x / self.magnitude(), self.y / self.magnitude())

    @staticmethod
    def clamp(vec, minVec, maxVec):
        return Vector2(min(max(vec.x, minVec.x), maxVec.x), min(max(vec.y, minVec.y), maxVec.y))
