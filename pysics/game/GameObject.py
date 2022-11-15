import pygame

from pysics.math.Vector2 import Vector2


class GameObject:
    def __init__(self, spritePath, col, pos: Vector2 = Vector2(0, 0)):
        self.sprite = pygame.image.load(spritePath)
        self.pos = pos
        self.col = col

    def draw(self, world):
        world.blit(self.sprite, (self.pos.x, self.pos.y))
