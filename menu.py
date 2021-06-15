import pygame

from constantes import *

class Menu(pygame.sprite.Sprite):

    def __init__(self):
        self.surface.fill(verdeclaro)
        self.display_text('Presiona una tecla para comenzar', 36, negro, ancho // 2, 10)

        pygame.display.flip()

        self.wait()