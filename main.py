import pygame
import sys

from personaje import Personaje
from bloques import Bloques
from fondo import Fondo
from generador import Generador
from enemigos import Enemigos
from modificadores import Modificadores
from indicadores import Indicadores
from funciones import recorte
from funciones import corazon
from imagenes import *
from constantes import *

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption("Video Juego")
    fuente = pygame.font.Font('freesansbold.ttf', 25)

    musicaFondo = pygame.mixer.Sound('sounds/mdf.wav')
    musicaFondo.play()
    
    #grupos
    fondos = pygame.sprite.Group()
    personajes = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    generadores = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    modificadores = pygame.sprite.Group()
    indicadores = pygame.sprite.Group()

    f = Fondo(imgFondo)
    fondos.add(f)

    #Ciclo presentacion
    seguir = False

    while True and not seguir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                seguir = True

        texto = fuente.render("¡¡¡Bienvenido!!! ", True, blanco)
        texto2 = fuente.render("Preciona una tecla para jugar", True, blanco)
        pantalla.blit(texto, [100,100])
        pantalla.blit(texto2, [100,200])
        pygame.display.flip()

    #recorte items
    items_ancho = 16
    items_alto = 4
    mi = recorte(items_ancho, items_alto, imgItems)

    #Modificador Salud
    m = Modificadores([posRandomX, posRandomY], mi, [11, 1], despm = 0)
    modificadores.add(m)

    m = Modificadores([posRandomX1, posRandomY1], mi, [11, 1], despm = 0)
    modificadores.add(m)

    m = Modificadores([posRandomX2, posRandomY2], mi, [11, 1], despm = 0)
    modificadores.add(m)

    m = Modificadores([posRandomX3, posRandomY3], mi, [11, 1], despm = 0)
    modificadores.add(m)

    #recorte generador
    gen_ancho = 4
    gen_alto = 5
    mg = recorte(gen_ancho, gen_alto, imgGenerador)
    
    #Generador
    ls_gen = [(350, 90), (500, 200), (100, 200)]
    con = 0
    for p in ls_gen:
        g = Generador(con, p, mg, [1, 1], despg=0)
        con += 1
        g.limiteEnemigos = limiteEnemigos
        generadores.add(g)

    """g = Generador([350, 1100], mg, [1, 1], despg=0)
    g.limite=limite
    generadores.add(g)

    g = Generador([1600, 75], mg, [1, 1], despg=0)
    g.limite=limite
    generadores.add(g)

    g = Generador([1600, 1100], mg, [1, 1], despg=0)
    g.limite=limite
    generadores.add(g)"""

    #Recorte imagen del PJ
    sp_ancho = 12
    sp_alto = 8
    m = recorte(sp_ancho, sp_alto, imgPersonaje)

    #Eleccion del pj y sus movimientos
    desp = 0
    p = Personaje(m, [3, 5], desp)
    personajes.add(p)

    cantCoras=p.salud

    #Recorte imagen de Enemigos
    en_ancho = 3
    en_alto = 4
    me = recorte(en_ancho, en_alto, imgEnemigo)

    #Recorte de la imagen para los bloques
    bl_ancho = 2
    bl_alto = 12
    mb = recorte(bl_ancho, bl_alto, imgBloque)

    b = Bloques([100, 120], mb, [0, 0], despb=0)
    bloques.add(b)

    b = Bloques([210, 210], mb, [1, 1], despb=3)
    bloques.add(b)

    b = Bloques([645, 10], mb, [1, 1], despb=6)
    bloques.add(b)

    b = Bloques([1200, 340], mb, [1, 1], despb=9)
    bloques.add(b)

    b = Bloques([1600, 332], mb, [1, 1], despb=0)
    bloques.add(b)

    b = Bloques([1850, 85], mb, [1, 1], despb=3)
    bloques.add(b)
    
    b = Bloques([140, 510], mb, [0, 0], despb=6)
    bloques.add(b)

    b = Bloques([400, 786], mb, [1, 1], despb=9)
    bloques.add(b)

    b = Bloques([679, 499], mb, [1, 1], despb=0)
    bloques.add(b)

    b = Bloques([899, 601], mb, [1, 1], despb=3)
    bloques.add(b)

    b = Bloques([1100, 807], mb, [1, 1], despb=6)
    bloques.add(b)

    b = Bloques([1596, 510], mb, [1, 1], despb=9)
    bloques.add(b)

    b = Bloques([1763, 499], mb, [1, 1], despb=0)
    bloques.add(b)

    b = Bloques([350, 998], mb, [1, 1], despb=3)
    bloques.add(b)

    b = Bloques([570, 1150], mb, [1, 1], despb=6)
    bloques.add(b)

    b = Bloques([759, 1000], mb, [1, 1], despb=9)
    bloques.add(b)

    b = Bloques([1090, 890], mb, [1, 1], despb=0)
    bloques.add(b)

    b = Bloques([1350, 915], mb, [1, 1], despb=3)
    bloques.add(b)

    b = Bloques([1610, 1130], mb, [1, 1], despb=6)
    bloques.add(b)

    b = Bloques([1850, 1199], mb, [1, 1], despb=9)
    bloques.add(b)

    p.bloques = bloques
    p.generadores = generadores
    p.enemigos = enemigos
    p.modificadores = modificadores
    p.indicadores = indicadores

    reloj = pygame.time.Clock()
    ganar = False
    perder = False
    
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

        #Generador de perros esqueletos
        for g in generadores:
            #if g.crear and (g.limiteEnemigos > len(enemigos)):
            if g.pob < g.lim:
                e = Enemigos((g.RetPos()), g.id, me, despe = 1)
                e.CambiarDir()
                enemigos.add(e)
                #g.crear = False
                g.pob += 1

                e.bloques = bloques
                e.personajes = personajes

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

        for g in generadores:
            g.velx = f.f_vx   
            g.vely = f.f_vy

        #Condición para fin de juego por salud
        for p in personajes:
            if p.salud <= 0:
                personajes.remove(p)
                perder = True
        if perder:
            break

        #Actualizaciones
        personajes.update()
        bloques.update()
        generadores.update()
        enemigos.update()
        modificadores.update()
        indicadores.update()
        
        #Tiempo transcurrido de la partida
        tiempo = pygame.time.get_ticks() // 1000
        infoTime = "Tiempo: " + str(tiempo)
        texto = fuente.render(infoTime, False, blanco)

        #Salud del personaje
        infoSalud = "Salud: "
        textoSalud = fuente.render(infoSalud, False, blanco)

        pantalla.blit(imgFondo, [f.f_x, f.f_y])
        pantalla.blit(textoSalud, [2, 2])
        pantalla.blit(texto, [500, 2])

        #Aumento de corazones por generador
        for s in range(p.salud):
            espacio = 30 * s
            corazon(pantalla, [90 + espacio, 10], rojo)
            #indi = Indicadores([80 + espacio, 3], mi, [11, 1], despi = 0)
            #indicadores.add(indi)

        personajes.draw(pantalla)
        bloques.draw(pantalla)
        generadores.draw(pantalla)
        enemigos.draw(pantalla)
        modificadores.draw(pantalla)
        indicadores.draw(pantalla)
        
        pygame.display.flip()
        reloj.tick(40)

        #Desplazamiento de la pantalla en la imagen de fondo a la derecha
        if f.f_x > f.f_limx:
            f.f_x += f.f_vx

        #Desplazamiento de la pantalla en la imagen de fondo a abajo
        if f.f_y > f.f_limy:
            f.f_y += f.f_vy

        #Mensaje fin del juego
    if perder:
        pygame.mixer.pause()
        p.morir.play()
        pantalla.fill(negro)
        pantalla.blit(imgGameOver, [-60, -60])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
