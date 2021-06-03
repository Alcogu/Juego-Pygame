import pygame

ancho = 640
alto = 420

class Fondo(pygame.sprite.Sprite):

    def __init__(self, m):
        pygame.sprite.Sprite.__init__(self)
        self.fondo=m
        self.image=self.fondo
        self.rect=self.image.get_rect()
        self.rect.x= 0
        self.rect.y= 0
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely