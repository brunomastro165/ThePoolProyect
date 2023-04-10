import pygame, sys
import pymunk
import pymunk.pygame_util
import button
import mesa
from pygame.locals import *


# Funcion para cargar imagenes
def imageLoad(name):
    return pygame.image.load(name)


# Funcion para hacer resposive los botones
def resposiveHitbox(object, pos):
    object.x = (window.get_width() - 800) / 2 + pos
    object.hitbox = pygame.Rect(object.x, object.y, object.width, object.height)


# Variables de la Resolucion
base_width = 800
base_height = 800

posX = 0
posY = 0

# Color Blanco
white_color = (255, 255, 255)

# Iniciar Pygame, hacer la ventana como una variable con la resolucion y poner el nombre del juego
pygame.init()
window = pygame.display.set_mode((base_width, base_height), pygame.RESIZABLE)
pygame.display.set_caption("PoolGame")
clock = pygame.time.Clock()

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

"""
Esto no se usa todavía y capaz no se use
right = False
left = False
up = False
down = False
"""
# BOTONES

# BOTONES PANTALLA PRINCIPAL
start_hitbox = button.Button(231, 568, 575 - 231, 675 - 568)
menu_hitbox = button.Button(300, 696, 500 - 300, 759 - 696)
data_hitbox = button.Button(714, 706, 778 - 714, 782 - 706)

# BOTÓN BACK
return_hitbox = button.Button(12, 18, 165 - 12, 74 - 18)

# BOTONES DE LA PANTALLA DE JUEGO BÁSICA
prePlayPlayerActive_hitbox = button.Button(221, 502, 0, 0)
preBotActive_hitbox = button.Button(221, 629, 0, 0)

# BOTONES DE LA PANTALLA MENU


# SECCIÓN DE MÚSICA
pygame.mixer.music.load('easy-lifestyle-137766.mp3')  # agregar música
pygame.mixer.music.set_volume(0.1)  # setear volumen

# hacer cada línea individualmente, para poder rodear la imagen con la hitbox
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


def playMusic():
    pygame.mixer.music.play(-1)  # reproducir música en bucle


# Condicion para cambiar de pantalla
main = True
menu = False
start = False
data = False
prePlay = False
playing = False
playMusic()

#                      COSAS DE PYMUNK

# Pymunk space
space = pymunk.Space()
static_body = space.static_body
# Con esta funcion le puedo pedir a pymunk que dibuje las formar que creo, en la ventana
draw_options = pymunk.pygame_util.DrawOptions(window)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game variables
diam = 36

# Colores
BG = [50, 50, 50]

# load images
table_image = pygame.image.load("Assets/Images/table.png").convert_alpha()
ball_images = []
for i in range(1, 17):
    ball_image = pygame.image.load(f"Assets/Images/bola{i}.png").convert_alpha()
    ball_image = pygame.transform.scale(ball_image, (diam * 2, diam * 2))
    ball_images.append(ball_image)


# Funcion para crear bolas
def create_ball(rad, pos):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, rad)
    shape.mass = 5
    shape.elasticity = 0.9
    # use pivot joint to add friction
    pivot = pymunk.PivotJoint(static_body, body, (0, 0), (0, 0))
    pivot.max_bias = 0  # Disable joint correction
    pivot.max_force = 500  # emulate linear friction

    space.add(body, shape, pivot)
    return shape


# Crear las bolas para el jogo
balls = []
rows = 5
# Bolas numeradas
for col in range(5):
    for row in range(rows):
        pos = (250 + (col*(diam+3)), 267 + (row*(diam+3)) + (col*diam/2))
        new_ball = create_ball((diam/2), pos)
        balls.append(new_ball)
    rows -= 1

# Bola blanca
pos = (888, (base_height/2))
cue_ball = create_ball((diam/2), pos)
balls.append(cue_ball)

