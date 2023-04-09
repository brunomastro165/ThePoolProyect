import pygame, sys
import pymunk
import pymunk.pygame_util
import button
import mesa
from pygame.locals import *

#Funcion para cargar imagenes
def imageLoad(name):
    return pygame.image.load(name)

#Funcion para hacer resposive los botones
def resposiveHitbox(object,pos):
    object.x = (window.get_width() - 800) / 2 + pos
    object.hitbox = pygame.Rect(object.x, object.y, object.width, object.height)

#Variables de la Resolucion
base_width = 800
base_height = 800

#Condicion para cambiar de pantalla
main = True
menu = False
start = False
data = False

posX = 0
posY = 0

#Color Blanco
white_color = (255,255,255)

#Iniciar Pygame, hacer la ventana como una variable con la resolucion y poner el nombre del juego
pygame.init()
window = pygame.display.set_mode((base_width, base_height), pygame.RESIZABLE)
pygame.display.set_caption("PoolGame")
clock = pygame.time.Clock()

#Cargando Imagenes

#Pantalla Principal
game = imageLoad("PLAY.png")
game_start_click = imageLoad("PLAY (ACTIVE).png")
game_menu_click = imageLoad("MENU (ACTIVE).png")
game_data_click = imageLoad("PLAY DATOS.png")

#Pantalla de Datos
data_image = imageLoad("DATOS (PAGINA).png")
data_return = imageLoad("DATOS (PAG ACTIVA).png")

"""
Esto no se usa todavía y capaz no se use
right = False
left = False
up = False
down = False
"""
#BOTONES

#BOTONES PANTALLA PRINCIPAL
start_hitbox = button.Button(231,568, 575-231, 675-568)
menu_hitbox = button.Button(300, 696, 500 -300, 759 -696)
data_hitbox = button.Button(714, 706, 778-714, 782 - 706)

#BOTÓN BACK EN DATOS
data_return_hitbox = button.Button(12, 18, 165-12, 64-18)

#SECCIÓN DE MÚSICA
pygame.mixer.music.load('easy-lifestyle-137766.mp3') #agregar música
pygame.mixer.music.play(-1) #reproducir música en bucle
pygame.mixer.music.set_volume(0.1) #setear volumen

#hacer cada línea individualmente, para poder rodear la imagen con la hitbox
topLine = mesa.MesaObject(100, 50, 500, 10)
leftLine = mesa.MesaObject(100, 50, 10, 650)
botLine = mesa.MesaObject(100, 700, 500, 10)
rightLine = mesa.MesaObject(600, 50, 10, 660)
"""
print(f"Hitbox de la línea superior: {topLine.hitbox}")
print(f"Hitbox de la línea izquierda: {leftLine.hitbox}")
print(f"Hitbox de la línea inferior: {botLine.hitbox}")
print(f"Hitbox de la línea derecha: {rightLine.hitbox}")
"""
window.fill(white_color)


while True:
    # mouse_x, mouse_y = pygame.mouse.get_pos()  # posición cartesiana del mouse

    #Este for revisa cada evento posible
    for event in pygame.event.get():

        #Revisa si la resolucion varia para ajustase
        if event.type == pygame.VIDEORESIZE:
            for hitbox, value in zip([start_hitbox, menu_hitbox, data_hitbox, data_return_hitbox], [231, 300, 714, 12]):
                resposiveHitbox(hitbox, value)
                window.fill(white_color)
                posX = (window.get_width() - 800) / 2
                posY = (window.get_height() - 800) / 2

        #VENTANA DE JUEGO
        if start == True:
            # dibujamos la hitbox
            window.fill(white_color)
            leftLine.draw(window)
            botLine.draw(window)
            rightLine.draw(window)
            topLine.draw(window)
            pygame.mixer.music.stop()  # detener la música
            # window.blit(mesa_pool_, (posX, posY))

        # VENTANA MENU
        if menu == True:
            window.fill(white_color)
            pygame.mixer.music.stop()

        # VENTANA DATOS
        if data == True:
            pygame.mixer.music.stop()
            # No sé por qué funciona solo con down, pero si le pongo up se rompe, funciona perfecto de todas formas
            if data_return_hitbox.down(event) == True:
                window.blit(data_return, (posX, posY))
            else:
                window.blit(data_image, (posX, posY))
            if data_return_hitbox.up(event) == True:
                data = False

        # Animacion de Botones y cambio de pestañas
        # START
        if start == menu == data == False and start_hitbox.down(event) == True:
            window.blit(game_start_click, (posX, posY))
            start = True
        # MENU
        elif start == menu == data == False and menu_hitbox.down(event) == True:
            window.blit(game_menu_click, (posX, posY))
            menu = True
        # DATOS
        elif start == menu == data == False and data_hitbox.down(event) == True:
            window.blit(game_data_click, (posX, posY))
            data = True
        # Pantalla principal
        elif start == menu == data == False:
            window.blit(game, (posX, posY))

        #Es innecesario poner el .up event, esto provoca el error de los botones
            '''
        # Abriendo otras pantallas
        if start == menu == False and start_hitbox.up(event) == True:
            start = True
        if start == menu == False and menu_hitbox.up(event) == True:
            menu = True
        if start == menu == False and data_hitbox.up(event) == True:
            data = True
            '''

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

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #print(pygame.mouse.get_pos())
    clock.tick(60)
    pygame.display.flip()