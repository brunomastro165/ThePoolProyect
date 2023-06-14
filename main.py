import sys
import pymunk.pygame_util
import button
import mesa
import palo
import funciones
import math
import random
import pygame.mixer
from pygame.locals import *
import pygame.font
import IA

# Finalizado
# Callback de colisión
def handle_collision(arbiter, _space, _data):
    # Obtener las formas colisionadas
    shape_a, shape_b = arbiter.shapes

    # Comprobar si las formas son bolas
    if isinstance(shape_a, funciones.MyCircle) and isinstance(shape_b, funciones.MyCircle):
        # Realizar las acciones necesarias cuando hay colisión entre las bolas
        if not taking_shot:
            sound_ball.play()
    return True


# Función para registrar el controlador de colisiones
def register_collision_handler(_space):
    handler = _space.add_collision_handler(0, 0)  # Ajusta los tipos de colisión según tus necesidades
    handler.pre_solve = lambda arbiter, _space, _data: handle_collision(arbiter, space, data)


# Variables de la Resolucion
tS = True
taking_shot = True
base_width = 800
base_height = 800
# pos X e Y de la pantalla
posX = 0
posY = 0
# Colores
white_color = (255, 255, 255)
green_color = (52, 130, 43)
yellow_color = (238, 182, 2)
BG = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (96, 108, 56)
WOOD = (221, 161, 94)
LIGHT_BROWN = (127, 79, 36)
DARK_BLUE = (20, 33, 61)
# Iniciar Pygame, hacer la ventana como una variable con la resolucion y poner el nombre del juego
pygame.init()
window = pygame.display.set_mode((base_width, base_height))
pygame.display.set_caption("PoolGame")

# Cargando Imagenes
# Pantalla Principal
game = pygame.image.load("Assets/Menus/PLAY.png")
game_start_click = pygame.image.load("Assets/Menus/PLAY (ACTIVE).png")
game_menu_click = pygame.image.load("Assets/Menus/MENU (ACTIVE).png")
game_data_click = pygame.image.load("Assets/Menus/PLAY DATOS.png")
# Pantalla de Datos
data_image = pygame.image.load("Assets/Menus/DATOS (PAGINA).png")
data_return = pygame.image.load("Assets/Menus/DATOS (PAG ACTIVA).png")
# Pantalla Menu
# Cargamos Imagenes
imagenPrincpal = pygame.image.load("Assets/Menus/MENU_PRINCIPAL.png")
imagenSiFacil = pygame.image.load("Assets/Menus/M_P_SI_FACIL.png")
imagenSiFacilBack = pygame.image.load("Assets/Menus/M_P_SI_FACIL_BACK.png")
imagenSiMedio = pygame.image.load("Assets/Menus/M_P_SI_MEDIO.png")
imagenSiMedioBack = pygame.image.load("Assets/Menus/M_P_SI_MEDIO_BACK.png")
imagenSiDificil = pygame.image.load("Assets/Menus/M_P_SI_DIFICIL.png")
imagenSiDificilBack = pygame.image.load("Assets/Menus/M_P_SI_DIFICIL_BACK.png")
imagenNoFacil = pygame.image.load("Assets/Menus/M_P_NO_FACIL.png")
imagenNoFacilBack = pygame.image.load("Assets/Menus/M_P_NO_FACIL_BACK.png")
imagenNoMedio = pygame.image.load("Assets/Menus/M_P_NO_MEDIO.png")
imagenNoMedioBack = pygame.image.load("Assets/Menus/M_P_NO_MEDIO_BACK.png")
imagenNoDificil = pygame.image.load("Assets/Menus/M_P_NO_DIFICIL.png")
imagenNoDificilBack = pygame.image.load("Assets/Menus/M_P_NO_DIFICIL_BACK.png")
# Generamos variable para cambiar las imagenes de menu
imagenActual = imagenNoMedio
# Pantalla PrePlay
prePlayInactive = pygame.image.load("Assets/Menus/PrePlayInactive.png")
prePlayPlayerActiveImage = pygame.image.load("Assets/Menus/PrePlayPlayerActive.png")
prePlayBotActive = pygame.image.load("Assets/Menus/PrePlayBotActive.png")
prePlayBackActive = pygame.image.load("Assets/Menus/PrePlayBackActive.png")
# Jugadores, turnos y victorias
jugador1Turno = pygame.image.load("Assets/Menus/j1.png")
jugador2Turno = pygame.image.load("Assets/Menus/j2.png")
turnoActual = pygame.image.load("Assets/Menus/TurnoActual.png")
turnosRestantes1 = pygame.image.load("Assets/Menus/TR1.png")
turnosRestantes2 = pygame.image.load("Assets/Menus/TR2.png")
j1eslisa = pygame.image.load("Assets/Menus/j1eslisas.png")
j1esrayada = pygame.image.load("Assets/Menus/j1esrayada.png")
j2esrayada = pygame.image.load("Assets/Menus/j2esrayada.png")
j2eslisa = pygame.image.load("Assets/Menus/j2eslisas.png")
ganaj1 = pygame.image.load("Assets/Menus/ganaj1.png")
ganaj2 = pygame.image.load("Assets/Menus/ganaj2.png")
# Bolas con poca opacidad
bola1PO = pygame.image.load('Assets/GameAssets/ball1LO.png')
bola2PO = pygame.image.load('Assets/GameAssets/ball2LO.png')
bola3PO = pygame.image.load('Assets/GameAssets/ball3LO.png')
bola4PO = pygame.image.load('Assets/GameAssets/ball4LO.png')
bola5PO = pygame.image.load('Assets/GameAssets/ball5LO.png')
bola6PO = pygame.image.load('Assets/GameAssets/ball6LO.png')
bola7PO = pygame.image.load('Assets/GameAssets/ball7LO.png')
bola8PO = pygame.image.load('Assets/GameAssets/ball8LO.png')
bola9PO = pygame.image.load('Assets/GameAssets/ball9LO.png')
bola10PO = pygame.image.load('Assets/GameAssets/ball10LO.png')
bola11PO = pygame.image.load('Assets/GameAssets/ball11LO.png')
bola12PO = pygame.image.load('Assets/GameAssets/ball12LO.png')
bola13PO = pygame.image.load('Assets/GameAssets/ball13LO.png')
bola14PO = pygame.image.load('Assets/GameAssets/ball14LO.png')
bola15PO = pygame.image.load('Assets/GameAssets/ball15LO.png')