# Crear los bordes de la mesa (usando las coordenadas donde quiero dibujarlos)
border = [
    [(88, 56), (109, 77), (555, 77), (564, 56)],
    [(621, 56), (630, 77), (1081, 77), (1102, 56)],
    [(89, 621), (110, 600), (556, 600), (564, 621)],
    [(622, 621), (630, 600), (1081, 600), (1102, 621)],
    [(56, 96), (77, 117), (77, 560), (56, 581)],
    [(1143, 96), (1122, 117), (1122, 560), (1143, 581)]
]


# Funcion para crear objetos del escenario
def create_table_border(poly_dims):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (0, 0)
    shape = pymunk.Poly(body, poly_dims)
    shape.elasticity = 0.8

    space.add(body, shape)


for b in border:
    create_table_border(b)


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
            if main == True:

                window.blit(game, (posX, posY))
                if start_hitbox.down(event) == True:
                    window.blit(game_start_click, (posX, posY))
                # MENU
                if menu_hitbox.down(event) == True:
                    window.blit(game_menu_click, (posX, posY))
                # DATOS
                if data_hitbox.down(event) == True:
                    window.blit(game_data_click, (posX, posY))
                if start_hitbox.up(event) == True:
                    main = False
                    start = True
                # MENU
                if menu_hitbox.up(event) == True:
                    menu = True
                    main = False
                # DATOS
                if data_hitbox.up(event) == True:
                    data = True
                    main = False

            # VENTANA DE PRE JUEGO
            if start == True and main == False:

                # dibujamos la hitbox
                prePlayPlayerActive_hitbox = button.Button(221, 502, 577 - 210, 585 - 502)
                preBotActive_hitbox = button.Button(221, 629, 577 - 210, 585 - 502)

                pygame.mixer.music.stop()
                window.fill(white_color)

                # DOWN EVENT

                if return_hitbox.down(event) == True:
                    window.blit(prePlayBackActive, (posX, posY))

                elif prePlayPlayerActive_hitbox.down(event) == True:
                    window.blit(prePlayPlayerActiveImage, (posX, posY))

                elif preBotActive_hitbox.down(event) == True:
                    window.blit(prePlayBotActive, (posX, posY))

                else:
                    window.blit(prePlayInactive, (posX, posY))

                # UP EVENT
                if prePlayPlayerActive_hitbox.up(event) == True:
                    playMusic()
                    start = False
                    playing = True
                    base_height = 678
                    base_width = 1200
                    window = pygame.display.set_mode((base_width, base_height), pygame.RESIZABLE)

                if return_hitbox.up(event) == True:
                    playMusic()
                    start = False
                    main = True

                if preBotActive_hitbox.up(event) == True:
                    playMusic()
                    start = False
                    main = True

            # VENTANA MENU
            if menu == True:
                window.fill(white_color)
                pygame.mixer.music.stop()

            # VENTANA DATOS
            if data == True:
                pygame.mixer.music.stop()

                if return_hitbox.down(event) == True:
                    window.blit(data_return, (posX, posY))
                else:
                    window.blit(data_image, (posX, posY))
                if return_hitbox.up(event) == True:
                    playMusic()
                    data = False
                    main = True






            # Es innecesario poner el .up event, esto provoca el error de los botones
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
            prePlayPlayerActive_hitbox.draw(window)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    else:
        # Time simulation
        clock.tick(FPS)
        space.step(1 / FPS)

        # Fill background
        window.fill(BG)

        # draw pool table
        window.blit(table_image, (0, 0))

        # draw pool balls
        # Utilizo el iterador i para obtener el nÃºmero de la bola
        # Esto debido a que el iterador ball solo me da la direccion de memoria del objeto ball
        for i, ball in enumerate(balls):
            window.blit(ball_images[i], (ball.body.position[0] - diam, ball.body.position[1] - diam))

        # Event Handler
        for event in pygame.event.get():
            # Disparar la bola blanca
            if event.type == pygame.MOUSEBUTTONUP:
                cue_ball.body.apply_impulse_at_local_point((-3500, 0), (0, 0))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # space.debug_draw(draw_options)
        pygame.display.update()

    # print(pygame.mouse.get_pos())
    clock.tick(60)
    pygame.display.flip()
