
import pygame
from archivos import *
from animaciones import *
W, H = 1200, 600
FPS = 10

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))

# Fondo
fondo = pygame.image.load("ciudad.jpg")
fondo = pygame.transform.scale(fondo, (W, H))

reescalar_imagenes([personaje_quieto],75,85)
reescalar_imagenes([personaje_camina],75,85)
#Personaje:
x_inicial= W/10 
y_inicial= H-100
contador_pasos=0
velocidad= 5
rectangulo_personaje= personaje_camina[0].get_rect()
rectangulo_personaje.x= x_inicial
rectangulo_personaje.y= y_inicial

posicion_actual_x=0

que_hace= "Quieto"

def animar_personaje(pantalla, rectangulo_personaje,accion_personaje):
    global contador_pasos
    

    largo= len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos=0
    #el contador va animando y moviendo el personaje, nos dice que secuencia es
    # print(contador_pasos)
    PANTALLA.blit(accion_personaje[contador_pasos],rectangulo_personaje)
    contador_pasos +=1 #va pasando de la imagen en movimiento 0 a la 1 a la 2 y asi sucesivamente
    
def mover_personaje(rectangulo_personaje: pygame.Rect , velocidad):
    rectangulo_personaje.x += velocidad

def actualizar_pantalla(pantalla, que_hace,rectangulo_personaje, velocidad): 
    match que_hace: #si lo que esta haciendo...
        case "Derecha": #esta a la derecha
            #animar:
            animar_personaje(pantalla,rectangulo_personaje,personaje_camina)
            #mover
            mover_personaje(rectangulo_personaje, velocidad)
        case "Quieto":
            #analizarlo
            animar_personaje(pantalla,rectangulo_personaje, personaje_quieto)



while True:
    RELOJ.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    keys= pygame.key.get_pressed() #teclas presionadas
    if(keys[pygame.K_RIGHT]): #va para la derecha
        que_hace= "Derecha"
    else:
        que_hace="Quieto" #sino esta quieto
    
    PANTALLA.blit(fondo, (0, 0))

    # animar_personaje(PANTALLA, rectangulo_personaje,personaje_quieto)
    actualizar_pantalla(PANTALLA, que_hace, rectangulo_personaje, velocidad)
    # PANTALLA.blit(personaje_quieto[0],rectangulo_personaje)
    
    pygame.display.update()