# BOTONES
# BOTONES PANTALLA PRINCIPAL
start_hitbox = button.Button(231, 568, 575 - 231, 675 - 568)
menu_hitbox = button.Button(300, 696, 500 - 300, 759 - 696)
data_hitbox = button.Button(714, 706, 778 - 714, 782 - 706)
# BOTON BACK
return_hitbox = button.Button(12, 18, 165 - 12, 74 - 18)
# BOTONES DE LA PANTALLA DE JUEGO BASICA
prePlayPlayerActive_hitbox = button.Button(221, 319, 577 - 210, 585 - 502)
preBotActive_hitbox = button.Button(221, 441, 577 - 210, 585 - 502)
# BOTONES DE LA PANTALLA MENU
fullscreenSi_hitbox = button.Button(406, 355, 484 - 406, 436 - 355)
fullscreenNo_hitbox = button.Button(621, 360, 700 - 621, 432 - 360)
diffFacil_hitbox = button.Button(404, 474, 695 - 404, 560 - 474)
diffMedio_hitbox = button.Button(405, 574, 693 - 405, 657 - 574)
diffDificil_hitbox = button.Button(407, 684, 697 - 407, 760 - 684)
# SECCION DE MUSICA
# Inicializo el mixer
pygame.mixer.init()
# Musica
pygame.mixer.music.load("Assets/Sound/Jazza Plaza.mp3")  # agregar musica
pygame.mixer.music.set_volume(0.5)  # setear volumen
doom = pygame.mixer.Sound("Assets/Sound/DMusic.mp3")
musicD = False

# Sonidos
palo_sound = pygame.mixer.Sound("Assets/Sound/ball_sound.wav")
change_turn_sound = pygame.mixer.Sound("Assets/Sound/cturn.wav")
ball_in = pygame.mixer.Sound("Assets/Sound/sound_ball_in.mp3")
win_sound = pygame.mixer.Sound("Assets/Sound/win_sound.mp3")
sound_ball = pygame.mixer.Sound("Assets/Sound/balls_collide.wav")

change_turn_sound.set_volume(0.1)

lost_sound = pygame.mixer.Sound("Assets/Sound/lost.mp3")
lost_sound.set_volume(0.5)
# VARIABLES DE LA BARRA DE VOLUMEN
moving_cursor = False
moving_bar = False
cursor = pygame.Rect(0, 0, 0, 0)
default_sound = True
actual_resolution = 800
# hacer cada linea individualmente, para poder rodear la imagen con la hitbox
topLine = mesa.MesaObject(100, 50, 500, 10)
leftLine = mesa.MesaObject(100, 50, 10, 650)
botLine = mesa.MesaObject(100, 700, 500, 10)
rightLine = mesa.MesaObject(600, 50, 10, 660)
window.fill(white_color)
# Condicion para cambiar de pantalla
main = True
menu = False
start = False
data = False
prePlay = False
playing = False
playing_bot = False
funciones.play_music()
# Condiciones para los botones del menu
screenSiPress = False
screenNoPress = True
Facil = False
Medio = True
dificil = False
# Condicion para los turnos
cont = 1
suma_hecha = False
changeTurn = False
turn = True
soundTurn = False
# Condicion de victoria
win = False
p1win = False
p2win = False
defeat_sound = False
winnin_sound = False
one_time = True

# COSAS DE PYMUNK
# Pymunk space
space = pymunk.Space()
static_body = space.static_body

# Con esta funcion le puedo pedir a pymunk que dibuje las formar que creo, en la ventana
draw_options = pymunk.pygame_util.DrawOptions(window)

# Collision Handler
register_collision_handler(space)

# Clock
clock = pygame.time.Clock()
FPS = 75

# Game variables
diam = 40
pocket_dia = 66
force = 0
max_force = 10000
top_force = 0
force_direction = 1
game_started = False

# Shot variables
new_shot = False
powering_up = False

# Balls variables
potted_balls = []
potted_balls_lisa = []
potted_balls_rayada = []
potted_negra = False
potted_blanca = False
ballTeam = True
p1_can_put_black = False
p2_can_put_black = False
contPottedBalls = 0

# Screen variables
FullScreen = False
change_image = True

# Flags variables
unicaVez = False
mostrarBochas = False
bot_active = True
music = False
musicExist = False
mainTheme = True
generalTheme = True

# Bot variables
num = random.randint(0, 2)
bot_balls = []

# load images
table_image = pygame.image.load("Assets/GameAssets/table.png").convert_alpha()
ball_images = []

for i in range(1, 17):
    ball_image = pygame.image.load(f"Assets/GameAssets/bola{i}.png").convert_alpha()
    ball_image = pygame.transform.scale(ball_image, (diam * 2, diam * 2))
    ball_images.append(ball_image)

# Crear las bolas para el juego
balls = []
rows = 5

# Bolas numeradas
for col in range(5):
    for row in range(rows):
        pos = (250 + (col * (diam + 3)), 267 + (row * (diam + 3)) + (col * diam / 2))
        '''COMO LAS BALLS NO SON OBJETOS, NO TIENEN ATRIBUTOS O PARAMETROS, 
        SIMPLEMENTE ES UNA FUNCION QUE DEVUELVE CIERTOS NUMEROS'''
        # ASI QUE SE MODIFICO LA CLASE CIRCLE DE PYMUNK, PARA PODER TENER OBJETOS
        if 8 > len(balls) > 0:
            new_ball = funciones.create_ball((diam / 2), pos, static_body, space)
            new_ball.tipo = "lisa"
        if len(balls) == 0:  # LA ITERACION 0 POR ALGUN MOTIVO ES LA NUMERO 15, Y ES RAYADA, POR ESO ES ESTE IF
            new_ball = funciones.create_ball((diam / 2), pos, static_body, space)
            new_ball.tipo = "rayada"
        if len(balls) > 8:
            new_ball = funciones.create_ball((diam / 2), pos, static_body, space)
            new_ball.tipo = "rayada"
        if len(balls) == 8:
            new_ball = funciones.create_ball((diam / 2), pos, static_body, space)
            new_ball.tipo = "negra"
        if new_ball:
            balls.append(new_ball)
    rows -= 1

# Cambiando las bolas de lugar (acomodandolas para que sean cómo el pool de verdad)
funciones.change_pos(0, 14, balls)
funciones.change_pos(1, 5, balls)
funciones.change_pos(2, 13, balls)
funciones.change_pos(13, 8, balls)
funciones.change_pos(4, 12, balls)
funciones.change_pos(4, 9, balls)
funciones.change_pos(7, 10, balls)
funciones.change_pos(10, 6, balls)
funciones.change_pos(3, 12, balls)
funciones.change_pos(12, 10, balls)

