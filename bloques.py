import pygame

blanco = [255,255,255]

ancho = 640
alto = 420

class Bloques(pygame.sprite.Sprite):

    def __init__(self, pos, mb, lim_anim=[0,2], despb=0):
        pygame.sprite.Sprite.__init__(self)
        self.mb=mb
        self.anm_ini=lim_anim[0]
        self.anm_fin=lim_anim[1]

        self.col=self.anm_ini
        self.dir=despb

        self.image = self.mb[self.dir][self.col]
        self.rect = self.image.get_rect()
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
