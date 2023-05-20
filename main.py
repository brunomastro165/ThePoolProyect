import random

import pygame
import sys
import pymunk
import pymunk.pygame_util
import button
import mesa
import palo
import math
import funciones
from pygame.locals import *

# Variables de la Resolucion
base_width = 800
base_height = 800

posX = 0
posY = 0

# Colores
white_color = (255, 255, 255)
green_color = (52, 130, 43)
yellow_color = (238, 182, 2)
BG = (50, 50, 50)
RED = (255, 0, 0)

# Iniciar Pygame, hacer la ventana como una variable con la resolucion y poner el nombre del juego
pygame.init()
window = pygame.display.set_mode((base_width, base_height), pygame.RESIZABLE)
pygame.display.set_caption("PoolGame")

# Cargando Imagenes
icon = funciones.imageLoad("Images/icono.png")
pygame.display.set_icon(icon)
# Pantalla Principal
game = funciones.imageLoad("Images/PLAY.png")
game_start_click = funciones.imageLoad("Images/PLAY (ACTIVE).png")
game_menu_click = funciones.imageLoad("Images/MENU (ACTIVE).png")
game_data_click = funciones.imageLoad("Images/PLAY DATOS.png")

# Pantalla de Datos
data_image = funciones.imageLoad("Images/DATOS (PAGINA).png")
data_return = funciones.imageLoad("Images/DATOS (PAG ACTIVA).png")

# Pantalla Menu
# Cargamos Imagenes
imagenPrincpal = funciones.imageLoad("Images/MENU_PRINCIPAL.png")
imagenSiFacil = funciones.imageLoad("Images/M_P_SI_FACIL.png")
imagenSiFacilBack = funciones.imageLoad("Images/M_P_SI_FACIL_BACK.png")
imagenSiMedio = funciones.imageLoad("Images/M_P_SI_MEDIO.png")
imagenSiMedioBack = funciones.imageLoad("Images/M_P_SI_MEDIO_BACK.png")
imagenSiDificil = funciones.imageLoad("Images/M_P_SI_DIFICIL.png")
imagenSiDificilBack = funciones.imageLoad("Images/M_P_SI_DIFICIL_BACK.png")
imagenNoFacil = funciones.imageLoad("Images/M_P_NO_FACIL.png")
imagenNoFacilBack = funciones.imageLoad("Images/M_P_NO_FACIL_BACK.png")
imagenNoMedio = funciones.imageLoad("Images/M_P_NO_MEDIO.png")
imagenNoMedioBack = funciones.imageLoad("Images/M_P_NO_MEDIO_BACK.png")
imagenNoDificil = funciones.imageLoad("Images/M_P_NO_DIFICIL.png")
imagenNoDificilBack = funciones.imageLoad("Images/M_P_NO_DIFICIL_BACK.png")
# Generamos variable para cambiar las imagenes de menu
imagenActual = imagenNoMedio

# Pantalla PrePlay
prePlayInactive = funciones.imageLoad("Images/PrePlayInactive.png")
prePlayPlayerActiveImage = funciones.imageLoad("Images/PrePlayPlayerActive.png")
prePlayBotActive = funciones.imageLoad("Images/PrePlayBotActive.png")
prePlayBackActive = funciones.imageLoad("Images/PrePlayBackActive.png")

# Jugadores, turnos y victorias
jugador1Turno = funciones.imageLoad("Images/j1.png")
jugador2Turno = funciones.imageLoad("Images/j2.png")

turnoActual = funciones.imageLoad("Images/TurnoActual.png")

turnosRestantes1 = funciones.imageLoad("Images/TR1.png")
turnosRestantes2 = funciones.imageLoad("Images/TR2.png")

j1eslisa = funciones.imageLoad("Images/j1eslisas.png")
j1esrayada = funciones.imageLoad("Images/j1esrayada.png")

j2esrayada = funciones.imageLoad("Images/j2esrayada.png")
j2eslisa = funciones.imageLoad("Images/j2eslisas.png")

ganaj1 = funciones.imageLoad("Images/ganaj1.png")
ganaj2 = funciones.imageLoad("Images/ganaj2.png")

# BOTONES

# BOTONES PANTALLA PRINCIPAL
start_hitbox = button.Button(231, 568, 575 - 231, 675 - 568)
menu_hitbox = button.Button(300, 696, 500 - 300, 759 - 696)
data_hitbox = button.Button(714, 706, 778 - 714, 782 - 706)

