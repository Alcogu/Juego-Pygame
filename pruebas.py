import pygame
import sys 

#Fondo ancho 4000 alto 3000

verde = [47, 163, 41]
blanco = [255,255,255]
ancho = 700
alto = 500
dj = 30

class Jugador(pygame.sprite.Sprite):

    def __init__(self, cl=verde):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([dj, dj])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.velx = 0
        self.vely = 0
        self.salud = 100
        self.bloques = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.velx

        col = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in col: 
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
            self.velx=0

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > ancho:
            self.rect.right = ancho

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
        
class Bloque(pygame.sprite.Sprite):

    def __init__(self, pos, dim, cl=blanco):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(dim)
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption("Video Juego")
    fondo = pygame.image.load('fondo3.jpg')
    info = fondo.get_rect()
    f_ancho=info[2]
    f_alto=info[3]

    #Variable de posicion en X y Y
    f_x = 0
    f_y = 0
    f_xleft = 0
    f_yup = 0

    #Variable de velocidad de desplazamiento en X y Y
    f_vx = 0
    f_vy = 0
    f_vxleft = 0
    f_vyup = 0

    #Limite de desplzamiento hacia adelante y abajo
    f_limx = ancho - f_ancho
    f_limy = alto - f_alto

    #Se debe cambiar orden para los otros sentidos
    f_limx_positivo = f_ancho - ancho
    f_limy_positivo = f_alto - alto

    #Limites para avanzar o retroceder
    lim_d = ancho -1
    lim_a = alto - 1
    lim_up = 1
    lim_iz = 1

    jugadores = pygame.sprite.Group()
    bloques = pygame.sprite.Group()

    """b=Bloque([400,200] , [dj,dj*5])
    bloques.add(b)

    b=Bloque([3800,200] , [dj,dj*5])
    bloques.add(b)"""

    j = Jugador()
    j.bloques=bloques
    jugadores.add(j)
    
    reloj=pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYUP:
                j.velx = 0
                j.vely = 0

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_UP:
                    j.velx = 0
                    j.vely = -10
                if event.key == pygame.K_DOWN:
                    j.velx = 0
                    j.vely = 10
                if event.key == pygame.K_RIGHT:
                    j.velx = 10
                    j.vely = 0
                if event.key == pygame.K_LEFT:
                    j.velx = -10
                    j.vely = 0
            
        #Movimiento en mapa hacia la derecha
        if j.rect.right > lim_d:
            j.rect.right = lim_d
            f_vx = -5
        else:
            f_vx = 0

        #Movimiento en mapa hacia abajo
        if j.rect.bottom > lim_a:
            j.rect.bottom = lim_a
            f_vy = -5
        else:
            f_vy = 0

        #Movimiento en mapa hacia izquierda
        if j.rect.left < lim_iz:
            j.rect.left = lim_iz
            f_vxleft = 5
        else:
            f_vxleft = 0

        #Movimiento en mapa hacia arriba
        if j.rect.top < lim_up:
            j.rect.top = lim_up
            f_vyup = 5
        else:
            f_vyup = 0
        
        """for b in bloques:
            b.velx = f_vx   
            b.vely = f_vy
            b.velx = f_vxleft   
            b.vely = f_vyup"""
        
        jugadores.update()
        bloques.update()

        pantalla.blit(fondo,[f_x, f_y])
        
        jugadores.draw(pantalla)
        #bloques.draw(pantalla)

        pygame.display.flip()
        reloj.tick(50)
        
        #Desplazamiento de la pantalla en la imagen
        if f_x > f_limx:
            f_x += f_vx

        if f_y > f_limy:
            f_y += f_vy
        
        if f_x < f_limx_positivo:
            f_x += f_vxleft

            if f_x > f_vxleft:
                f_x = 0

        if f_y < f_limy_positivo:
            f_y += f_vyup

            if f_y > f_vyup:
                f_y = 0