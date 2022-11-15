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
