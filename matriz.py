import pygame

def recorte(ancho, alto, im):
    info = im.get_rect()
    f_ancho=info[2]
    f_alto=info[3]
    matriz=[]
    ls=[]
    fila = alto
    col = ancho
    cut_ancho=int(f_ancho/col)
    cut_alto=int(f_alto/fila)
    for i in range(fila):
        ls=[]
        for j in range(col):
            cuadro = im.subsurface((cut_ancho*j), (cut_alto*i), cut_ancho, cut_alto)
            ls.append(cuadro)
        matriz.append(ls)

    return matriz
