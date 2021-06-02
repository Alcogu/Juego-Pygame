import pygame
import sys
from personaje import Personaje
from matriz import recorte
from bloques import Bloques

azul = [76,160,233]
rojo = [245,15,15]
verde = [47, 163, 41]
blanco = [255,255,255]
negro = [0,0,0]

ancho = 640
alto = 420

if __name__ == "__main__":
    pygame.init()
    pantalla=pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption("Video Juego")
    fuente = pygame.font.Font(None, 32)

    fondo = pygame.image.load('Juego-Pygame/imagenes/fondoprado.jpg')
    info = fondo.get_rect()
    f_ancho=info[2]
    f_alto=info[3]
    f_x = 0
    f_vx = 0
    f_y = 0
    f_vy = 0
    """f_limx = ancho - f_ancho
    f_limy = alto - f_alto"""
    lim_d = 620
    lim_a = 400
    
    personajes=pygame.sprite.Group()

    sp_ancho=12
    sp_alto=8
    imgPersonaje = pygame.image.load('Juego-Pygame/imagenes/centauros.png')

    m=recorte(sp_ancho, sp_alto, imgPersonaje)

    desp=4
    p=Personaje(m, [0, 2], desp)
    personajes.add(p)

    bloques = pygame.sprite.Group()

    bl_ancho=2
    bl_alto=12
    imgBloque = pygame.image.load('Juego-Pygame/imagenes/bloques.png')

    mb=recorte(bl_ancho, bl_alto, imgBloque)

    b=Bloques([90, 90], mb, [0, 0], despb=3)
    bloques.add(b)

    b=Bloques([200, 200], mb, [1, 1], despb=6)
    bloques.add(b)

    p.bloques=bloques
    
    col=0
    reloj=pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYUP:
                p.velx = 0
                p.vely = 0

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_UP:
                    p.velx = 0
                    p.vely = -5
                    p.dir = desp + 3
                if event.key == pygame.K_DOWN:
                    p.velx = 0
                    p.vely = 5
                    p.dir = desp + 0
                if event.key == pygame.K_RIGHT:
                    p.velx = 5
                    p.vely = 0
                    p.dir = desp + 2
                if event.key == pygame.K_LEFT:
                    p.velx = -5
                    p.vely = 0
                    p.dir = desp + 1
    
        if p.rect.right > lim_d:
            p.rect.right = lim_d
            f_vx = -5
        else:
            f_vx = 0

        if p.rect.bottom > lim_a:
            p.rect.bottom = lim_a
            f_vy = -5
        else:
            f_vy = 0

        for b in bloques:    
            b.vely = f_vy

        for b in bloques:
            b.velx = f_vx
            
        personajes.update()
        bloques.update()

        pantalla.blit(fondo,[f_x, f_y])
        personajes.draw(pantalla)
        bloques.draw(pantalla)

        pygame.display.flip()
        reloj.tick(70)

        """if f_x > f_limx:
            f_x+=f_vx

        if f_y > f_limy:
            f_y+=f_vy"""