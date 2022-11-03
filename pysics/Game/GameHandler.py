import sys

from pygame import QUIT

from pysics.physics.Handler import Handler
import pygame

class Game:
    def __init__(self, title, HEIGHT:int, WIDTH:int):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.objects = []
        self.PhysicsHandler = Handler()
        self.title = title

    def init(self):
        pygame.init()
        displaySurface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.title)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()



    def update(self):
        FramePerSec = pygame.time.Clock()
        pygame.display.update()
        FramePerSec.tick(60)
        return
        # TODO: Actualiza los graficos de los objetos con su posicion
        # TODO: Corre update() en el PhysicsHandler