# Bola blanca
pos = (888, (678 / 2))

cue_ball = funciones.create_ball((diam / 2), pos, static_body, space)
cue_ball.tipo = "blanca"
balls.append(cue_ball)
contBalls = 0

for i in balls:
    contBalls = contBalls + 1

# NO BORREN ESTO NUNCA
balls[0].tipo = "lisa"
balls[8].tipo = "rayada"
balls[7].tipo = "negra"

# Crear los bordes de la mesa (usando las coordenadas donde quiero dibujarlos)
border = [
    [(88, 56), (109, 77), (555, 77), (564, 56)],
    [(621, 56), (630, 77), (1081, 77), (1102, 56)],
    [(89, 621), (110, 600), (556, 600), (564, 621)],
    [(622, 621), (630, 600), (1081, 600), (1102, 621)],
    [(56, 96), (77, 117), (77, 560), (56, 581)],
    [(1143, 96), (1122, 117), (1122, 560), (1143, 581)]
]

# Crear los hoyos de la mesa
pockets = [
    (55, 63),
    (592, 48),
    (1134, 64),
    (55, 616),
    (592, 629),
    (1134, 616)
]

bot_pockets = [
    (82, 86),
    (594, 74),
    (1112, 86),
    (82, 592),
    (594, 600),
    (1112, 590)
]

for b in border:
    funciones.create_table_border(b, space)

# Objeto palo (instancia de la clase palo)
palo_p1 = palo.Palo(balls[-1].body.position)

# Imagen para la barra de carga
barra_placeholder = pygame.image.load("Assets/GameAssets/power_bar.png")
barra_placeholder1 = pygame.image.load("Assets/GameAssets/power_bar1.png")
barra_placeholder2 = pygame.image.load("Assets/GameAssets/power_bar2.png")
barra_placeholder3 = pygame.image.load('Assets/GameAssets/power_bar3.png')
barra_placeholder4 = pygame.image.load('Assets/GameAssets/power_bar4.png')

# Barra de poder del palo
power_bar = pygame.Surface((barra_placeholder.get_width(), barra_placeholder.get_height()))
power_bar.blit(barra_placeholder, (0, 0))
power_bar1 = pygame.Surface((barra_placeholder1.get_width(), barra_placeholder1.get_height()))
power_bar1.blit(barra_placeholder1, (0, 0))
power_bar2 = pygame.Surface((barra_placeholder2.get_width(), barra_placeholder2.get_height()))
power_bar2.blit(barra_placeholder2, (0, 0))
power_bar3 = pygame.Surface((barra_placeholder3.get_width(), barra_placeholder3.get_height()))
power_bar3.blit(barra_placeholder3, (0, 0))
power_bar4 = pygame.Surface((barra_placeholder4.get_width(), barra_placeholder4.get_height()))
power_bar4.blit(barra_placeholder4, (0, 0))
aux_rayada = 0
aux_lisa = 0

