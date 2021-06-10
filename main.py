import pygame
import sys

from personaje import Personaje
from matriz import recorte
from bloques import Bloques
from fondo import Fondo
from generador import Generador
from enemigos import Enemigos
from constantes import *

if __name__ == "__main__":
    pygame.init()
    pantallaprincipal = pygame.display.set_mode([ancho, alto])
    pantalla = pygame.Surface((ancho, alto-30))
    pygame.display.set_caption("Video Juego")
    fuente = pygame.font.Font('freesansbold.ttf', 25)
    limite = 10

    #Música de fondo
    pygame.mixer.music.load('sounds/mdf.wav')
    #Primer valor para que la cancion no debe de sonar y segundo punto de inicio de la cancion
    pygame.mixer.music.play(-1, 0.0)
    #La canción va bajando volumen a medida que se va terminando
    
    #grupos
    fondos=pygame.sprite.Group()
    personajes=pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    generadores = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()

    #Imagenes
    imgFondo = pygame.image.load('imagenes/fondoprado2.jpg').convert_alpha()
    imgPersonaje = pygame.image.load('imagenes/centauros.png').convert_alpha()
    imgBloque = pygame.image.load('imagenes/bloques.png').convert_alpha()
    imgGenerador = pygame.image.load('imagenes/fosa.png').convert_alpha()
    imgEnemigo = pygame.image.load('imagenes/dogs.png').convert_alpha()

    f=Fondo(imgFondo)
    fondos.add(f)

    #recorte generador
    gen_ancho=4
    gen_alto=5
    mg = recorte(gen_ancho, gen_alto, imgGenerador)
    
    #Generador
    g = Generador([350, 75], mg, [1, 1], despg=0)
    g.limite=limite
    generadores.add(g)

    #Recorte imagen del PJ
    sp_ancho=12
    sp_alto=8
    m = recorte(sp_ancho, sp_alto, imgPersonaje)

    #Eleccion del pj y sus movimientos
    desp=0
    p = Personaje(m, [3, 5], desp)
    personajes.add(p)

    #Recorte imagen de Enemigos
    en_ancho=3
    en_alto=4
    me = recorte(en_ancho, en_alto, imgEnemigo)

    #Recorte de la imagen para los bloques
    bl_ancho=2
    bl_alto=12
    mb=recorte(bl_ancho, bl_alto, imgBloque)

    b=Bloques([100, 120], mb, [0, 0], despb=0)
    bloques.add(b)

    b=Bloques([210, 210], mb, [1, 1], despb=3)
    bloques.add(b)

    b=Bloques([645, 10], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([1200, 340], mb, [1, 1], despb=9)
    bloques.add(b)

    b=Bloques([1600, 332], mb, [1, 1], despb=0)
    bloques.add(b)

    b=Bloques([1850, 85], mb, [1, 1], despb=3)
    bloques.add(b)
    
    b=Bloques([140, 510], mb, [0, 0], despb=6)
    bloques.add(b)

    b=Bloques([400, 786], mb, [1, 1], despb=9)
    bloques.add(b)

    b=Bloques([679, 499], mb, [1, 1], despb=0)
    bloques.add(b)

    b=Bloques([899, 601], mb, [1, 1], despb=3)
    bloques.add(b)

    b=Bloques([1100, 807], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([1596, 510], mb, [1, 1], despb=9)
    bloques.add(b)

    b=Bloques([1763, 499], mb, [1, 1], despb=0)
    bloques.add(b)

    b=Bloques([350, 998], mb, [1, 1], despb=3)
    bloques.add(b)

    b=Bloques([570, 1150], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([759, 1000], mb, [1, 1], despb=9)
    bloques.add(b)

    b=Bloques([1090, 890], mb, [1, 1], despb=0)
    bloques.add(b)

    b=Bloques([1350, 915], mb, [1, 1], despb=3)
    bloques.add(b)

    b=Bloques([1610, 1130], mb, [1, 1], despb=6)
    bloques.add(b)

    b=Bloques([1850, 1199], mb, [1, 1], despb=9)
    bloques.add(b)

    p.bloques = bloques
    p.generadores = generadores
    
    #col=0
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

        for enem in generadores:
            if enem.crear and (enem.limite > len(enemigos)):
                #Crear goma
                e = Enemigos((enem.RetPos()), me, despe=2)
                enemigos.add(e)
                """e.crear=False
                e.temp = 100"""

        for b in bloques:
            b.velx = f.f_vx   
            b.vely = f.f_vy

        for g in generadores:
            g.velx = f.f_vx   
            g.vely = f.f_vy
            
        #Actualizaciones
        personajes.update()
        bloques.update()
        generadores.update()
        enemigos.update()

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
        generadores.draw(pantalla)
        enemigos.draw(pantalla)

        pygame.display.flip()
        reloj.tick(20)

        #Desplazamiento de la pantalla en la imagen de fondo a la derecha
        if f.f_x > f.f_limx:
            f.f_x+=f.f_vx

        #Desplazamiento de la pantalla en la imagen de fondo a abajo
        if f.f_y > f.f_limy:
            f.f_y+=f.f_vy