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

    def __str__(self):
        return "x: " + str(self.x) + ", y:" + str(self.y)

    def rotate(self, angle):
        cos = math.cos(angle)
        sin = math.sin(angle)
        self.x = cos * self.x - sin * self.y
        self.y = sin * self.x - cos * self.y