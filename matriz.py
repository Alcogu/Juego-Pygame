
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
