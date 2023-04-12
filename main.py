import pygame, sys
import pymunk
import pymunk.pygame_util
import button
import mesa
import palo
import math
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


# Funcion para crear objetos del escenario
def create_table_border(poly_dims):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (0, 0)
    shape = pymunk.Poly(body, poly_dims)
    shape = pymunk.Poly(body, poly_dims)
    shape.elasticity = 0.8

    space.add(body, shape)


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

# Cargando Imagenes

# Pantalla Principal
game = imageLoad("Images/PLAY.png")
game_start_click = imageLoad("Images/PLAY (ACTIVE).png")
game_menu_click = imageLoad("Images/MENU (ACTIVE).png")
game_data_click = imageLoad("Images/PLAY DATOS.png")

# Pantalla de Datos
data_image = imageLoad("Images/DATOS (PAGINA).png")
data_return = imageLoad("Images/DATOS (PAG ACTIVA).png")

# Pantalla Menu
    # Cargamos Imagenes
imagenPrincpal = imageLoad("Images/MENU_PRINCIPAL.png")
imagenSiFacil = imageLoad("Images/M_P_SI_FACIL.png")
imagenSiFacilBack = imageLoad("Images/M_P_SI_FACIL_BACK.png")
imagenSiMedio = imageLoad("Images/M_P_SI_MEDIO.png")
imagenSiMedioBack = imageLoad("Images/M_P_SI_MEDIO_BACK.png")
imagenSiDificil = imageLoad("Images/M_P_SI_DIFICIL.png")
imagenSiDificilBack = imageLoad("Images/M_P_SI_DIFICIL_BACK.png")
imagenNoFacil = imageLoad("Images/M_P_NO_FACIL.png")
imagenNoFacilBack = imageLoad("Images/M_P_NO_FACIL_BACK.png")
imagenNoMedio = imageLoad("Images/M_P_NO_MEDIO.png")
imagenNoMedioBack = imageLoad("Images/M_P_NO_MEDIO_BACK.png")
imagenNoDificil = imageLoad("Images/M_P_NO_DIFICIL.png")
imagenNoDificilBack = imageLoad("Images/M_P_NO_DIFICIL_BACK.png")
    # Generamos variable para cambiar las imagenes de menu
imagenActual = imagenNoMedio

# Pantalla PrePlay
prePlayInactive = imageLoad("Images/PrePlayInactive.png")
prePlayPlayerActiveImage = imageLoad("Images/PrePlayPlayerActive.png")
prePlayBotActive = imageLoad("Images/PrePlayBotActive.png")
prePlayBackActive = imageLoad("Images/PrePlayBackActive.png")

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

# BOTONES DE LA PANTALLA MENU
fullscreenSi_hitbox = button.Button(406, 355, 484-406, 436-355)
fullscreenNo_hitbox = button.Button(621, 360, 700-621, 432-360)
diffFacil_hitbox = button.Button(404, 474, 695-404, 560-474)
diffMedio_hitbox = button.Button(405, 574, 693-405, 657-574)
diffDificil_hitbox = button.Button(407, 684, 697-407, 760-684)

# SECCIÓN DE MÚSICA
pygame.mixer.music.load('easy-lifestyle-137766.mp3')  # agregar música
pygame.mixer.music.set_volume(0.1)  # setear volumen

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
playMusic()

# Condiciones para los botones del menu
screenSiPress = False
screenNoPress = True
Facil = False
Medio = True
dificil = False

# COSAS DE PYMUNK

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
force = 0
max_force = 10000
force_direction = 1
taking_shot = True
powering_up = False

# Colores
BG = (50, 50, 50)
RED = (255, 0, 0)

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
        pos = (250 + (col*(diam+3)), 267 + (row*(diam+3)) + (col*diam/2))
        new_ball = create_ball((diam/2), pos)
        balls.append(new_ball)
    rows -= 1

# Bola blanca
pos = (888, (678/2))
print(pos)
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

for b in border:
    create_table_border(b)



# Objeto palo (instancia de la clase palo)
palo_p1 = palo.Palo(balls[-1].body.position)

