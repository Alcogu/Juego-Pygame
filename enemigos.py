import pygame

from constantes import *

class Enemigos(pygame.sprite.Sprite):

    def __init__(self, pos, me, lim_anim = [0,2], despe = 0):
        pygame.sprite.Sprite.__init__(self)
        self.me=me
        self.anm_ini=lim_anim[0]
        self.anm_fin=lim_anim[1]

        self.col=self.anm_ini
        self.dir=despe

        self.image = self.me[self.dir][self.col]
        self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = -5
        self.vely = 0
        self.salud = 100
        self.bloques = pygame.sprite.Group()
        self.generadores = pygame.sprite.Group()
        self.personajes = pygame.sprite.Group()
        self.disparar = False
        self.temp = 10

    def update(self):

        if self.velx != self.vely:
            self.image = self.me[self.dir][self.col]

            if self.col < self.anm_fin:
                self.col+=1
            else:
                self.col=self.anm_ini

        self.rect.x += self.velx
        
        col = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in col: 
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
            self.velx=5

        if self.rect.left < 0:
            self.rect.left = 0
            self.velx = 5
            self.bloques.velx = 0

        if self.rect.right > ancho:
            self.rect.right = ancho
            self.velx = -5
            self.bloques.velx = 0

        col = pygame.sprite.spritecollide(self, self.generadores, False)
        for g in col: 
            if self.velx > 0:
                if self.rect.right > g.rect.left:
                    self.rect.right = g.rect.left
            else:
                if self.rect.left < g.rect.right:
                    self.rect.left = g.rect.right
            self.velx=5

        if self.rect.left < 0:
            self.rect.left = 0
            self.velx = 5
            self.generadores.velx = 0

        if self.rect.right > ancho:
            self.rect.right = ancho
            self.velx = -5
            self.generadores.velx = 0

        col = pygame.sprite.spritecollide(self, self.personajes, False)
        for p in col: 
            if self.velx > 0:
                if self.rect.right > p.rect.left:
                    self.rect.right = p.rect.left
            else:
                if self.rect.left < p.rect.right:
                    self.rect.left = p.rect.right
            self.velx=5

        if self.rect.left < 0:
            self.rect.left = 0
            self.velx = 5
            self.generadores.velx = 0

        if self.rect.right > ancho:
            self.rect.right = ancho
            self.velx = -5
            self.personajes.velx = 0

        self.rect.y += self.vely
        
        col = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in col: 
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
            self.vely=0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > alto:
            self.rect.bottom = alto
            self.bloques.vely = 0
        
        col = pygame.sprite.spritecollide(self, self.generadores, False)

        for g in col: 
            if self.vely > 0:
                if self.rect.bottom > g.rect.top:
                    self.rect.bottom = g.rect.top
            else:
                if self.rect.top < g.rect.bottom:
                    self.rect.top = g.rect.bottom
            self.vely=0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > alto:
            self.rect.bottom = alto
            self.bloques.vely = 0

        col = pygame.sprite.spritecollide(self, self.personajes, False)
        for p in col: 
            if self.vely > 0:
                if self.rect.bottom > p.rect.top:
                    self.rect.bottom = p.rect.top
            else:
                if self.rect.top < p.rect.bottom:
                    self.rect.top = p.rect.bottom
            self.vely=0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > alto:
            self.rect.bottom = alto
            self.personajes.vely = 0