# BOTÓN BACK
return_hitbox = button.Button(12, 18, 165 - 12, 74 - 18)

# BOTONES DE LA PANTALLA DE JUEGO BÁSICA
prePlayPlayerActive_hitbox = button.Button(221, 319, 577 - 210, 585 - 502)
preBotActive_hitbox = button.Button(221, 441, 577 - 210, 585 - 502)

# BOTONES DE LA PANTALLA MENU
fullscreenSi_hitbox = button.Button(406, 355, 484 - 406, 436 - 355)
fullscreenNo_hitbox = button.Button(621, 360, 700 - 621, 432 - 360)
diffFacil_hitbox = button.Button(404, 474, 695 - 404, 560 - 474)
diffMedio_hitbox = button.Button(405, 574, 693 - 405, 657 - 574)
diffDificil_hitbox = button.Button(407, 684, 697 - 407, 760 - 684)

# SECCIÓN DE MÚSICA
pygame.mixer.music.load('easy-lifestyle-137766.mp3')  # agregar música
pygame.mixer.music.set_volume(0.1)  # setear volumen
# VARIABLES DE LA BARRA DE VOLUMEN
moving_cursor = False
moving_bar = False
cursor = pygame.Rect(0, 0, 0, 0)
default_sound = True
actual_resolution = 800

# hacer cada línea individualmente, para poder rodear la imagen con la hitbox
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
funciones.playMusic()

# Condiciones para los botones del menu
screenSiPress = False
screenNoPress = True
Facil = False
Medio = True
dificil = False

# Condición para los turnos
cont = 1
suma_hecha = False
changeTurn = False
turn = True

# COSAS DE PYMUNK

# Pymunk space
space = pymunk.Space()
static_body = space.static_body
# Con esta funcion le puedo pedir a pymunk que dibuje las formar que creo, en la ventana
draw_options = pymunk.pygame_util.DrawOptions(window)

# Clock
clock = pygame.time.Clock()
FPS = 75

# Game variables
diam = 40
pocket_dia = 66
force = 0
max_force = 10000
force_direction = 1
taking_shot = True
powering_up = False
potted_balls = []
potted_balls_lisa = []
potted_balls_rayada = []
potted_negra = False
potted_blanca = False
ballTeam = True
p1_can_put_black = False
p2_can_put_black = False
FullScreen = False

# load images
table_image = pygame.image.load("Assets/Images/table.png").convert_alpha()
ball_images = []
for i in range(1, 17):
    ball_image = pygame.image.load(f"Assets/Images/bola{i}.png").convert_alpha()
    ball_image = pygame.transform.scale(ball_image, (diam * 2, diam * 2))
    ball_images.append(ball_image)

# Crear las bolas para el juego
balls = []
rows = 5
# Bolas numeradas

for col in range(5):
    for row in range(rows):
        pos = (250 + (col * (diam + 3)), 267 + (row * (diam + 3)) + (col * diam / 2))

        '''CÓMO LAS BALLS NO SON OBJETOS, NO TIENEN ATRIBUTOS O PARÁMETROS, 
        SIMPLEMENTE ES UNA FUNCIÓN QUE DEVUELVE CIERTOS NÚMEROS'''
        # ASÍ QUE SE MODIFICÓ LA CLASE CIRCLE DE PYMUNK, PARA PODER TENER OBJETOS

        if 8 > len(balls) > 0:
            # print(f"Lisas: {len(balls)}")
            new_ball = funciones.create_ball((diam / 2), pos, "lisas", static_body, space)
            new_ball.tipo = "lisa"
        if len(balls) == 0:  # LA ITERACION 0 POR ALGÚN MOTIVO ES LA NÚMERO 15, Y ES RAYADA, POR ESO ES ESTE IF
            # print(f"Rayadas: {len(balls)}")
            new_ball = funciones.create_ball((diam / 2), pos, "rayadas", static_body, space)
            new_ball.tipo = "rayada"
        if len(balls) > 8:
            # print(f"Rayadas: {len(balls)}")
            new_ball = funciones.create_ball((diam / 2), pos, "rayadas", static_body, space)
            new_ball.tipo = "rayada"
        if len(balls) == 8:
            # print(f"Negra: {len(balls)}")
            new_ball = funciones.create_ball((diam / 2), pos, "negra", static_body, space)
            new_ball.tipo = "negra"

        if new_ball:
            balls.append(new_ball)
    rows -= 1

