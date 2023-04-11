import pygame, sys
import pymunk
import pymunk.pygame_util
import button
import mesa
import palo
import ball
from pygame.locals import *

# Funcion para cargar imagenes
def imageLoad(name):
        return pygame.image.load(name)

# Funcion para hacer resposive los botones
def resposiveHitbox(object, pos):
    object.x = (window.get_width() - 800) / 2 + pos
    object.hitbox = pygame.Rect(object.x, object.y, object.width, object.height)

def playMusic():
    pygame.mixer.music.play(-1)  # reproducir música en bucle



# Variables de la Resolucion
base_width = 800
base_height = 800

# Variables de posicion
posX = 0
posY = 0

# Color Blanco
white_color = (255, 255, 255)

# Iniciar Pygame, hacer la ventana como una variable con la resolucion y poner el nombre del juego
pygame.init()
# screen_info = pygame.display.Info()
window = pygame.display.set_mode((base_width, base_height), pygame.RESIZABLE)
pygame.display.set_caption("PoolGame")
# Espacio de Pymunk
space = pymunk.Space()

static_body = space.static_body
# Con esta funcion le puedo pedir a pymunk que dibuje las formas que creo, en la ventana
draw_options = pymunk.pygame_util.DrawOptions(window)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Variable de diametro
diam = 36

# Colores
BG = [50, 50, 50]

# Cargando Imagenes

# Pantalla Principal
game = imageLoad("Images/PLAY.png")
game_start_click = imageLoad("Images/PLAY (ACTIVE).png")
game_menu_click = imageLoad("Images/MENU (ACTIVE).png")
game_data_click = imageLoad("Images/PLAY DATOS.png")

# Pantalla de Datos
data_image = imageLoad("Images/DATOS (PAGINA).png")
data_return = imageLoad("Images/DATOS (PAG ACTIVA).png")

# Pantalla PrePlay
prePlayInactive = imageLoad("Images/PrePlayInactive.png")
prePlayPlayerActiveImage = imageLoad("Images/PrePlayPlayerActive.png")
prePlayBotActive = imageLoad("Images/PrePlayBotActive.png")
prePlayBackActive = imageLoad("Images/PrePlayBackActive.png")

table_image = imageLoad("Assets/Images/table.png")
ball_images = []
for i in range(1, 17):
    ball_image = imageLoad(f"Assets/Images/bola{i}.png")
    ball_image = pygame.transform.scale(ball_image, (diam * 2, diam * 2))
    ball_images.append(ball_image)

# BOTONES

# BOTONES PANTALLA PRINCIPAL
start_hitbox = button.Button(231, 568, 575 - 231, 675 - 568)
menu_hitbox = button.Button(300, 696, 500 - 300, 759 - 696)
data_hitbox = button.Button(714, 706, 778 - 714, 782 - 706)

# BOTÓN BACK
return_hitbox = button.Button(12, 18, 165 - 12, 74 - 18)

# BOTONES DE LA PANTALLA DE JUEGO BÁSICA
prePlayPlayerActive_hitbox = button.Button(221, 319, 0, 0)
preBotActive_hitbox = button.Button(221, 441, 0, 0)

# SECCIÓN DE MÚSICA
pygame.mixer.music.load('easy-lifestyle-137766.mp3')  # agregar música
pygame.mixer.music.set_volume(0.1)  # setear volumen

# Variables de la interface
main = True
menu = False
start = False
data = False
prePlay = False
playing = False
playMusic()
window.fill(white_color)

while True:
    # mouse_x, mouse_y = pygame.mouse.get_pos()  # posición cartesiana del mouse

    if playing == False:
    # Este for revisa cada evento posible
        for event in pygame.event.get():

            # Revisa si la resolucion varia para ajustase
            if event.type == pygame.VIDEORESIZE:
                for hitbox, value in zip(
                        [start_hitbox, menu_hitbox, data_hitbox, return_hitbox, prePlayPlayerActive_hitbox,
                         preBotActive_hitbox], [231, 300, 714, 12, 221, 221]):
                    resposiveHitbox(hitbox, value)
                    window.fill(white_color)
                    posX = (window.get_width() - 800) / 2
                    posY = (window.get_height() - 800) / 2
            # Animacion de Botones y cambio de pestañas

            # PANTALLA PRINCIPAL
            if main:

                window.blit(game, (posX, posY))
                # START HOVER
                if start_hitbox.hover(event):
                    window.blit(game_start_click, (posX, posY))
                # MENU HOVER
                if menu_hitbox.hover(event):
                    window.blit(game_menu_click, (posX, posY))
                # DATOS HOVER
                if data_hitbox.hover(event):
                    window.blit(game_data_click, (posX, posY))

                # START DOWN
                if start_hitbox.down(event):
                    main = False
                    start = True
                # MENU DOWN
                if menu_hitbox.down(event):
                    menu = True
                    main = False
                # DATOS DOWN
                if data_hitbox.down(event):
                    data = True
                    main = False

            # VENTANA DE PRE JUEGO
            if start and main == False:

                # Dibujamos la hitbox
                prePlayPlayerActive_hitbox = button.Button(221, 319, 577 - 210, 585 - 502)
                preBotActive_hitbox = button.Button(221, 441, 577 - 210, 585 - 502)

                pygame.mixer.music.stop()
                window.fill(white_color)

                # HOVER

                if return_hitbox.hover(event):
                    window.blit(prePlayBackActive, (posX, posY))

                elif prePlayPlayerActive_hitbox.hover(event):
                    window.blit(prePlayPlayerActiveImage, (posX, posY))

                elif preBotActive_hitbox.hover(event):
                    window.blit(prePlayBotActive, (posX, posY))

                else:
                    window.blit(prePlayInactive, (posX, posY))

                # DOWN

                if prePlayPlayerActive_hitbox.down(event):
                    playMusic()
                    start = False
                    playing = True
                    base_height = 678
                    base_width = 1200
                    window = pygame.display.set_mode((base_width, base_height), pygame.RESIZABLE)

                if return_hitbox.down(event):
                    playMusic()
                    start = False
                    main = True

                if preBotActive_hitbox.down(event):
                    playMusic()
                    start = False
                    main = True

            # VENTANA MENU
            if menu:
                window.fill(white_color)
                pygame.mixer.music.stop()

            # VENTANA DATOS
            if data:

                if return_hitbox.down(event):
                    data = False
                    main = True

                if return_hitbox.hover(event):
                    window.blit(data_return, (posX, posY))

                else:
                    window.blit(data_image, (posX, posY))

            if event.type == QUIT:
                pygame.quit()
                sys.exit()