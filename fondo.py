import pygame

from constantes import *

class Fondo(pygame.sprite.Sprite):

    def __init__(self, m):
        pygame.sprite.Sprite.__init__(self)
        self.fondo = m
        self.image = self.fondo
        self.rect = self.image.get_rect()
        info = m.get_rect()
        self.f_ancho=info[2]
        self.f_alto=info[3]
        self.rect.x = 0
        self.rect.y = 0
        self.velx = 0
        self.vely = 0

        #Variable de posicion en X y Y
        self.f_x = 0
        self.f_y = 0
        self.f_xleft = 0
        self.f_yup = 20

        #Variable de velocidad de desplazamiento en X y Y
        self.f_vx = 0
        self.f_vy = 0
        self.f_vxleft = 0
        self.f_vyup = 0
        
        #Limite de desplzamiento hacia adelante y abajo
        self.f_limx = ancho - self.f_ancho
        self.f_limy = alto - self.f_alto

        #Se debe cambiar orden para los otros sentidos
        self.f_limx_positivo = self.f_ancho - ancho
        self.f_limy_positivo = self.f_alto - alto

        #Limites para avanzar o retroceder
        self.lim_d = ancho - 50
        self.lim_a = alto - 50
        self.lim_up = 50
        self.lim_iz = 50