# Cambiando las bolas de lugar

funciones.changePos(0, 14, balls)
funciones.changePos(1, 5, balls)
funciones.changePos(2, 13, balls)
funciones.changePos(13, 8, balls)
funciones.changePos(4, 12, balls)
funciones.changePos(4, 9, balls)
funciones.changePos(7, 10, balls)
funciones.changePos(10, 6, balls)
funciones.changePos(3, 12, balls)
funciones.changePos(12, 10, balls)

# Bola blanca
pos = (888, (678 / 2))
print(pos)
cue_ball = funciones.create_ball((diam / 2), pos, "blanca", static_body, space)
cue_ball.tipo = "blanca"
balls.append(cue_ball)

contBalls = 0
for i in balls:
    print(f"{contBalls} : {i.tipo}")
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

for b in border:
    funciones.create_table_border(b, space)

# Objeto palo (instancia de la clase palo)
palo_p1 = palo.Palo(balls[-1].body.position)

# Imagen para la barra de carga
barra_placeholder = funciones.imageLoad('Assets/Images/MascaraHK.png')
barra_placeholder2 = funciones.imageLoad('Assets/Images/Joni.png')

# Barra de poder del paliño
power_bar = pygame.Surface((barra_placeholder.get_width(), barra_placeholder.get_height()))
power_bar.blit(barra_placeholder, (0, 0))

power_bar2 = pygame.Surface((barra_placeholder2.get_width(), barra_placeholder2.get_height()))
power_bar2.blit(barra_placeholder2, (0, 0))

aux_rayada = 0
aux_lisa = 0
print(balls[15].tipo)