while True:
    # mouse_x, mouse_y = pygame.mouse.get_pos()  # posicion cartesiana del mouse
    # print(mouse_x ,",", mouse_y)
    if not playing and not playing_bot:
        # Este for revisa cada evento posible
        for event in pygame.event.get():
            # Revisa si la resolucion varia para ajustase
            if event.type == pygame.VIDEORESIZE:
                cursor.x = cursor.x + (window.get_width() - actual_resolution) / 2
                actual_resolution = window.get_width()
                for hitbox, value in zip(
                        [start_hitbox, menu_hitbox, data_hitbox, return_hitbox, prePlayPlayerActive_hitbox,
                         preBotActive_hitbox], [231, 300, 714, 12, 221, 221]):
                    funciones.resposive_hitbox(hitbox, value, window)
                    window.fill(white_color)
                    posX = (window.get_width() - 800) / 2
                    posY = (window.get_height() - 800) / 2
            # Animacion de Botones y cambio de pestanas
            # VENTANA MENU
            if menu:
                # BARRA DE VOLUMEN
                pygame.draw.rect(window, (255, 255, 255), pygame.Rect(389, 222, 736 - 389, 319 - 222))
                # Definir la barra
                bar_width = 300
                bar_height = 10
                bar_x = (window.get_width() - 800) / 2 + 408
                bar_y = (window.get_height() - 800) / 2 + 273
                sound_bar = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
                mouse_state = pygame.mouse.get_pressed()
                # Definir el cursor
                cursor_width = 20
                cursor_height = 40
                if default_sound:
                    x_cursor = bar_x + bar_width / 2
                    y_cursor = bar_y - (cursor_height / 2)
                    cursor = pygame.Rect(x_cursor - cursor_width / 2, y_cursor, cursor_width, cursor_height)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if cursor.collidepoint(event.pos):
                        moving_cursor = True
                        x_cursor, y_cursor = event.pos
                        cursor.x = x_cursor - (cursor_width / 2)
                        default_sound = False
                    elif sound_bar.collidepoint(event.pos):
                        moving_bar = True
                        x_cursor, y_cursor = event.pos
                        cursor.x = x_cursor - (cursor_width / 2)
                        default_sound = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    moving_cursor = False
                    moving_bar = False
                    x_cursor, y_cursor = event.pos  # actualizar posicion del cursor
                elif event.type == pygame.MOUSEMOTION:
                    if moving_cursor:
                        x_cursor, y_cursor = event.pos
                        # asegurarse de que el cursor no se mueva fuera de los limites de la barra
                        if x_cursor < bar_x:
                            x_cursor = bar_x
                        elif x_cursor > bar_x + bar_width - cursor_width:
                            x_cursor = bar_x + bar_width - cursor_width
                        cursor.x = x_cursor - (cursor_width / 2)
                    elif moving_bar:
                        x_cursor, y_cursor = event.pos
                        # asegurarse de que el cursor no se mueva fuera de los limites de la barra
                        if x_cursor < bar_x:
                            x_cursor = bar_x
                        elif x_cursor > bar_x + bar_width - cursor_width:
                            x_cursor = bar_x + bar_width - cursor_width
                        cursor.x = x_cursor - (cursor_width / 2)
                # Calcular el volumen y actualizar la musica
                sound = (cursor.x - bar_x) / bar_width
                pygame.mixer.music.set_volume(sound)
                sound = (cursor.y - bar_y) / bar_height
                pygame.mixer.music.set_volume(sound)
                # VOLVER AL PRINCIPAL
                if return_hitbox.down(event):
                    change_image = True
                    menu = False
                    main = True
                if change_image and not return_hitbox.hover():
                    change_image = False
                    window.blit(imagenActual, (posX, posY))
                # SI ESTA APRETADO SI
                if fullscreenSi_hitbox.down(event):
                    change_image = True
                    screenSiPress = True
                    screenNoPress = False
                    imagenActual = imagenSiMedio
                    FullScreen = True
                # DIFERENCIADOS POR DIFICULTADO
                if diffFacil_hitbox.down(event):
                    change_image = True
                    Medio = False
                    Facil = True
                    dificil = False
                    muiscD = False
                    mainTheme = True

                if diffMedio_hitbox.down(event):
                    change_image = True
                    Medio = True
                    Facil = False
                    dificil = False
                    musicD = False
                    mainTheme = True

                if diffDificil_hitbox.down(event):
                    change_image = True
                    Medio = False
                    Facil = False
                    dificil = True
                    musicD = True
                    music = True
                    musicExist = True
                    mainTheme = False

                # SI ESTA APRETADO NO
                if fullscreenNo_hitbox.down(event):
                    change_image = True
                    screenNoPress = True
                    screenSiPress = False
                    imagenActual = imagenNoMedio
                    FullScreen = False

                # Cosas de frontEnd
                if screenSiPress:
                    if Facil:
                        imagenActual = imagenSiFacil
                        if not change_image and return_hitbox.hover():
                            change_image = True
                            window.blit(imagenSiFacilBack, (posX, posY))

                    if Medio:
                        imagenActual = imagenSiMedio
                        if not change_image and return_hitbox.hover():
                            change_image = True
                            window.blit(imagenSiMedioBack, (posX, posY))

                    if dificil:
                        imagenActual = imagenSiDificil
                        if not change_image and return_hitbox.hover():
                            change_image = True
                            window.blit(imagenSiDificilBack, (posX, posY))

                elif screenNoPress:
                    if Facil:
                        imagenActual = imagenNoFacil
                        if not change_image and return_hitbox.hover():
                            change_image = True
                            window.blit(imagenNoFacilBack, (posX, posY))

                    if Medio:
                        imagenActual = imagenNoMedio
                        if not change_image and return_hitbox.hover():
                            change_image = True
                            window.blit(imagenNoMedioBack, (posX, posY))

                    if dificil:
                        imagenActual = imagenNoDificil
                        if not change_image and return_hitbox.hover():
                            change_image = True
                            window.blit(imagenNoDificilBack, (posX, posY))

                pygame.draw.rect(window, green_color, sound_bar)
                pygame.draw.rect(window, yellow_color, cursor)
            # PANTALLA PRINCIPAL
            if main:
                if change_image and not start_hitbox.hover() and not menu_hitbox.hover() and not data_hitbox.hover():
                    change_image = False
                    window.blit(game, (posX, posY))
                # START HOVER
                if not change_image and start_hitbox.hover():
                    change_image = True
                    window.blit(game_start_click, (posX, posY))
                # MENU HOVER
                if not change_image and menu_hitbox.hover():
                    change_image = True
                    window.blit(game_menu_click, (posX, posY))
                # DATOS HOVER
                if not change_image and data_hitbox.hover():
                    change_image = True
                    window.blit(game_data_click, (posX, posY))
                # START DOWN
                if start_hitbox.down(event):
                    main = False
                    change_image = True
                    start = True
                # MENU DOWN
                if menu_hitbox.down(event):
                    change_image = True
                    menu = True
                    main = False
                # DATOS DOWN
                if data_hitbox.down(event):
                    change_image = True
                    data = True
                    main = False
            # VENTANA DE PRE JUEGO
            if start:
                if change_image and not return_hitbox.hover() and not prePlayPlayerActive_hitbox.hover() \
                        and not preBotActive_hitbox.hover():
                    change_image = False
                    window.blit(prePlayInactive, (posX, posY))
                if not change_image and return_hitbox.hover():
                    change_image = True
                    window.blit(prePlayBackActive, (posX, posY))
                if not change_image and prePlayPlayerActive_hitbox.hover():
                    change_image = True
                    window.blit(prePlayPlayerActiveImage, (posX, posY))
                if not change_image and preBotActive_hitbox.hover():
                    change_image = True
                    window.blit(prePlayBotActive, (posX, posY))
                # DOWN EVENT
                if prePlayPlayerActive_hitbox.down(event):
                    pygame.mixer.music.stop()
                    start = False
                    playing = True
                    base_height = 678
                    base_width = 1200
                    base_bottom_panel = 50
                    if not FullScreen:
                        window = pygame.display.set_mode((base_width + 250, base_height + base_bottom_panel),
                                                         pygame.RESIZABLE)

                    else:
                        screen_info = pygame.display.Info()
                        screen_width = screen_info.current_w
                        screen_height = screen_info.current_h
                        w = (screen_width - base_width) // 2
                        h = (screen_height - base_height + base_bottom_panel) // 2
                        screen_position = (w, h)
                        window = pygame.display.set_mode((base_width + 200, base_height + base_bottom_panel),
                                                         pygame.RESIZABLE)
                        pygame.display.set_mode((base_width + 200, base_height + base_bottom_panel), w, h)

                if return_hitbox.down(event):
                    change_image = True
                    start = False
                    main = True
                if preBotActive_hitbox.down(event):
                    if not dificil:
                        pygame.mixer.music.stop()

                    start = False
                    playing_bot = True
                    base_height = 678
                    base_width = 1200
                    base_bottom_panel = 50
                    if not FullScreen:
                        window = pygame.display.set_mode((base_width + 250, base_height + base_bottom_panel),
                                                         pygame.RESIZABLE)
                    else:
                        screen_info = pygame.display.Info()
                        screen_width = screen_info.current_w
                        screen_height = screen_info.current_h
                        w = (screen_width - base_width) // 2
                        h = (screen_height - base_height + base_bottom_panel) // 2
                        screen_position = (w, h)
                        window = pygame.display.set_mode((base_width + 200, base_height + base_bottom_panel),
                                                         pygame.RESIZABLE)
                        pygame.display.set_mode((base_width + 200, base_height + base_bottom_panel), w, h)

            # VENTANA DATOS
            if data:
                if return_hitbox.down(event):
                    change_image = True
                    data = False
                    main = True
                if change_image and not return_hitbox.hover():
                    change_image = False
                    window.blit(data_image, (posX, posY))
                if not change_image and return_hitbox.hover():
                    change_image = True
                    window.blit(data_return, (posX, posY))
            # Revision de eventos
            # Revisa si aprita el boton para cerrar la aplicacion
            if event.type == QUIT:
                sys.exit()
            # Revisa si aprita el boton ESCAPE para cerrar la aplicacion
            if event.type == event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
    # Parte del loop jugable con el bot
    elif playing_bot:

        if musicD is True:
            pygame.mixer.music.load("Assets/Sound/DMusic.mp3")
            pygame.mixer.music.play(-1)
            musicD = False

        if mainTheme is True:
            pygame.mixer.music.load("Assets/Sound/GameMusic.mp3")
            pygame.mixer.music.play(-1)
            mainTheme = False

        # Time simulation
        clock.tick(FPS)
        space.step(1 / FPS)
        # Fill background
        window.fill(DARK_BLUE)
        # draw pool table
        window.blit(table_image, (0, 0))
        # Aparecen los jugadores al mismo tiempo
        window.blit(jugador1Turno, (1200, 5))
        window.blit(jugador2Turno, (1200, 235))
        if turn:
            if soundTurn:
                change_turn_sound.play()
                soundTurn = False
            if cont >= 0:
                window.blit(turnosRestantes1, (1200, 80))
            elif cont == 0:
                window.blit(turnosRestantes2, (1200, 80))
            elif cont == -1:
                print("3")
        else:
            if soundTurn:
                change_turn_sound.play()
                soundTurn = False
            if cont > 0:
                window.blit(turnosRestantes1, (1200, 312))
            elif cont == 0:
                window.blit(turnosRestantes2, (1200, 312))
            elif cont == -1:
                print("3")

        # Fijarse si cualquier ball toco un hoyo
        for i, ball in enumerate(balls):
            for pocket in pockets:
                ball_x_dist = abs(ball.body.position[0] - pocket[0])
                ball_y_dist = abs(ball.body.position[1] - pocket[1])
                ball_dist = math.sqrt((ball_x_dist ** 2) + (ball_y_dist ** 2))
                if ball_dist <= pocket_dia / 2:
                    ball_in.play()
                    if ball.tipo == "lisa":
                        potted_balls.append(ball_images[i])
                        potted_balls_lisa.append(ball_images[i])
                        ball.body.position = (-1000, contPottedBalls)
                        ball.body.velocity = (0.0, 0.0)
                        space.remove(ball.body)
                        balls.remove(ball)
                        ball_images.pop(i)
                        contPottedBalls = contPottedBalls - 100

                    elif ball.tipo == "rayada":
                        potted_balls.append(ball_images[i])
                        potted_balls_rayada.append(ball_images[i])
                        ball.body.position = (-1000, contPottedBalls)
                        ball.body.velocity = (0.0, 0.0)
                        space.remove(ball.body)
                        balls.remove(ball)
                        ball_images.pop(i)
                        contPottedBalls = contPottedBalls - 100

                    elif ball.tipo == "negra":
                        potted_negra = True
                        potted_balls.append(ball_images[i])
                        space.remove(ball.body)
                        balls.remove(ball)
                        ball_images.pop(i)

                    elif ball.tipo == "blanca":
                        potted_blanca = True
                        ball.body.position = (-100, -100)
                        ball.body.velocity = (0.0, 0.0)

                    contBalls = 0
                    for j in balls:
                        contBalls = contBalls + 1

        # draw pool balls
        # Utilizo el iterador i para obtener el numero de la bola
        # Esto debido a que el iterador ball solo me da la direccion de memoria del objeto ball
        for i, ball in enumerate(balls):
            window.blit(ball_images[i], (ball.body.position[0] - diam, ball.body.position[1] - diam))
            # Checkar si las bolas estan quietas
        taking_shot = True
        for ball in balls:
            if int(ball.body.velocity[0]) != 0 or int(ball.body.velocity[1]) != 0:
                taking_shot = False
                changeTurn = True
        # Si un jugador mete la blanca, le toca al otro jugador durante 2 turnos (como en el pool de verdad)
        # NO MUEVAN ESTO DE ACA, PORQUE MAS ABAJO SE MODIFICA LA VARIABLE Y NO FUNCIONARIA
        if potted_blanca and not unicaVez and not win and not p2win and not p1win:
            turn = not turn
            cont = -1
            unicaVez = True
        # Tipos de bocha para cada jugador
        if ballTeam:
            # Jugador 1
            if len(potted_balls_lisa) > 0 and turn:  # Probado y funciona
                P1LISA = True
                P1RAY = False
                P2LISA = False
                P2RAY = True
                ballTeam = False
                mostrarBochas = True
                cont = 0
            elif len(potted_balls_rayada) > 0 and turn:  # Probado y funciona
                P1LISA = False
                P1RAY = True
                P2LISA = True
                P2RAY = False
                ballTeam = False
                mostrarBochas = True
                cont = 0
            # Jugador 2
            elif len(potted_balls_lisa) > 0 and not turn:  # Probado y funciona
                P1LISA = False
                P1RAY = True
                P2LISA = True
                P2RAY = False
                ballTeam = False
                mostrarBochas = True
                cont = 0
            elif len(potted_balls_rayada) > 0 and not turn:  # Probado y funciona
                P1LISA = True
                P1RAY = False
                P2LISA = False
                P2RAY = True
                ballTeam = False
                mostrarBochas = True
                cont = 0
        # dibujar las bochas metidas en la parte de abajo

        # este comentario
        if mostrarBochas:
            if P1LISA:
                for i, ball in enumerate(potted_balls_lisa):
                    window.blit(ball, (1200 + (i * 20), 110))

                for i, ball in enumerate(potted_balls_rayada):
                    window.blit(ball, (1200 + (i * 20), 335))

            else:
                for i, ball in enumerate(potted_balls_lisa):
                    window.blit(ball, (1200 + (i * 20), 335))

                for i, ball in enumerate(potted_balls_rayada):
                    window.blit(ball, (1200 + (i * 20), 110))

        # CONDICIONES DE VICTORIA
        if not ballTeam and taking_shot:
            if len(potted_balls_lisa) > aux_lisa and len(potted_balls_rayada) > aux_rayada:
                aux_rayada += 1
                aux_lisa += 1
            elif ((P1RAY and turn) or (P2RAY and not turn)) and len(potted_balls_rayada) > aux_rayada:
                aux_rayada += 1
                cont = 0
            elif ((P1LISA and turn) or (P2LISA and not turn)) and len(potted_balls_lisa) > aux_lisa:
                aux_lisa += 1
                cont = 0
            elif ((P1RAY and turn) or (P2RAY and not turn)) and len(potted_balls_lisa) > aux_lisa:
                turn = not turn
                aux_lisa += 1
                cont = -1
            elif ((P1LISA and turn) or (P2LISA and not turn)) and len(potted_balls_rayada) > aux_rayada:
                turn = not turn
                aux_rayada += 1
                cont = -1

            # Meter las bochas correspondientes al equipo
            if (P1LISA and len(potted_balls_lisa) == 7) or (P1RAY and len(potted_balls_rayada) == 7):
                p1_can_put_black = True
            if (P2LISA and len(potted_balls_lisa) == 7) or (P2RAY and len(potted_balls_rayada) == 7):
                p2_can_put_black = True

        # Meter la negra para ganar
        if not win:
            # No cambien el == True por turn porque no funciona
            if p1_can_put_black and potted_negra and turn == True:
                taking_shot = False
                window.blit(ganaj1, (400, 300))
                win = True
                p1win = True

            # No cambien el == False por not turn porque no funciona
            if p2_can_put_black and potted_negra and not turn == False:
                taking_shot = False
                window.blit(ganaj2, (400, 300))
                win = True
                p2win = True

            # Meter la negra antes de tiempo
            if turn and potted_negra and not p1_can_put_black:
                taking_shot = False
                window.blit(ganaj2, (400, 300))
                p2win = True

            if not turn and potted_negra and not p2_can_put_black:
                taking_shot = False
                window.blit(ganaj1, (400, 300))
                p1win = True

        if p1win:
            window.blit(ganaj1, (400, 300))
            bot_active = False
            taking_shot = False
        elif p2win:
            window.blit(ganaj2, (400, 300))
            bot_active = False
            taking_shot = False

        if p1win is True and one_time:
            pygame.mixer.music.stop()
            win_sound.play()
            one_time = False

        if p2win is True and one_time:
            pygame.mixer.music.stop()
            lost_sound.play()
            one_time = False

        if taking_shot:
            if changeTurn:
                soundTurn = True
                changeTurn = False
                cont += 1
                if cont > 1:
                    turn = not turn
            if turn:
                # Sistema de turnos
                if potted_blanca:
                    balls[-1].body.position = (888, base_height / 2)
                    potted_blanca = False
                # Calcular el angulo
                mouse_pos = pygame.mouse.get_pos()
                palo_p1.rect.center = balls[-1].body.position
                x_dist = balls[-1].body.position[0] - mouse_pos[0]
                y_dist = -(balls[-1].body.position[1] - mouse_pos[1])
                palo_angle = math.degrees(math.atan2(y_dist, x_dist))
                palo_p1.update(palo_angle)
                # dibujar palo
                palo_p1.draw(window)
                # Fuerza del golpe
                if powering_up:
                    force += 100 * force_direction
                    if force >= max_force or force <= 0:
                        force_direction *= -1
                    # Dibujar las barras de poder
                    for b in range(math.ceil(force / 2000)):
                        if b == 4:
                            window.blit(power_bar4,
                                        (balls[-1].body.position[0] - 30 + (b * 15),
                                         balls[-1].body.position[1] + 30))
                        elif b == 3:
                            window.blit(power_bar3,
                                        (balls[-1].body.position[0] - 30 + (b * 15),
                                         balls[-1].body.position[1] + 30))
                        elif b == 2:
                            window.blit(power_bar2,
                                        (balls[-1].body.position[0] - 30 + (b * 15),
                                         balls[-1].body.position[1] + 30))
                        elif b == 1:
                            window.blit(power_bar1,
                                        (balls[-1].body.position[0] - 30 + (b * 15),
                                         balls[-1].body.position[1] + 30))
                        else:
                            window.blit(power_bar,
                                        (balls[-1].body.position[0] - 30 + (b * 15),
                                         balls[-1].body.position[1] + 30))
                elif powering_up is False and taking_shot is True:
                    x_impulse = math.cos(math.radians(palo_angle))
                    y_impulse = math.sin(math.radians(palo_angle))
                    balls[-1].body.apply_impulse_at_local_point((force * -x_impulse, force * y_impulse), (0, 0))
                    force = 0
                    force_direction = 1
            elif turn is False and bot_active is True:
                powering_up = True
                # Sistema de turnos
                if powering_up and not new_shot:
                    if potted_blanca:
                        balls[-1].body.position = (888, base_height / 2)

                        potted_blanca = False
                    new_shot = True
                    # Calcular el angulo
                    mouse_pos = pygame.mouse.get_pos()
                    palo_p1.rect.center = balls[-1].body.position
                    x_dist = balls[-1].body.position[0] - mouse_pos[0]
                    y_dist = -(balls[-1].body.position[1] - mouse_pos[1])
                    if ballTeam:
                        bot_balls = []
                        for ball in balls:
                            if ball.tipo != "negra":
                                bot_balls.append(ball)
                    else:
                        bot_balls = []
                        if p2_can_put_black:
                            for ball in balls:
                                if ball.tipo == "negra":
                                    bot_balls.append(ball)
                        if P2LISA:
                            for ball in balls:
                                if ball.tipo == "lisa":
                                    bot_balls.append(ball)
                        elif P2RAY:
                            for ball in balls:
                                if ball.tipo == "rayada":
                                    bot_balls.append(ball)
                        bot_balls.append(balls[len(balls)-1])

                    if Facil:
                        if funciones.calcular_probabilidad(30):
                            palo_angle = IA.determinar_mejor_bola(bot_balls, bot_pockets, balls[len(balls) - 1],
                                                                  diam, window)
                            # Fuerza del golpe
                            top_force = random.randint(4000, 10000)
                        else:
                            palo_angle = random.randint(-8, 8) + IA.determinar_mejor_bola\
                                (bot_balls, bot_pockets, balls[len(balls) - 1], diam, window)
                            # Fuerza del golpe
                            top_force = random.randint(7000, 10000)
                    if Medio:
                        if funciones.calcular_probabilidad(60):
                            palo_angle = IA.determinar_mejor_bola(bot_balls, bot_pockets, balls[len(balls) - 1],
                                                                  diam, window)
                            # Fuerza del golpe
                            top_force = random.randint(7000, 10000)
                        else:
                            palo_angle = random.randint(-5, 5) + IA.determinar_mejor_bola\
                                (bot_balls, bot_pockets, balls[len(balls) - 1], diam, window)
                            # Fuerza del golpe
                            top_force = random.randint(8500, 10000)
                    if dificil:
                        palo_angle = IA.determinar_mejor_bola(bot_balls, bot_pockets, balls[len(balls)-1],
                                                              diam, window)
                        # Fuerza del golpe
                        top_force = random.randint(9000, 10000)
                if taking_shot:
                    palo_p1.update(palo_angle)
                    # dibujar palo
                    palo_p1.draw(window)
                    # Fuerza del golpe
                    if force < top_force:
                        force += 100
                        # Dibujar las barras de poder
                        for b in range(math.ceil(force / 2000)):
                            if b == 4:
                                window.blit(power_bar4,
                                            (balls[-1].body.position[0] - 30 + (b * 15),
                                             balls[-1].body.position[1] + 30))
                            elif b == 3:
                                window.blit(power_bar3,
                                            (balls[-1].body.position[0] - 30 + (b * 15),
                                             balls[-1].body.position[1] + 30))
                            elif b == 2:
                                window.blit(power_bar2,
                                            (balls[-1].body.position[0] - 30 + (b * 15),
                                             balls[-1].body.position[1] + 30))
                            elif b == 1:
                                window.blit(power_bar1,
                                            (balls[-1].body.position[0] - 30 + (b * 15),
                                             balls[-1].body.position[1] + 30))
                            else:
                                window.blit(power_bar,
                                            (balls[-1].body.position[0] - 30 + (b * 15),
                                             balls[-1].body.position[1] + 30))
                    else:
                        changeTurn = True
                        powering_up = False
                        new_shot = False
                        try:
                            x_impulse = math.cos(math.radians(palo_angle))
                            y_impulse = math.sin(math.radians(palo_angle))
                            balls[-1].body.apply_impulse_at_local_point((force * -x_impulse, force * y_impulse), (0, 0))
                            force = 0
                            force_direction = 1
                        except Exception as e:
                            print("")

        # Event Handler
        for event in pygame.event.get():
            # Disparar la bola blanca
            if event.type == pygame.MOUSEBUTTONDOWN and taking_shot and turn:
                powering_up = True
                game_started = True
                unicaVez = False
            if event.type == pygame.MOUSEBUTTONUP and taking_shot and turn:
                num = random.randint(0, 2)
                powering_up = False
                if game_started:
                    palo_sound.play()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                if musicExist:
                    if music:
                        pygame.mixer.music.pause()
                        music = False
                    else:
                        pygame.mixer.music.unpause()
                        music = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()
    # Parte del loop jugable sin el bot
    else:

        # Comentario de ayuda
        if generalTheme is True:
            pygame.mixer.music.load("Assets/Sound/GameMusic.mp3")
            pygame.mixer.music.play(-1)
            generalTheme = False

        # Time simulation
        clock.tick(FPS)
        space.step(1 / FPS)
        # Fill background
        window.fill(DARK_BLUE)
        # draw pool table
        window.blit(table_image, (0, 0))
        # Aparecen los jugadores al mismo tiempo
        window.blit(jugador1Turno, (1200, 5))
        window.blit(jugador2Turno, (1200, 235))
        if turn:
            if soundTurn:
                change_turn_sound.play()
                soundTurn = False
            if cont >= 0:
                window.blit(turnosRestantes1, (1200, 80))
            elif cont == 0:
                window.blit(turnosRestantes2, (1200, 80))
            elif cont == -1:
                print("3")
        else:
            if soundTurn:
                change_turn_sound.play()
                soundTurn = False
            if cont > 0:
                window.blit(turnosRestantes1, (1200, 312))
            elif cont == 0:
                window.blit(turnosRestantes2, (1200, 312))
            elif cont == -1:
                print("3")

        if mostrarBochas:
            if P1LISA:
                for i, ball in enumerate(potted_balls_lisa):
                    window.blit(ball, (1200 + (i * 20), 110))

                for i, ball in enumerate(potted_balls_rayada):
                    window.blit(ball, (1200 + (i * 20), 335))

            else:
                for i, ball in enumerate(potted_balls_lisa):
                    window.blit(ball, (1200 + (i * 20), 335))

                for i, ball in enumerate(potted_balls_rayada):
                    window.blit(ball, (1200 + (i * 20), 110))

        # Fijarse si cualquier ball toco un hoyo
        for i, ball in enumerate(balls):
            for pocket in pockets:
                ball_x_dist = abs(ball.body.position[0] - pocket[0])
                ball_y_dist = abs(ball.body.position[1] - pocket[1])
                ball_dist = math.sqrt((ball_x_dist ** 2) + (ball_y_dist ** 2))
                if ball_dist <= pocket_dia / 2:
                    ball_in.play()
                    if ball.tipo == "lisa":
                        potted_balls.append(ball_images[i])
                        potted_balls_lisa.append(ball_images[i])
                        ball.body.position = (-1000, contPottedBalls)
                        ball.body.velocity = (0.0, 0.0)
                        space.remove(ball.body)
                        balls.remove(ball)
                        ball_images.pop(i)
                        contPottedBalls = contPottedBalls - 100

                    elif ball.tipo == "rayada":
                        potted_balls.append(ball_images[i])
                        potted_balls_rayada.append(ball_images[i])
                        ball.body.position = (-1000, contPottedBalls)
                        ball.body.velocity = (0.0, 0.0)
                        space.remove(ball.body)
                        balls.remove(ball)
                        ball_images.pop(i)
                        contPottedBalls = contPottedBalls - 100

                    elif ball.tipo == "negra":
                        potted_negra = True
                        potted_balls.append(ball_images[i])
                        space.remove(ball.body)
                        balls.remove(ball)
                        ball_images.pop(i)
                    elif ball.tipo == "blanca":
                        potted_blanca = True
                        ball.body.position = (-100, -100)
                        ball.body.velocity = (0.0, 0.0)
                    contBalls = 0
                    for j in balls:
                        contBalls = contBalls + 1

        # Dibujar las bolas del pool
        # Utilizo el iterador i para obtener el numero de la bola
        # Esto debido a que el iterador ball solo me da la direccion de memoria del objeto ball
        for i, ball in enumerate(balls):
            window.blit(ball_images[i], (ball.body.position[0] - diam, ball.body.position[1] - diam))

        # Checkar si las bolas estan quietas
        taking_shot = True
        for ball in balls:
            if int(ball.body.velocity[0]) != 0 or int(ball.body.velocity[1]) != 0:
                taking_shot = False
                changeTurn = True

        # Si un jugador mete la blanca, le toca al otro jugador durante 2 turnos (como en el pool de verdad)
        # NO MUEVAN ESTO DE ACA, PORQUE MAS ABAJO SE MODIFICA LA VARIABLE Y NO FUNCIONARIA
        if potted_blanca and not unicaVez and not win and not p2win and not p1win:
            turn = not turn
            cont = -1
            unicaVez = True

        # Tipos de bocha para cada jugador
        if ballTeam:

            # Jugador 1
            if len(potted_balls_lisa) > 0 and turn:
                P1LISA = True
                P1RAY = False
                P2LISA = False
                P2RAY = True
                ballTeam = False
                mostrarBochas = True
                cont = 0
            elif len(potted_balls_rayada) > 0 and turn:
                P1LISA = False
                P1RAY = True
                P2LISA = True
                P2RAY = False
                ballTeam = False
                mostrarBochas = True
                cont = 0

            # Jugador 2
            elif len(potted_balls_lisa) > 0 and not turn:
                P1LISA = False
                P1RAY = True
                P2LISA = True
                P2RAY = False
                ballTeam = False
                mostrarBochas = True
                cont = 0
            elif len(potted_balls_rayada) > 0 and not turn:
                P1LISA = True
                P1RAY = False
                P2LISA = False
                P2RAY = True
                ballTeam = False
                mostrarBochas = True
                cont = 0

        # CONDICIONES DE VICTORIA
        if not ballTeam and taking_shot:
            if len(potted_balls_lisa) > aux_lisa and len(potted_balls_rayada) > aux_rayada:
                aux_rayada += 1
                aux_lisa += 1
            elif ((P1RAY and turn) or (P2RAY and not turn)) and len(potted_balls_rayada) > aux_rayada:
                aux_rayada += 1
                cont = 0
            elif ((P1LISA and turn) or (P2LISA and not turn)) and len(potted_balls_lisa) > aux_lisa:
                aux_lisa += 1
                cont = 0
            elif ((P1RAY and turn) or (P2RAY and not turn)) and len(potted_balls_lisa) > aux_lisa:
                turn = not turn
                aux_lisa += 1
                cont = -1
            elif ((P1LISA and turn) or (P2LISA and not turn)) and len(potted_balls_rayada) > aux_rayada:
                turn = not turn
                aux_rayada += 1
                cont = -1

            # Meter las bochas correspondientes al equipo
            if (P1LISA and len(potted_balls_lisa) == 7) or (P1RAY and len(potted_balls_rayada) == 7):
                p1_can_put_black = True
            if (P2LISA and len(potted_balls_lisa) == 7) or (P2RAY and len(potted_balls_rayada) == 7):
                p2_can_put_black = True

        # Meter la negra antes de tiempo
        if turn and potted_negra and not p1_can_put_black:
            taking_shot = False
            window.blit(ganaj2, (400, 300))
            p2win = True

        if not turn and potted_negra and not p2_can_put_black:
            taking_shot = False
            window.blit(ganaj1, (400, 300))
            p1win = True

        # Meter la negra para ganar

        if not win:
            if p1_can_put_black and potted_negra and turn is True:
                taking_shot = False
                window.blit(ganaj1, (400, 300))
                p1win = True
            if p2_can_put_black and potted_negra and turn is False:
                taking_shot = False
                window.blit(ganaj2, (400, 300))
                p2win = True

        if p1win:
            window.blit(ganaj1, (400, 300))
        elif p2win:
            window.blit(ganaj2, (400, 300))

        if p1win is True and one_time:
            pygame.mixer.music.stop()
            win_sound.play()
            one_time = False

        if p2win is True and one_time:
            pygame.mixer.music.stop()
            win_sound.play()
            one_time = False

        if taking_shot:
            # Sistema de turnos
            if changeTurn:
                soundTurn = True
                changeTurn = False
                cont += 1
                if cont > 1:
                    turn = not turn
            if potted_blanca:
                balls[-1].body.position = (888, base_height / 2)
                potted_blanca = False
            # Calcular el angulo
            mouse_pos = pygame.mouse.get_pos()
            palo_p1.rect.center = balls[-1].body.position
            x_dist = balls[-1].body.position[0] - mouse_pos[0]
            y_dist = -(balls[-1].body.position[1] - mouse_pos[1])
            palo_angle = math.degrees(math.atan2(y_dist, x_dist))
            palo_p1.update(palo_angle)
            # dibujar palo
            palo_p1.draw(window)
            # Fuerza del golpe
            if powering_up is True:
                force += 100 * force_direction
                if force >= max_force or force <= 0:
                    force_direction *= -1
                # Dibujar las barras de poder
                for b in range(math.ceil(force / 2000)):
                    if b == 4:
                        window.blit(power_bar4,
                                    (balls[-1].body.position[0] - 30 + (b * 15),
                                     balls[-1].body.position[1] + 30))
                    elif b == 3:
                        window.blit(power_bar3,
                                    (balls[-1].body.position[0] - 30 + (b * 15),
                                     balls[-1].body.position[1] + 30))
                    elif b == 2:
                        window.blit(power_bar2,
                                    (balls[-1].body.position[0] - 30 + (b * 15),
                                     balls[-1].body.position[1] + 30))
                    elif b == 1:
                        window.blit(power_bar1,
                                    (balls[-1].body.position[0] - 30 + (b * 15),
                                     balls[-1].body.position[1] + 30))
                    else:
                        window.blit(power_bar,
                                    (balls[-1].body.position[0] - 30 + (b * 15),
                                     balls[-1].body.position[1] + 30))
            elif powering_up is False and taking_shot is True:
                x_impulse = math.cos(math.radians(palo_angle))
                y_impulse = math.sin(math.radians(palo_angle))
                balls[-1].body.apply_impulse_at_local_point((force * -x_impulse, force * y_impulse), (0, 0))
                force = 0
                force_direction = 1
        # Event Handler
        for event in pygame.event.get():
            # Disparar la bola blanca
            if event.type == pygame.MOUSEBUTTONDOWN and taking_shot:
                powering_up = True
                game_started = True
                unicaVez = False
            if event.type == pygame.MOUSEBUTTONUP and taking_shot:
                powering_up = False
                if game_started:
                    palo_sound.play()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                balls[-1].body.position = (55, 58)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                balls[7].body.position = (55, 58)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                if musicExist:
                    if music:
                        pygame.mixer.music.pause()
                        music = False
                    else:
                        pygame.mixer.music.unpause()
                        music = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

    clock.tick(FPS)
    pygame.display.flip()
