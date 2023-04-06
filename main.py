import pygame, sys
import pymunk
import pymunk.pygame_util
import button
import mesa
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((800, 800)) #settear el tamaño de la ventana
pygame.display.set_caption("PoolGame") #nombre que va a tener la ventana

posX = 0
posY = 0

#CARGADO DE IMAGENES

#PANTALLA PRINCIPAL
pantalla_principal = pygame.image.load("PLAY.png") #cargado de imagen en una variable
pantalla_principal_activa = pygame.image.load("PLAY (ACTIVE).png")
pantalla_principal_menu_active = pygame.image.load("MENU (ACTIVE).png")
pantalla_principal_datos = pygame.image.load("PLAY DATOS.png")

#PANTALLA DATOS
pantalla_datos = pygame.image.load("DATOS (PAGINA).png")
pantalla_datos_activa = pygame.image.load("DATOS (PAG ACTIVA).png")

#para mover una imagen...

velocidad = 200 #variable para el movimiento con teclas
blanco=(255,255,255) #variable que da el color blanco

derecha= False
izquierda = False
arriba = False
abajo = False

#rectangulo_hitbox = pygame.Rect(231,568, 575-231, 675-568) #hitbox del rectángulo de 'play' en la pantalla principal

#uwu
#BOTONES PANTALLA PRINCIPAL
start_hitbox = button.Button(231,568, 575-231, 675-568)
menu_hitbox = button.Button(300, 696, 500 -300, 759 -696)
datos_hitbox = button.Button(714, 706, 778-714, 782- 706)

#BOTÓN BACK EN DATOS
back_datos_hitbox = button.Button(12, 18, 165-12, 64-18)

#SECCIÓN DE MÚSICA
pygame.mixer.music.load('easy-lifestyle-137766.mp3') #agregar música

pygame.mixer.music.play(-1) #reproducir música en bucle

pygame.mixer.music.set_volume(0.1) #setear volumen

window.blit(pantalla_principal, (posX, posY))

#hacer cada línea individualmente, para poder rodear la imagen con la hitbox
topLine = mesa.MesaObject(100, 50, 500, 10)
leftLine = mesa.MesaObject(100, 50, 10, 650)
botLine = mesa.MesaObject(100, 700, 500, 10)
rightLine = mesa.MesaObject(600, 50, 10, 660)


menu = False
start = False #condicion para mostrar la pantalla principal o el 'juego'
principal = True
datos = False

print(f"Hitbox de la línea superior: {topLine.hitbox}")
print(f"Hitbox de la línea izquierda: {leftLine.hitbox}")
print(f"Hitbox de la línea inferior: {botLine.hitbox}")
print(f"Hitbox de la línea derecha: {rightLine.hitbox}")


while True:

    mouse_x,mouse_y = pygame.mouse.get_pos() #posición cartesiana del mouse
    #JUEGO
    if(start == True):
        #dibujamos la hitbox
        #Prueba rojo
        window.fill(blanco)
        leftLine.draw(window)
        botLine.draw(window)
        rightLine.draw(window)
        topLine.draw(window)
        pygame.mixer.music.stop()  # detener la música
        #window.blit(mesa_pool_, (posX, posY))

    #VENTANA MENU
    if(menu == True):
        window.fill(blanco)
        pygame.mixer.music.stop()

    #VENTANA DATOS
    if (datos == True):
        window.blit(pantalla_datos, (posX, posY))
        pygame.mixer.music.stop()

        #No sé por qué funciona solo con down, pero si le pongo up se rompe, funciona perfecto de todas formas
        if back_datos_hitbox.down(event) == True:
            window.blit(pantalla_datos_activa, (posX, posY))
            datos = False

    for event in pygame.event.get(): #event.get() son los eventos prefabricados de pygame
        #1 = izquierdo 2 = rueda 3 = derecho
        #and ((mouse_x >= 229 and mouse_y >= 568) and (mouse_x >= 567 and mouse_y >= 658))

        #Animacion de Botones
        #START
        if start == False and menu == False and datos == False and start_hitbox.down(event) == True:
            window.blit(pantalla_principal_activa, (posX, posY))

        #MENU
        elif start == False and menu == False and datos == False and menu_hitbox.down(event) == True:

            window.blit(pantalla_principal_menu_active, (posX, posY))
        #DATOS
        elif start == False and menu == False and datos == False and datos_hitbox.down(event) == True:
            window.blit(pantalla_principal_datos, (posX,posY))

        #Pantalla principal
        elif (start == False and menu == False and datos == False):
            window.blit(pantalla_principal, (posX, posY))

        #Abriendo otras pantallas
        if start == False and menu == False and start_hitbox.up(event) == True:
            start = True
        if start == False and menu == False and menu_hitbox.up(event) == True:
            menu = True
        if start == False and menu == False and datos_hitbox.up(event) == True:
            datos = True

        #DATOS
       #if(start == False and menu == False):

        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    '''
    #Detectar colisiones (hay que probarlo con las bochas creadas)
    if leftLine.check_collision('bocha'):
        print("Colisión con la línea izquierda")
    elif botLine.check_collision('bocha'):
        print('Colisión con la línea inferior')
    elif rightLine.check_collision('bocha'):
        print('Colisión con la línea derecha')
    elif topLine.check_collision('bocha'):
        print('Colisión con la línea superior')
    '''

    #Mover imágenes con el mouse


    '''
    posX, posY = (pygame.mouse.get_pos())
    posX = posX-100
    posY = posY-100
    '''
    print(pygame.mouse.get_pos())
    pygame.display.update()