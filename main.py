import pygame
import sys

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