import pygame
import sys

from personaje import Personaje
from bloques import Bloques
from fondo import Fondo
from generador import Generador
from enemigos import Enemigos
from orcos import Orcos
from modificadores import Modificadores
from llaves import Llaves
from flecha import Flecha
from funciones import *

from imagenes import *
from constantes import *
from recortes import *

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode([ancho, alto])
    pygame.display.set_caption("Video Juego")
    fuente = pygame.font.Font('freesansbold.ttf', 25)

    #Ciclo presentacion
    presentacion = True

    while True and presentacion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                presentacion = False

        texto2 = fuente.render("Oprime una tecla para empezar la aventura", True, azul)
        texto3 = fuente.render("Debes recolectar las 3 llaves sin dejar", True, verde)
        texto4 = fuente.render(" que te quedes sin salud", True, verde)

        pantalla.blit(texto2, [50,alto//5])
        pantalla.blit(texto3, [90, 240])
        pantalla.blit(texto4, [150, 270])
        pygame.display.flip()

    #grupos
    fondos = pygame.sprite.Group()
    personajes = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    generadores = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    orcos = pygame.sprite.Group()
    modificadores = pygame.sprite.Group()
    llaves = pygame.sprite.Group()
    flechas = pygame.sprite.Group()

    f = Fondo(imgFondo)
    fondos.add(f)

    musicaFondo = pygame.mixer.Sound('sounds/El pueblo.wav')
    musicaFondo.play()

    #Modificador Corazones
    ls_modificadores = ([posRandomX, posRandomY], [posRandomX1, posRandomY1],
                        [posRandomX2, posRandomY2], [posRandomX3, posRandomY3])
    con = 0
    for m in ls_modificadores:
        m = Modificadores(con, m, mi, [11, 1], despm = 0)
        con += 1
        modificadores.add(m)

    #Modificador Llaves
    ls_llaves = ([posLlaveX, posRandomY], [posLlaveX1, posLlaveY1],
                        [posLlaveX2, posLlaveY2])
    con = 0
    for mll in ls_llaves:
        mll = Llaves(con, mll, mi, 13, despll = 2)
        con += 1
        llaves.add(mll)

    #Generador
    ls_gen = [(350, 90), (500, 200), (100, 200), 
    #(350, 1100), (1600, 75), (1600, 1100)
    ]
    con = 0
    for p in ls_gen:
        g = Generador(con, p, mg, [1, 1], despg=0)
        con += 1
        generadores.add(g)

    #Eleccion del pj y sus movimientos
    desp = 0
    p = Personaje(mp, [3, 5], desp)
    personajes.add(p)


    ls_bloques = ([100, 120], [1600, 332], [1090, 890], [679, 499], [1763, 499])
    con = 0
    for b in ls_bloques:
        b = Bloques(con, b, mb, [0, 0], despb = 0)
        con += 1
        bloques.add(b)

    ls_bloques = ([210, 210], [1350, 915], [1850, 85], [899, 601], [350, 998])
    con = 0
    for b in ls_bloques:
        b = Bloques(con, b, mb, [0, 0], despb = 3)
        con += 1
        bloques.add(b)

    ls_bloques = ([645, 10], [140, 510], [1100, 807], [570, 1150], [1610, 1130])
    con = 0
    for b in ls_bloques:
        b = Bloques(con, b, mb, [0, 0], despb = 6)
        con += 1
        bloques.add(b)

    ls_bloques = ([1200, 340], [400, 786], [1596, 510], [759, 1000], [1850, 1199])
    con = 0
    for b in ls_bloques:
        b = Bloques(con, b, mb, [0, 0], despb = 9)
        con += 1
        bloques.add(b)

    p.bloques = bloques
    p.generadores = generadores
    p.enemigos = enemigos
    p.orcos = orcos
    p.modificadores = modificadores
    p.llaves = llaves

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
                    p.orientacion = 1
                if event.key == pygame.K_DOWN:
                    p.velx = 0
                    p.vely = 5
                    p.dir = desp + 0
                    p.orientacion = 2
                if event.key == pygame.K_LEFT:
                    p.velx = -5
                    p.vely = 0
                    p.dir = desp + 1
                    p.orientacion = 3
                if event.key == pygame.K_RIGHT:
                    p.velx = 5
                    p.vely = 0
                    p.dir = desp + 2
                    p.orientacion = 4
                if event.key == pygame.K_SPACE and p.orientacion == 1:
                    fle = Flecha(p.rect.midtop, mi, 2, despmfl = 0)
                    flechas.add(fle)
                    fle.vely = -3
                if event.key == pygame.K_SPACE and p.orientacion == 2:
                    fle = Flecha(p.rect.midbottom, mi, 0, despmfl = 0)
                    flechas.add(fle)
                    fle.vely = 3
                if event.key == pygame.K_SPACE and p.orientacion == 3:
                    fle = Flecha(p.rect.midleft, mi, 1, despmfl = 0)
                    flechas.add(fle)
                    fle.velx = -3
                if event.key == pygame.K_SPACE and p.orientacion == 4:
                    fle = Flecha(p.rect.midright, mi, 3, despmfl = 0)
                    flechas.add(fle)
                    fle.velx = 3
             
        #Generador de perros esqueletos y orcos
        for g in generadores:
            if g.crear and (g.pob < g.lim):
                tipo_enemigo = random.randrange(10)
                orientacion = 0

                if tipo_enemigo < 7:
                    e = Enemigos((g.RetPos()), g.id, me, despe = 1)
                    e.CambiarDirDogs()
                    enemigos.add(e)

                    e.bloques = bloques
                    e.personajes = personajes

                else:
                    o = Orcos((g.RetPos()), g.id, mo, despo = 1)
                    o.CambiarDirOrcs()
                    orcos.add(o)

                    o.bloques = bloques
                    o.personajes = personajes

                g.temp = 200
                g.crear = False
                g.pob += 1

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

        for m in modificadores:
            m.velx = f.f_vx   
            m.vely = f.f_vy

        for mll in llaves:
            mll.velx = f.f_vx   
            mll.vely = f.f_vy

        #Condición para fin de juego por salud
        for p in personajes:
            if p.salud <= 0:
                perder = True
        if perder:
            break

        #Condición para fin de juego por victoria
        for p in personajes:
            if p.contLlaves == 3:
                ganar = True
        if ganar:
            break

        #Actualizaciones
        personajes.update()
        bloques.update()
        generadores.update()
        enemigos.update()
        orcos.update()
        modificadores.update()
        llaves.update()
        flechas.update()
        
        #Tiempo transcurrido de la partida
        tiempo = pygame.time.get_ticks() // 1000
        infoTime = "Tiempo: " + str(tiempo)
        texto = fuente.render(infoTime, False, morado)

        #Salud del personaje
        infoSalud = "Salud: "
        textoSalud = fuente.render(infoSalud, False, rojo)

        #Llaves obtenidas
        infoLlaves = "Llaves: " + str(p.contLlaves)
        textoLlaves = fuente.render(infoLlaves, False, dorado)

        pantalla.blit(imgFondo, [f.f_x, f.f_y])
        pantalla.blit(textoSalud, [2, 2])
        pantalla.blit(texto, [500, 2])
        pantalla.blit(textoLlaves, [300, 2])

        #Aumento de corazones por generador
        for s in range(p.salud):
            espacio = 20 * s
            corazon(pantalla, [90 + espacio, 10], rojo)

        personajes.draw(pantalla)
        bloques.draw(pantalla)
        generadores.draw(pantalla)
        enemigos.draw(pantalla)
        orcos.draw(pantalla)
        modificadores.draw(pantalla)
        llaves.draw(pantalla)
        flechas.draw(pantalla)
        
        pygame.display.flip()
        reloj.tick(30)

        #Desplazamiento de la pantalla en la imagen de fondo a la derecha
        if f.f_x > f.f_limx:
            f.f_x += f.f_vx

        #Desplazamiento de la pantalla en la imagen de fondo a abajo
        if f.f_y > f.f_limy:
            f.f_y += f.f_vy

    #Game Over
    if perder:
        pygame.mixer.pause()
        p.morir.play()
        pantalla.blit(imgGameOver, [-60, -60])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
    
    #Winner
    if ganar:
        pygame.mixer.pause()
        p.ganar.play()
        pantalla.blit(imgWinner, [-90, 0])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
