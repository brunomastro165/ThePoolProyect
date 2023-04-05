import pygame, sys
import mesa
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((800, 800)) #settear el tamaño de la ventana
pygame.display.set_caption("PoolGame") #nombre que va a tener la ventana

posX = 0
posY = 0

pantalla_principal = pygame.image.load("PLAY (1).png") #cargado de imagen en una variable

#para mover una imagen...

velocidad = 200 #variable para el movimiento con teclas
blanco=(255,255,255) #variable que da el color blanco

derecha= False
izquierda = False
arriba = False
abajo = False

rectangulo_hitbox = pygame.Rect(231,568, 575-231, 675-568) #hitbox del rectángulo de 'play' en la pantalla principal

window.blit(pantalla_principal,(posX, posY)) #usar una imagen cómo ventana

pygame.mixer.music.load('easy-lifestyle-137766.mp3') #agregar música

pygame.mixer.music.play(-1) #reproducir música en bucle

pygame.mixer.music.set_volume(0.1) #setear volumen

#objeto mesaDePool creado desde la clase mesa, con sus atributos

#hacer cada línea individualmente, para poder rodear la imagen con la hitbox
topLine = mesa.MesaObject(100, 50, 500, 10)
leftLine = mesa.MesaObject(100, 50, 10, 650)
botLine = mesa.MesaObject(100, 700, 500, 10)
rightLine = mesa.MesaObject(600, 50, 10, 660)

game = False #condicion para mostrar la pantalla principal o el 'juego'

print(f"Hitbox de la línea superior: {topLine.hitbox}")
print(f"Hitbox de la línea izquierda: {leftLine.hitbox}")
print(f"Hitbox de la línea inferior: {botLine.hitbox}")
print(f"Hitbox de la línea derecha: {rightLine.hitbox}")

while True:
    mouse_x,mouse_y = pygame.mouse.get_pos() #posición cartesiana del mouse
    if(game == True):
        #dibujamos la hitbox
        window.fill(blanco)
        leftLine.draw(window)
        botLine.draw(window)
        rightLine.draw(window)
        topLine.draw(window)
        pygame.mixer.music.stop()  # detener la música
        #window.blit(mesa_pool_, (posX, posY))

    for event in pygame.event.get(): #event.get() son los eventos prefabricados de pygame
        #1 = izquierdo 2 = rueda 3 = derecho
        #and ((mouse_x >= 229 and mouse_y >= 568) and (mouse_x >= 567 and mouse_y >= 658))
        if event.type == pygame.MOUSEBUTTONDOWN and game == False:
            mouse_pos = pygame.mouse.get_pos()

            if rectangulo_hitbox.collidepoint(mouse_pos):
                if event.button == 1:
                    game = True

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

    #print(pygame.mouse.get_pos())
    pygame.display.update()