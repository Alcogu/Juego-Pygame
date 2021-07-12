import pygame
import sys
import random

gris =  [135, 133, 133]
azul = [76,160,233]
rojo = [245,15,15]
verde = [47, 163, 41]
negro = [0,0,0]
blanco = [255,255,255]

ancho = 1000
alto = 600


class Rival(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15, 15])
        self.image.fill(rojo)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.radius = 120
        self.velx = 0
        self.vely = -5

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

class Generador(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60, 60])
        self.image.fill(azul)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 500
        self.temp = random.randrange(80, 120)
        #self.crear = False

    def update(self):
        self. temp -= 1

class Linea(pygame.sprite.Sprite):
    def __init__(self, pos, dimension, nueva_vel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(dimension)
        self.image.fill(blanco)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.nueva_velx = nueva_vel[0]
        self.nueva_vely = nueva_vel[1]
        self.tipo = 0

if __name__ == "__main__":
    pygame.init()
    pantalla=pygame.display.set_mode([ancho, alto])

    rivales = pygame.sprite.Group()
    generadores = pygame.sprite.Group()
    lineas = pygame.sprite.Group()

    g = Generador()
    generadores.add(g)

    #ancho 1000 alto 600
    #Poscision, dimensiones, neva velocidad
    l2 = Linea([0, 0], [10, 600], [0, 5])
    l2.tipo = 1
    lineas.add(l2)

    l = Linea([0, 0],[1000, 10], [5, 0])
    lineas.add(l)

    l3 = Linea([0, 590], [1000, 10], [-5, 0])
    lineas.add(l3)

    l4 = Linea([990, 0], [10, 600], [0, -5])
    l4.tipo = 1
    lineas.add(l4)


    reloj=pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        
        #Crear Rivales
        for g in generadores:
            if g.temp < 0:
                r = Rival(g.rect.center)
                rivales.add(r)
                g.temp = random.randrange(80, 120)
        
        for r in rivales:
            if r.rect.x < - 50:
                rivales.remove(r)

        for r in rivales:
            ls_col = pygame.sprite.spritecollide(r, lineas, False)
            for l in ls_col:
                if l.tipo == 0:
                    r.rect.top = l.rect.bottom
                if l.tipo == 1:
                    r.rect.right = l.rect.left
                r.velx = l.nueva_velx
                r.vely = l.nueva_vely
        
        rivales.update()
        generadores.update()

        pantalla.fill(negro)
        rivales.draw(pantalla)
        generadores.draw(pantalla)
        lineas.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)