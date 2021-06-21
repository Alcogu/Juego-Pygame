import pygame

from constantes import *

class Enemigos(pygame.sprite.Sprite):

    def __init__(self, pos, idg, me, lim_anim = [0,2], despe = 0):
        pygame.sprite.Sprite.__init__(self)
        self.me = me
        self.anm_ini = lim_anim[0]
        self.anm_fin = lim_anim[1]

        self.col = self.anm_ini
        self.dir = despe

        self.image = self.me[self.dir][self.col]
        self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.limitesuperior = 20
        self.idgen = idg

        self.bloques = pygame.sprite.Group()
        self.personajes = pygame.sprite.Group()
        self.indicadores = pygame.sprite.Group()

    #Dirección de salida aleatoria
    def CambiarDir(self):

        eje = random.randrange(100)
        sentido = random.randrange(100)
        if eje > 50:
            if sentido > 50:
                self.vely = -5
            else:
                self.vely = 5
        else:
            if sentido > 50:
                self.velx = -5
            else:
                self.velx = 5

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
            #Si hay desplazamiento en X
            if self.velx > 0:
                #Si el lado derecho del enemigo coliciona con el lado izquierdo del bloque se detiene
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
                    #Cambia la fila del sprite del enemigo
                    self.dir = self.despe = 1
                    #Movimiento hacia la izquierda después de la colición
                    self.velx = -5
            else:
                #Si el lado izquierdo del enemigo coliciona con el lado derecho del bloque se detiene
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
                    #Cambia la fila del sprite del enemigo
                    self.dir = self.despe = 2
                    #Movimiento hacia la derecha después de la colición
                    self.velx = 5

        col = pygame.sprite.spritecollide(self, self.personajes, False)
        for p in col:
            #Si hay desplazamiento en X
            if self.velx > 0:
                #Si el lado derecho del enemigo coliciona con el lado izquierdo del personaje se detiene
                if self.rect.right > p.rect.left:
                    self.rect.right = p.rect.left
                    #Cambia la fila del sprite del enemigo
                    self.dir = self.despe = 1
                    #Movimiento hacia la izquierda después de la colición
                    self.velx = -5
            else:
                #Si el lado izquierdo del enemigo coliciona con el lado derecho del bloque se detiene
                if self.rect.left < p.rect.right:
                    self.rect.left = p.rect.right
                    #Cambia la fila del sprite del enemigo
                    self.dir = self.despe = 2
                    #Movimiento hacia la derecha después de la colición
                    self.velx = 5
            #En caso de colición en el eje X se reduce salud del Personaje
            p.salud -= 1
            #p.indicadores.kill(p.indi)

        #Cambio de sprite y sentido del movimiento en el eje X después de la colición
        #con el limite izquierdo de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
            self.dir = self.despe = 2
            self.velx = 5

        #Cambio de sprite y sentido del movimiento en el eje X después de la colición
        #con el limite derecho de la pantalla
        if self.rect.right > ancho:
            self.rect.right = ancho
            self.dir = self.despe = 1
            self.velx = -5

        self.rect.y += self.vely
        
        col = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in col: 
            if self.vely > 0:
                #Se cambia de sprite y el enemigo se desplaza hacia arriba después de colicionar
                #en el eje Y con el bloque
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    self.dir = self.despe = 3
                    self.vely = -5
            else:
                #Se cambia de sprite y el enemigo se desplaza hacia abajo después de colicionar
                #en el eje Y con el bloque
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                    self.dir = self.despe = 0
                    self.vely = 5

        col = pygame.sprite.spritecollide(self, self.personajes, False)
        for p in col:
            #Si hay desplazamiento en el eje Y
            if self.vely > 0:
                #Se cambia de sprite y el enemigo se desplaza hacia arriba después de colicionar
                #en el eje Y con el personaje
                if self.rect.bottom > p.rect.top:
                    self.rect.bottom = p.rect.top
                    self.dir = self.despe = 3
                    self.vely = -5
            else:
                #Se cambia de sprite y el enemigo se desplaza hacia abajo después de colicionar
                #en el eje Y con el personaje
                if self.rect.top < p.rect.bottom:
                    self.rect.top = p.rect.bottom
                    self.dir = self.despe = 0
                    self.vely = 5
            #Se resta salud al colicionar en el eje Y
            p.salud -= 1

        #Cambio de sprite y sentido del movimiento en el eje Y después de la colición
        #con el limite superior de la pantalla
        if self.rect.top < self.limitesuperior:
            self.rect.top = self.limitesuperior
            self.dir = self.despe = 0
            self.vely = 5

        #Cambio de sprite y sentido del movimiento en el eje Y después de la colición
        #con el limite inferior de la pantalla
        if self.rect.bottom > alto:
            self.rect.bottom = alto
            self.dir = self.despe = 3
            self.vely = -5
