
def recorte(ancho, alto, im):
    info = im.get_rect()
    f_ancho=info[2]
    f_alto=info[3]
    matriz=[]
    ls=[]
    cut_ancho=int(f_ancho/ancho)
    cut_alto=int(f_alto/alto)
    for i in range(alto):
        ls=[]
        for j in range(ancho):
            cuadro = im.subsurface((cut_ancho*j), (cut_alto*i), cut_ancho, cut_alto)
            ls.append(cuadro)
        matriz.append(ls)

    return matriz
