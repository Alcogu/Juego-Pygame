import pygame

from constantes import *

class Orcos(pygame.sprite.Sprite):

    def __init__(self, pos, idg, morc, lim_anim = [0,2], despo = 0):
        pygame.sprite.Sprite.__init__(self)
        self.morc = morc
        self.anm_ini = lim_anim[0]
        self.anm_fin = lim_anim[1]

        self.col = self.anm_ini
        self.dir = despo

        self.image = self.morc[self.dir][self.col]
        self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.velxx = 0
        self.velyy = 0
        self.limitesuperior = 20
        self.idgen = idg

        self.bloques = pygame.sprite.Group()
        self.personajes = pygame.sprite.Group()
        self.margenes = pygame.sprite.Group()

    #Dirección de salida aleatoria
    def CambiarDirOrcs(self):

        eje = random.randrange(100)
        sentido = random.randrange(100)
        if eje > 50:
            if sentido > 50:
                self.vely = -3
                self.dir = 3
            else:
                self.vely = 3
                self.dir = 0
        else:
            if sentido > 50:
                self.velx = -3
                self.dir = 1
            else:
                self.velx = 3
                self.dir = 2

    def update(self):

        if self.velx != self.vely:
            self.image = self.morc[self.dir][self.col]

            if self.col < self.anm_fin:
                self.col+=1
            else:
                self.col=self.anm_ini

        self.rect.x += self.velx
        self.rect.x += self.velxx

        col = pygame.sprite.spritecollide(self, self.margenes, False)
        for mar in col: 
            if self.velx > 0:
                    if self.rect.right > mar.rect.left:
                        self.rect.right = mar.rect.left
                        self.dir = self.dir = 1
                        self.velx = -3
            else:
                    if self.rect.left < mar.rect.right:
                        self.rect.left = mar.rect.right
                        self.dir = self.dir = 2
                        self.velx = 3 

        col = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in col:
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
                    self.dir = self.dir = 1
                    self.velx = -3
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
                    self.dir = self.dir = 2
                    self.velx = 3

        col = pygame.sprite.spritecollide(self, self.personajes, False)
        for p in col:
            if self.velx > 0:
                if self.rect.right > p.rect.left:
                    self.rect.right = p.rect.left
                    self.dir = self.dir = 1
                    self.velx = -3
            else:
                if self.rect.left < p.rect.right:
                    self.rect.left = p.rect.right
                    self.dir = self.dir = 2
                    self.velx = 3
            p.salud -= 2
<<<<<<< HEAD
 
        """if self.rect.left < 0:
            self.rect.left = 0
            self.dir = self.dir = 2
            self.velx = 3"""
=======
>>>>>>> e11c6aa57bc935041a1f18dd0c641385ddeae12e

        if self.rect.right > anchoIma:
            self.rect.right = anchoIma
            self.dir = self.dir = 1
            self.velx = -3

        self.rect.y += self.vely
        self.rect.y += self.velyy

        col = pygame.sprite.spritecollide(self, self.margenes, False)
        for mar in col: 
            if self.vely > 0:
                    if self.rect.bottom > mar.rect.top:
                        self.rect.bottom = mar.rect.top
                        self.dir = self.dir = 3
                        self.vely = -3
            else:
                    if self.rect.top < mar.rect.bottom:
                        self.rect.top = mar.rect.bottom
                        self.dir = self.dir = 0
                        self.vely = 3
        
        col = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in col: 
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    self.dir = self.dir = 3
                    self.vely = -3
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                    self.dir = self.dir = 0
                    self.vely = 3

        col = pygame.sprite.spritecollide(self, self.personajes, False)
        for p in col:
            if self.vely > 0:
                if self.rect.bottom > p.rect.top:
                    self.rect.bottom = p.rect.top
                    self.dir = self.dir = 3
                    self.vely = -3
            else:
                if self.rect.top < p.rect.bottom:
                    self.rect.top = p.rect.bottom
                    self.dir = self.dir = 0
                    self.vely = 3
            p.salud -= 2

<<<<<<< HEAD
        """if self.rect.top < self.limitesuperior:
            self.rect.top = self.limitesuperior
            self.dir = self.dir = 0
            self.vely = 3"""

=======
>>>>>>> e11c6aa57bc935041a1f18dd0c641385ddeae12e
        if self.rect.bottom > altoIma:
            self.rect.bottom = altoIma
            self.dir = self.dir = 3
            self.vely = -3
