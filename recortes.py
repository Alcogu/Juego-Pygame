from funciones import recorte
from imagenes import *

#recorte items
items_ancho = 16
items_alto = 4
mi = recorte(items_ancho, items_alto, imgItems)

#recorte generador
gen_ancho = 4
gen_alto = 5
mg = recorte(gen_ancho, gen_alto, imgGenerador)

#Recorte imagen del PJ
sp_ancho = 12
sp_alto = 8
mp = recorte(sp_ancho, sp_alto, imgPersonaje)

#Recorte imagen de Perros
en_ancho = 3
en_alto = 4
me = recorte(en_ancho, en_alto, imgEnemigo)

#Recorte imagen de Orcos
or_ancho = 3
or_alto = 4
mo = recorte(or_ancho, or_alto, imgOrcos)

#Recorte de la imagen para los bloques
bl_ancho = 2
bl_alto = 12
mb = recorte(bl_ancho, bl_alto, imgBloque)