while True:
    # mouse_x, mouse_y = pygame.mouse.get_pos()  # posición cartesiana del mouse

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
                    funciones.resposiveHitbox(hitbox, value, window)
                    window.fill(white_color)
                    posX = (window.get_width() - 800) / 2
                    posY = (window.get_height() - 800) / 2
            # Animacion de Botones y cambio de pestañas

            # PANTALLA PRINCIPAL
            if main:

                window.blit(game, (posX, posY))
                # START HOVER
                funciones.updateImage(start_hitbox, game_start_click, event, window, posX, posY)
                # MENU HOVER
                funciones.updateImage(menu_hitbox, game_menu_click, event, window, posX, posY)
                # DATOS HOVER
                funciones.updateImage(data_hitbox, game_data_click, event, window, posX, posY)

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
            if start:

                pygame.mixer.music.stop()

                window.blit(prePlayInactive, (posX, posY))

                funciones.updateImage(return_hitbox, prePlayBackActive, event, window, posX, posY)
                funciones.updateImage(prePlayPlayerActive_hitbox, prePlayPlayerActiveImage, event, window, posX, posY)
                funciones.updateImage(preBotActive_hitbox, prePlayBotActive, event, window, posX, posY)

                # DOWN EVENT

                if prePlayPlayerActive_hitbox.down(event):
                    # playMusic()
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
                    start = False
                    main = True

                if preBotActive_hitbox.down(event):
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

            # VENTANA MENU
            if menu:
                # BARRA DE VOLUMEN
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
                print(cursor.x)
                # pygame.mixer.music.stop()
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
                    x_cursor, y_cursor = event.pos  # actualizar posición del cursor

                elif event.type == pygame.MOUSEMOTION:
                    if moving_cursor:
                        x_cursor, y_cursor = event.pos
                        # asegurarse de que el cursor no se mueva fuera de los límites de la barra
                        if x_cursor < bar_x:
                            x_cursor = bar_x
                        elif x_cursor > bar_x + bar_width - cursor_width:
                            x_cursor = bar_x + bar_width - cursor_width
                        cursor.x = x_cursor - (cursor_width / 2)
                    elif moving_bar:
                        x_cursor, y_cursor = event.pos
                        # asegurarse de que el cursor no se mueva fuera de los límites de la barra
                        if x_cursor < bar_x:
                            x_cursor = bar_x
                        elif x_cursor > bar_x + bar_width - cursor_width:
                            x_cursor = bar_x + bar_width - cursor_width
                        cursor.x = x_cursor - (cursor_width / 2)

                # Calcular el volumen y actualizar la música
                sound = (cursor.x - bar_x) / bar_width
                pygame.mixer.music.set_volume(sound)

                soud = (x_cursor - bar_x) / bar_width
                pygame.mixer.music.set_volume(soud)
                # VOLVER AL PRINCIPAL

                if return_hitbox.down(event):
                    menu = False
                    main = True

                # SI ESTA APRETADO SI

                if fullscreenSi_hitbox.down(event):
                    screenSiPress = True
                    screenNoPress = False
                    imagenActual = imagenSiMedio
                    window.blit(imagenActual, (posX, posY))
                    FullScreen = True
                else:
                    window.blit(imagenActual, (posX, posY))

                # DIFERENCIADOS POR DIFICULTADO

                if diffFacil_hitbox.down(event):
                    Medio = False
                    Facil = True
                    dificil = False

                if diffMedio_hitbox.down(event):
                    Medio = True
                    Facil = False
                    dificil = False

                if diffDificil_hitbox.down(event):
                    Medio = False
                    Facil = False
                    dificil = True

                # SI ESTA APRETADO NO

                if fullscreenNo_hitbox.down(event):
                    screenNoPress = True
                    screenSiPress = False
                    imagenActual = imagenNoMedio
                    window.blit(imagenActual, (posX, posY))
                    FullScreen = False
                else:
                    window.blit(imagenActual, (posX, posY))

                # Cosas de frontEnd
                if screenSiPress:
                    if Facil:
                        imagenActual = imagenSiFacil
                        window.blit(imagenActual, (posX, posY))
                        funciones.updateImage(return_hitbox, imagenSiFacilBack, event, window, posX, posY)
                    if Medio:
                        imagenActual = imagenSiMedio
                        window.blit(imagenActual, (posX, posY))
                        funciones.updateImage(return_hitbox, imagenSiMedioBack, event, window, posX, posY)
                    if dificil:
                        imagenActual = imagenSiDificil
                        window.blit(imagenActual, (posX, posY))
                        funciones.updateImage(return_hitbox, imagenSiDificilBack, event, window, posX, posY)

                elif screenNoPress:
                    if Facil:
                        imagenActual = imagenNoFacil
                        window.blit(imagenActual, (posX, posY))
                        funciones.updateImage(return_hitbox, imagenNoFacilBack, event, window, posX, posY)
                    if Medio:
                        imagenActual = imagenNoMedio
                        window.blit(imagenActual, (posX, posY))
                        funciones.updateImage(return_hitbox, imagenNoMedioBack, event, window, posX, posY)
                    if dificil:
                        imagenActual = imagenNoDificil
                        window.blit(imagenActual, (posX, posY))
                        funciones.updateImage(return_hitbox, imagenNoDificilBack, event, window, posX, posY)
                pygame.draw.rect(window, green_color, sound_bar)
                pygame.draw.rect(window, yellow_color, cursor)
            # VENTANA DATOS
            if data:
                if return_hitbox.down(event):
                    data = False
                    main = True

                window.blit(data_image, (posX, posY))
                funciones.updateImage(return_hitbox, data_return, event, window, posX, posY)

            if event.type == QUIT:
                sys.exit()

            if event.type == event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()

    elif playing_bot:
        # Time simulation
        clock.tick(FPS)
        space.step(1 / FPS)

        # Fill background
        window.fill(BG)

        # draw pool table
        window.blit(table_image, (0, 0))

        if turn:
            window.blit(jugador1Turno, (1180, -50))
            if cont >= 0:
                window.blit(turnosRestantes1, (1195, 0))
            elif cont == -1:
                window.blit(turnosRestantes2, (1197, 0))
            elif cont == -2:
                print("3")

        else:
            window.blit(jugador2Turno, (1183, -50))
            if cont > 0:
                window.blit(turnosRestantes1, (1195, 0))
            elif cont == 0:
                window.blit(turnosRestantes2, (1197, 0))
            elif cont == -1:
                print("3")

        if not ballTeam:
            if P1LISA:
                window.blit(j1eslisa, (1200, 100))
            elif P1RAY:
                window.blit(j1esrayada, (1200, 100))

            if P2LISA:
                window.blit(j2eslisa, (1200, 120))
            elif P2RAY:
                window.blit(j2esrayada, (1200, 120))

        # Fijarse si cualquier ball tocó un hoyo
        for i, ball in enumerate(balls):
            for pocket in pockets:
                ball_x_dist = abs(ball.body.position[0] - pocket[0])
                ball_y_dist = abs(ball.body.position[1] - pocket[1])
                ball_dist = math.sqrt((ball_x_dist ** 2) + (ball_y_dist ** 2))
                if ball_dist <= pocket_dia / 2:
                    if ball.tipo == "lisa":
                        potted_balls.append(ball_images[i])
                        potted_balls_lisa.append(ball_images[i])
                        ball.body.position = (-1000, -1000)
                        ball.body.velocity = (0.0, 0.0)
                        space.remove(ball.body)
                        balls.remove(ball)
                        ball_images.pop(i)

                    elif ball.tipo == "rayada":
                        potted_balls.append(ball_images[i])
                        potted_balls_rayada.append(ball_images[i])
                        ball.body.position = (-1000, -1000)
                        ball.body.velocity = (0.0, 0.0)
                        space.remove(ball.body)
                        balls.remove(ball)
                        ball_images.pop(i)

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
                    for i in balls:
                        print(f"{contBalls} : {i.tipo}")
                        contBalls = contBalls + 1

                    print(f"Lisas: {potted_balls_lisa}")
                    print(f"Rayadas: {potted_balls_rayada}")
                    print(f"Negra: {potted_negra}")

        # draw pool balls
        # Utilizo el iterador i para obtener el número de la bola
        # Esto debido a que el iterador ball solo me da la direccion de memoria del objeto ball
        for i, ball in enumerate(balls):
            window.blit(ball_images[i], (ball.body.position[0] - diam, ball.body.position[1] - diam))

        # Checkar si las bolas estan quietas
        taking_shot = True
        for ball in balls:
            if int(ball.body.velocity[0]) != 0 or int(ball.body.velocity[1]) != 0:
                taking_shot = False
                changeTurn = True

        # Si un jugador mete la blanca, le toca al otro jugador durante 2 turnos (cómo en el pool de verdad)
        # NO MUEVAN ESTO DE ACÁ, PORQUE MÁS ABAJO SE MODIFICA LA VARIABLE Y NO FUNCIONARÍA
        if potted_blanca:
            turn = not turn
            cont = -1

        # Tipos de bocha para cada jugador
        if ballTeam:

            # Jugador 1
            if len(potted_balls_lisa) > 0 and turn:  # Probado y funciona
                P1LISA = True
                P1RAY = False
                P2LISA = False
                P2RAY = True
                ballTeam = False
                cont = 0

            elif len(potted_balls_rayada) > 0 and turn:  # Probado y funciona
                P1LISA = False
                P1RAY = True
                P2LISA = True
                P2RAY = False
                ballTeam = False
                cont = 0

            # Jugador 2
            elif len(potted_balls_lisa) > 0 and not turn:  # Probado y funciona
                P1LISA = False
                P1RAY = True
                P2LISA = True
                P2RAY = False
                ballTeam = False
                cont = 0

            elif len(potted_balls_rayada) > 0 and not turn:  # Probado y funciona
                P1LISA = True
                P1RAY = False
                P2LISA = False
                P2RAY = True
                ballTeam = False
                cont = 0

        # dibujar las bochas metidas en la parte de abajo
        for i, ball in enumerate(potted_balls):
            window.blit(ball, (10 + (i * 50), base_height - 10))

        # CONDICIONES DE VICTORIA (PROTOTIPO)
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
            if P1LISA and len(potted_balls_lisa) == 7:
                p1_can_put_black = True
            elif P1RAY and len(potted_balls_rayada) == 7:
                p1_can_put_black = True

            if P2LISA and len(potted_balls_lisa) == 7:
                p2_can_put_black = True
            elif P2RAY and len(potted_balls_rayada) == 7:
                p2_can_put_black = True

        # Meter la negra antes de tiempo
        if turn and potted_negra and not p1_can_put_black:
            taking_shot = False
            window.blit(ganaj2, (400, 300))

        if not turn and potted_negra and not p2_can_put_black:
            taking_shot = False
            window.blit(ganaj1, (400, 300))

        # Meter la negra para ganar
        if p1_can_put_black and potted_negra:
            taking_shot = False
            window.blit(ganaj1, (400, 300))

        if p2_can_put_black and potted_negra:
            taking_shot = False
            window.blit(ganaj2, (400, 300))
        if taking_shot:
            if changeTurn:
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
                # print(palo_angle)
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
                            window.blit(power_bar2,
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

            else:
                powering_up = True
                # Sistema de turnos
                if potted_blanca:
                    balls[-1].body.position = (888, base_height / 2)
                    potted_blanca = False
                if powering_up:
                    changeTurn = True
                    powering_up = False
                    # Calcular el angulo
                    mouse_pos = pygame.mouse.get_pos()
                    palo_p1.rect.center = balls[-1].body.position
                    x_dist = balls[-1].body.position[0] - mouse_pos[0]
                    y_dist = -(balls[-1].body.position[1] - mouse_pos[1])
                    palo_angle = random.uniform(-180, 180)
                    # print(palo_angle)
                    palo_p1.update(palo_angle)
                    # dibujar palo
                    palo_p1.draw(window)
                    # Fuerza del golpe

                    force = random.randint(1000, 10000)
                    x_impulse = math.cos(math.radians(palo_angle))
                    y_impulse = math.sin(math.radians(palo_angle))
                    balls[-1].body.apply_impulse_at_local_point((force * -x_impulse, force * y_impulse), (0, 0))
                    force = 0
                    force_direction = 1

        # Event Handler
        for event in pygame.event.get():
            if event.type == KEYDOWN:  # Verificar si se presionó una tecla
                if event.key == pygame.K_p:
                    funciones.makeNewGame(balls, diam, static_body, space)
            # Disparar la bola blanca
            if event.type == pygame.MOUSEBUTTONDOWN and taking_shot and turn:
                powering_up = True

            if event.type == pygame.MOUSEBUTTONUP and taking_shot and turn:
                powering_up = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()

            if event.type == pygame.QUIT:
                sys.exit()

        '''
        if not ballTeam:
            if P1LISA == True:
                print(f"Jugador 1 juega con lisas {P1LISA}")
            else:
                print(f"Jugador 1 juega con rayadas {P1RAY}")

            if P2LISA == True:
                print(f"Jugador 2 juega con lisas {P2LISA}")
            else:
                print(f"Jugador 2 juega con raydas {P2RAY}")
        '''

        # print(f"BallTeam{ballTeam}")
        # space.debug_draw(draw_options)
        pygame.display.update()
    else:
        # Time simulation
        clock.tick(FPS)
        space.step(1 / FPS)

        # Fill background
        window.fill(BG)

        # draw pool table
        window.blit(table_image, (0, 0))

        if turn:
            window.blit(jugador1Turno, (1180, -50))
            if cont >= 0:
                window.blit(turnosRestantes1, (1195, 0))
            elif cont == -1:
                window.blit(turnosRestantes2, (1197, 0))
            elif cont == -2:
                print("3")

        else:
            window.blit(jugador2Turno, (1183, -50))
            if cont > 0:
                window.blit(turnosRestantes1, (1195, 0))
            elif cont == 0:
                window.blit(turnosRestantes2, (1197, 0))
            elif cont == -1:
                print("3")

        if not ballTeam:
            if P1LISA:
                window.blit(j1eslisa, (1200, 100))
            elif P1RAY:
                window.blit(j1esrayada, (1200, 100))

            if P2LISA:
                window.blit(j2eslisa, (1200, 120))
            elif P2RAY:
                window.blit(j2esrayada, (1200, 120))

        # Fijarse si cualquier ball tocó un hoyo
        for i, ball in enumerate(balls):
            for pocket in pockets:
                ball_x_dist = abs(ball.body.position[0] - pocket[0])
                ball_y_dist = abs(ball.body.position[1] - pocket[1])
                ball_dist = math.sqrt((ball_x_dist ** 2) + (ball_y_dist ** 2))
                if ball_dist <= pocket_dia / 2:
                    if ball.tipo == "lisa":
                        potted_balls.append(ball_images[i])
                        potted_balls_lisa.append(ball_images[i])
                        ball.body.position = (-1000, -1000)
                        ball.body.velocity = (0.0, 0.0)
                        space.remove(ball.body)
                        balls.remove(ball)
                        ball_images.pop(i)

                    elif ball.tipo == "rayada":
                        potted_balls.append(ball_images[i])
                        potted_balls_rayada.append(ball_images[i])
                        ball.body.position = (-1000, -1000)
                        ball.body.velocity = (0.0, 0.0)
                        space.remove(ball.body)
                        balls.remove(ball)
                        ball_images.pop(i)

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
                    for i in balls:
                        print(f"{contBalls} : {i.tipo}")
                        contBalls = contBalls + 1

                    print(f"Lisas: {potted_balls_lisa}")
                    print(f"Rayadas: {potted_balls_rayada}")
                    print(f"Negra: {potted_negra}")

        # draw pool balls
        # Utilizo el iterador i para obtener el número de la bola
        # Esto debido a que el iterador ball solo me da la direccion de memoria del objeto ball
        for i, ball in enumerate(balls):
            window.blit(ball_images[i], (ball.body.position[0] - diam, ball.body.position[1] - diam))

        # Checkar si las bolas estan quietas
        taking_shot = True
        for ball in balls:
            if int(ball.body.velocity[0]) != 0 or int(ball.body.velocity[1]) != 0:
                taking_shot = False
                changeTurn = True

        # Si un jugador mete la blanca, le toca al otro jugador durante 2 turnos (cómo en el pool de verdad)
        # NO MUEVAN ESTO DE ACÁ, PORQUE MÁS ABAJO SE MODIFICA LA VARIABLE Y NO FUNCIONARÍA
        if potted_blanca:
            turn = not turn
            cont = -1

        # Tipos de bocha para cada jugador
        if ballTeam:

            # Jugador 1
            if len(potted_balls_lisa) > 0 and turn:  # Probado y funciona
                P1LISA = True
                P1RAY = False
                P2LISA = False
                P2RAY = True
                ballTeam = False
                cont = 0

            elif len(potted_balls_rayada) > 0 and turn:  # Probado y funciona
                P1LISA = False
                P1RAY = True
                P2LISA = True
                P2RAY = False
                ballTeam = False
                cont = 0

            # Jugador 2
            elif len(potted_balls_lisa) > 0 and not turn:  # Probado y funciona
                P1LISA = False
                P1RAY = True
                P2LISA = True
                P2RAY = False
                ballTeam = False
                cont = 0

            elif len(potted_balls_rayada) > 0 and not turn:  # Probado y funciona
                P1LISA = True
                P1RAY = False
                P2LISA = False
                P2RAY = True
                ballTeam = False
                cont = 0

        # dibujar las bochas metidas en la parte de abajo
        for i, ball in enumerate(potted_balls):
            window.blit(ball, (10 + (i * 50), base_height - 10))

        # CONDICIONES DE VICTORIA (PROTOTIPO)
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
            if P1LISA and len(potted_balls_lisa) == 7:
                p1_can_put_black = True
            elif P1RAY and len(potted_balls_rayada) == 7:
                p1_can_put_black = True

            if P2LISA and len(potted_balls_lisa) == 7:
                p2_can_put_black = True
            elif P2RAY and len(potted_balls_rayada) == 7:
                p2_can_put_black = True

        # Meter la negra antes de tiempo
        if turn and potted_negra and not p1_can_put_black:
            taking_shot = False
            window.blit(ganaj2, (400, 300))

        if not turn and potted_negra and not p2_can_put_black:
            taking_shot = False
            window.blit(ganaj1, (400, 300))

        # Meter la negra para ganar
        if p1_can_put_black and potted_negra:
            taking_shot = False
            window.blit(ganaj1, (400, 300))

        if p2_can_put_black and potted_negra:
            taking_shot = False
            window.blit(ganaj2, (400, 300))
        if taking_shot:
            # Sistema de turnos
            if changeTurn:
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
            print(palo_angle)
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
                        window.blit(power_bar2,
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
            if event.type == KEYDOWN:  # Verificar si se presionó una tecla
                if event.key == pygame.K_p:
                    funciones.makeNewGame(balls, diam, static_body, space)
            # Disparar la bola blanca
            if event.type == pygame.MOUSEBUTTONDOWN and taking_shot:
                powering_up = True

            if event.type == pygame.MOUSEBUTTONUP and taking_shot:
                powering_up = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()

            if event.type == pygame.QUIT:
                sys.exit()

        '''
        if not ballTeam:
            if P1LISA == True:
                print(f"Jugador 1 juega con lisas {P1LISA}")
            else:
                print(f"Jugador 1 juega con rayadas {P1RAY}")

            if P2LISA == True:
                print(f"Jugador 2 juega con lisas {P2LISA}")
            else:
                print(f"Jugador 2 juega con raydas {P2RAY}")
        '''

        # print(f"BallTeam{ballTeam}")
        # space.debug_draw(draw_options)
        pygame.display.update()
    # print(pygame.mouse.get_pos())
    clock.tick(FPS)
    pygame.display.flip()
