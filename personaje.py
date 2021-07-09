import pygame

from constantes import *

class Personaje(pygame.sprite.Sprite):

    def __init__(self, mp, lim_anim = [0,2], desp = 0):
        pygame.sprite.Sprite.__init__(self)
        self.mp = mp
        self.anm_ini = lim_anim[0]
        self.anm_fin = lim_anim[1]

        self.col = self.anm_ini
        self.dir = desp

        self.image = self.mp[self.dir][self.col]
        self.rect = self.image.get_rect()

        self.rect.x = 20
        self.rect.y = 20
        self.velx = 0
        self.vely = 0
        self.salud = 5
        self.contLlaves = 0
        self.limitesuperior = 20
        self.aceleracion = 0

        self.bloques = pygame.sprite.Group()
        self.generadores = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.modificadores = pygame.sprite.Group()
        self.llaves = pygame.sprite.Group()
        self.orcos = pygame.sprite.Group()

        #Sounds
        self.morir = pygame.mixer.Sound('sounds/muerte.wav')
        self.ganar = pygame.mixer.Sound('sounds/ganar.wav')
        self.soundkey = pygame.mixer.Sound('sounds/coin.wav')

    def update(self):
        if self.velx != self.vely:
            self.image = self.mp[self.dir][self.col]

            if self.col < self.anm_fin:
                self.col += 1
            else:
                self.col = self.anm_ini

        self.rect.x += self.velx
            
        col = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in col: 
            if self.velx > 0:
                    self.rect.right = b.rect.left
            else:
                    self.rect.left = b.rect.right
            self.velx = 0

        col = pygame.sprite.spritecollide(self, self.generadores, False)
        for g in col: 
            if self.velx > 0:
                    self.rect.right = g.rect.left
            else:
                    self.rect.left = g.rect.right
            self.velx = 0

        col = pygame.sprite.spritecollide(self, self.enemigos, False)
        for e in col:
            if self.velx > 0:
                    self.rect.right = e.rect.left
            else:
                    self.rect.left = e.rect.right
            self.velx = 0

        col = pygame.sprite.spritecollide(self, self.orcos, False)
        for o in col:
            if self.velx > 0:
                    self.rect.right = o.rect.left
            else:
                    self.rect.left = o.rect.right
            self.velx = 0

        col = pygame.sprite.spritecollide(self, self.modificadores, True)
        for m in col:
            self.salud += 1

        col = pygame.sprite.spritecollide(self, self.llaves, True)
        for k in col:
            self.soundkey.play()
            self.contLlaves += 1
            

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > ancho:
            self.rect.right = ancho

        self.rect.y += self.vely
        
        col = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in col: 
            if self.vely > 0:
                    self.rect.bottom = b.rect.top
            else:
                    self.rect.top = b.rect.bottom
            self.vely = 0
        
        col = pygame.sprite.spritecollide(self, self.generadores, False)

        for g in col: 
            if self.vely > 0:
                    self.rect.bottom = g.rect.top
            else:
                    self.rect.top = g.rect.bottom
            self.vely = 0

        col = pygame.sprite.spritecollide(self, self.enemigos, False)
        for e in col: 
            if self.vely > 0:
                    self.rect.bottom = e.rect.top
            else:
                    self.rect.top = e.rect.bottom
            self.vely=0

        col = pygame.sprite.spritecollide(self, self.orcos, False)
        for o in col: 
            if self.vely > 0:
                    self.rect.bottom = o.rect.top
            else:
                    self.rect.top = o.rect.bottom
            self.vely=0

        if self.rect.top < self.limitesuperior:
            self.rect.top = self.limitesuperior

        if self.rect.bottom > alto:
            self.rect.bottom = alto
