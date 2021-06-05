import pygame
import sys
from personaje import Personaje
from matriz import recorte
from bloques import Bloques
from fondo import Fondo

azul = [76,160,233]
rojo = [245,15,15]
verde = [47, 163, 41]
blanco = [255,255,255]
negro = [0,0,0]

ancho = 640
alto = 420

if __name__ == "__main__":
    pygame.init()
    pantallaprincipal = pygame.display.set_mode([ancho, alto])
    pantalla = pygame.Surface((ancho, alto-30))
    pygame.display.set_caption("Video Juego")
    fuente = pygame.font.Font('freesansbold.ttf', 25)

    #Música de fondo
    pygame.mixer.music.load('Juego-Pygame/sounds/mdf.wav')
    #Primer valor para que la cancion no debe de sonar y segundo punto de inicio de la cancion
    pygame.mixer.music.play(-1, 0.0)
    #La canción va bajando volumen a medida que se va terminando
    #pygame.mixer.music.fadeout(50000)
    
    #grupos
    fondos=pygame.sprite.Group()
    personajes=pygame.sprite.Group()
    bloques = pygame.sprite.Group()

    #Imagenes
    imgFondo = pygame.image.load('Juego-Pygame/imagenes/fondoprado2.jpg')
    imgPersonaje = pygame.image.load('Juego-Pygame/imagenes/centauros.png')
    imgBloque = pygame.image.load('Juego-Pygame/imagenes/bloques.png')

    f=Fondo(imgFondo)
    fondos.add(f)
    
    #Recorte imagen del PJ
    sp_ancho=12
    sp_alto=8
    m=recorte(sp_ancho, sp_alto, imgPersonaje)

    #Eleccion del pj y sus movimientos
    desp=0
    p=Personaje(m, [0, 2], desp)
    personajes.add(p)

    #Recorte de la imagen para los bloques
    bl_ancho=2
    bl_alto=12
    mb=recorte(bl_ancho, bl_alto, imgBloque)

    b=Bloques([120, 120], mb, [0, 0], despb=0)
    bloques.add(b)

    b=Bloques([210, 210], mb, [1, 1], despb=0)
    bloques.add(b)

    b=Bloques([645, 10], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([1200, 340], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([1600, 332], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([1700, 85], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([1800, 175], mb, [1, 1], despb=9)
    bloques.add(b)
    
    """b=Bloques([2200, 175], mb, [1, 1], despb=9)
    bloques.add(b)

    b=Bloques([2800, 200], mb, [1, 1], despb=6)
    bloques.add(b)
    
    b=Bloques([3500, 200], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([4500, 200], mb, [1, 1], despb=9)
    bloques.add(b)

    b=Bloques([5500, 200], mb, [1, 1], despb=9)
    bloques.add(b)"""

    b=Bloques([200, 200], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([200, 200], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([200, 200], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([200, 200], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([200, 200], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([200, 200], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([200, 200], mb, [1, 1], despb=6)
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

            #PJ sin movimiento
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
    
        #Movimiento en mapa hacia la derecha
        if p.rect.right > f.lim_d:
            p.rect.right = f.lim_d
            f.f_vx = -5
        else:
            f.f_vx = 0

        #Movimiento en mapa hacia abajo
        if p.rect.bottom > f.lim_a:
            p.rect.bottom = f.lim_a
            f.f_vy = -5
        else:
            f.f_vy = 0

        for b in bloques:
            b.velx = f.f_vx   
            b.vely = f.f_vy
            
        #Actualizaciones
        personajes.update()
        bloques.update()

        #Tiempo transcurrido de la partida
        tiempo = pygame.time.get_ticks() // 1000
        info = "Tiempo: " + str(tiempo)
        texto = fuente.render(info, False, blanco)

        #Se dibuja en pantalla
        pantallaprincipal.fill(negro)
        pantallaprincipal.blit(pantalla, (0,30))
        pantalla.blit(imgFondo,[f.f_x, f.f_y])
        pantallaprincipal.blit(texto, [2, 2])
        personajes.draw(pantalla)
        bloques.draw(pantalla)

        pygame.display.flip()
        reloj.tick(70)

        #Desplazamiento de la pantalla en la imagen de fondo a la derecha
        if f.f_x > f.f_limx:
            f.f_x+=f.f_vx

        #Desplazamiento de la pantalla en la imagen de fondo a abajo
        if f.f_y > f.f_limy:
            f.f_y+=f.f_vy