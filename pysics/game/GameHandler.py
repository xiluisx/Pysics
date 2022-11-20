import sys
import os
from threading import Thread

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from pygame import QUIT

from pysics.game.GameObject import GameObject
from pysics.math.Vector2 import Vector2
from pysics.physics.Handler import Handler
import pygame


class Game:
    def __init__(self, title, HEIGHT: int, WIDTH: int):
        self.screen = None
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.objects: [GameObject] = []
        self.PhysicsHandler = Handler()
        self.title = title
        self.updateEvents = []

    def __init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.title)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()

    def start(self):
        thread = Thread(target=self.__init)
        thread.start()

    def add_object(self, spritePath, col, pos: Vector2 = Vector2(0, 0)):
        newObj = GameObject(spritePath, col, pos)
        self.objects.append(newObj)
        self.PhysicsHandler.colliders.append(newObj.col)
        return newObj

    def add_update(self, event):
        self.updateEvents.append(event)

    def update(self):
        frame_per_sec = pygame.time.Clock()
        self.screen.fill((0, 0, 0))

        for i in self.updateEvents:
            i()

        self.PhysicsHandler.update()

        # TODO: Actualiza los graficos de los objetos con su posicion
        for obj in self.objects:
            obj.pos += obj.aceleracion
            obj.aceleracion -= obj.desaceleracion
            obj.col.pos = obj.pos
            obj.draw(self.screen)

        # TODO: Corre update() en el PhysicsHandler

        pygame.display.update()
        frame_per_sec.tick(60)

        return
