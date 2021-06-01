import pygame
import sys
from matriz import recorte

azul = [76,160,233]
rojo = [245,15,15]
verde = [47, 163, 41]
blanco = [255,255,255]
negro = [0,0,0]

ancho = 900
alto = 500

if __name__ == "__main__":
    pygame.init()
    pantalla=pygame.display.set_mode([ancho, alto])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYUP:
                j.velx = 0
                j.vely = 0

            if event.type == pygame.KEYDOWN:
                #Salir con escape
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
       
        pantalla.fill(negro)