# Barra de poder del paliño
power_bar = pygame.Surface((10, 20))
power_bar.fill(RED)

while True:
    # mouse_x, mouse_y = pygame.mouse.get_pos()  # posición cartesiana del mouse

    if not playing:
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

                # dibujamos la hitbox
                prePlayPlayerActive_hitbox = button.Button(221, 319, 577 - 210, 585 - 502)
                preBotActive_hitbox = button.Button(221, 441, 577 - 210, 585 - 502)

                pygame.mixer.music.stop()
                window.fill(white_color)

                # DOWN EVENT

                if return_hitbox.hover(event):
                    window.blit(prePlayBackActive, (posX, posY))

                elif prePlayPlayerActive_hitbox.hover(event):
                    window.blit(prePlayPlayerActiveImage, (posX, posY))

                elif preBotActive_hitbox.hover(event):
                    window.blit(prePlayBotActive, (posX, posY))

                else:
                    window.blit(prePlayInactive, (posX, posY))

                # UP EVENT

                if prePlayPlayerActive_hitbox.down(event):
                    playMusic()
                    start = False
                    playing = True
                    base_height = 678
                    base_width = 1200
                    window = pygame.display.set_mode((base_width, base_height), pygame.RESIZABLE)

                if return_hitbox.down(event):
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

                # VOLVER AL PRINCIPAL

                if return_hitbox.down(event) == True:
                    menu = False
                    main = True

                # SI ESTA APRETADO SI

                if fullscreenSi_hitbox.down(event) == True:
                    screenSiPress = True
                    screenNoPress = False
                    imagenActual = imagenSiMedio
                    window.blit(imagenActual, (posX, posY))
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

                if fullscreenNo_hitbox.down(event) == True:
                    screenNoPress = True
                    screenSiPress = False
                    imagenActual = imagenNoMedio
                    window.blit(imagenActual, (posX, posY))
                else:
                    window.blit(imagenActual, (posX, posY))


                # Cosas de frontEnd
                if screenSiPress:
                    if Facil:
                        imagenActual = imagenSiFacil
                        window.blit(imagenActual, (posX, posY))
                        if return_hitbox.hover(event) == True:
                            window.blit(imagenSiFacilBack, (posX, posY))
                    if Medio:
                        imagenActual = imagenSiMedio
                        window.blit(imagenActual, (posX, posY))
                        if return_hitbox.hover(event) == True:
                            window.blit(imagenSiMedioBack, (posX, posY))
                    if dificil:
                        imagenActual = imagenSiDificil
                        window.blit(imagenActual, (posX, posY))
                        if return_hitbox.hover(event) == True:
                            window.blit(imagenSiDificilBack, (posX, posY))

                elif screenNoPress:
                    if Facil:
                        imagenActual = imagenNoFacil
                        window.blit(imagenActual, (posX, posY))
                        if return_hitbox.hover(event) == True:
                            window.blit(imagenNoFacilBack, (posX, posY))
                    if Medio:
                        imagenActual = imagenNoMedio
                        window.blit(imagenActual, (posX, posY))
                        if return_hitbox.hover(event) == True:
                            window.blit(imagenNoMedioBack, (posX, posY))
                    if dificil:
                        imagenActual = imagenNoDificil
                        window.blit(imagenActual, (posX, posY))
                        if return_hitbox.hover(event) == True:
                            window.blit(imagenNoDificilBack, (posX, posY))

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
    else:
        # Time simulation
        clock.tick(FPS)
        space.step(1 / FPS)

        # Fill background
        window.fill(BG)

        # draw pool table
        window.blit(table_image, (0, 0))

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

        if taking_shot:
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
            for b in range(math.ceil(force/2000)):
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
            if event.type == pygame.MOUSEBUTTONDOWN and taking_shot is True:
                powering_up = True
            if event.type == pygame.MOUSEBUTTONUP and taking_shot is True:
                powering_up = False

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # space.debug_draw(draw_options)
        pygame.display.update()
    #print(pygame.mouse.get_pos())
    clock.tick(FPS)
    pygame.display.flip()
