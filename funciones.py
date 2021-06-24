import pygame

from constantes import *

#Generador de indice de modificadores
def corazon(pantalla, pos, cl = rojo):
    pos1 = (pos[0]-2, pos[1]+2)
    pos2 = (pos[0], pos[1]+6)
    pos3 = (pos[0]+2, pos[1]+8)
    pos4 = (pos[0]+4, pos[1]+10)
    pos5 = (pos[0]+6, pos[1]+8)
    pos6 = (pos[0]+8, pos[1]+6)
    pos7 = (pos[0]+10, pos[1]+2)
    pos8 = (pos[0]+8, pos[1])
    pos9 = (pos[0]+4, pos[1]+2)
    pos10 = (pos[0]+4, pos[1]+4)
    pos11 = (pos[0]+2, pos[1]+2)
    ptos = (pos, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11)
    pygame.draw.polygon(pantalla, cl, ptos)
    
#---------------------------------------------------------------------------------
#Recorte de matriz para las imagenes    
def recorte(ancho, alto, im):
    #Toma tamaño y coordenadas de la imagen
    info = im.get_rect()
    #Toma las posiciones del ancho y alto de la imagen
    f_ancho = info[2]
    f_alto = info[3]
    #Creación de listas
    matriz = []
    ls = []
    #Cortes de ancho y alto de la imagen
    cut_ancho = int(f_ancho/ancho)
    cut_alto = int(f_alto/alto)
    #Recorrido de las columnas de la matriz
    for i in range(alto):
        ls = []
        #Recorrido de las filas de la matriz
        for j in range(ancho):
            cuadro = im.subsurface((cut_ancho*j), (cut_alto*i), cut_ancho, cut_alto)
            ls.append(cuadro)
        matriz.append(ls)

    return matriz
