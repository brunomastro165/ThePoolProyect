import pygame
import pymunk
import pymunk.pygame_util


# Funcion para cargar imagenes
def imageLoad(name):
    return pygame.image.load(name)


# Funcion para hacer resposive los botones
def resposiveHitbox(obj, pos, window):
    obj.x = (window.get_width() - 800) / 2 + pos
    obj.hitbox = pygame.Rect(obj.x, obj.y, obj.width, obj.height)


def playMusic():
    pygame.mixer.music.play(-1)  # reproducir música en bucle


# Funcion para crear objetos del escenario
def create_table_border(poly_dims, space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (0, 0)
    shape = pymunk.Poly(body, poly_dims)
    shape = pymunk.Poly(body, poly_dims)
    shape.elasticity = 0.8

    space.add(body, shape)


# Funcion para actualizar las imagenes con hover
def updateImage(hitbox, image, event, window, posX, posY):
    if hitbox.hover(event):
        window.blit(image, (posX, posY))


def changePos(a, b,balls):
    auxiliar = balls[a].body.position
    balls[a].body.position = balls[b].body.position
    balls[b].body.position = auxiliar


def makeNewGame(balls, diam, static_body, space):
    # Crear las bolas para el juego
    for ball in balls:
        ball.body.position = (-1000, -1000)
        ball.body.velocity = (0.0, 0.0)
    balls.clear()
    rows = 5
    # Bolas numeradas

    for col in range(5):
        for row in range(rows):
            pos = (250 + (col * (diam + 3)), 267 + (row * (diam + 3)) + (col * diam / 2))

            # CÓMO LAS BALLS NO SON OBJETOS, NO TIENEN ATRIBUTOS O PARÁMETROS, SIMPLEMENTE
            # ES UNA FUNCIÓN QUE DEVUELVE CIERTOS NÚMEROS
            # ASÍ QUE SE MODIFICÓ LA CLASE CIRCLE DE PYMUNK, PARA PODER TENER OBJETOS

            if 8 > len(balls) > 0:
                # print(f"Lisas: {len(balls)}")
                new_ball = create_ball((diam / 2), pos, "lisas", static_body, space)
                new_ball.tipo = "lisa"
            if len(balls) == 0:  # LA ITERACION 0 POR ALGÚN MOTIVO ES LA NÚMERO 15, Y ES RAYADA, POR ESO ES ESTE IF
                # print(f"Rayadas: {len(balls)}")
                new_ball = create_ball((diam / 2), pos, "rayadas", static_body, space)
                new_ball.tipo = "rayada"
            if len(balls) > 8:
                # print(f"Rayadas: {len(balls)}")
                new_ball = create_ball((diam / 2), pos, "rayadas", static_body, space)
                new_ball.tipo = "rayada"
            if len(balls) == 8:
                # print(f"Negra: {len(balls)}")
                new_ball = create_ball((diam / 2), pos, "negra", static_body, space)
                new_ball.tipo = "negra"

            if new_ball:
                balls.append(new_ball)
        rows -= 1

    # Cambiando las bolas de lugar

    changePos(0, 14, balls)
    changePos(1, 5, balls)
    changePos(2, 13, balls)
    changePos(13, 8, balls)
    changePos(4, 12, balls)
    changePos(4, 9, balls)
    changePos(7, 10, balls)
    changePos(10, 6, balls)
    changePos(3, 12, balls)
    changePos(12, 10, balls)

    # Bola blanca
    pos = (888, (678 / 2))
    print(pos)
    cue_ball = create_ball((diam / 2), pos, "blanca", static_body, space)
    cue_ball.tipo = "blanca"
    balls.append(cue_ball)

    contBalls = 0
    for i in balls:
        print(f"{contBalls} : {i.tipo}")
        contBalls = contBalls + 1

    balls[0].tipo = "lisa"
    balls[8].tipo = "rayada"
    balls[7].tipo = "negra"


'''
IMPORTANTÍSIMO
'''


# MODIFICACION DE LA CLASE CIRCLE DE PYMUNK
class MyCircle(pymunk.Circle):
    def __init__(self, body, radius, tipo=""):
        super().__init__(body, radius)
        self.tipo = tipo


# Funcion para crear objetos ball
def create_ball(rad, pos, tipo, static_body, space):
    body = pymunk.Body()
    body.position = pos
    shape = MyCircle(body, rad)
    shape.mass = 5
    shape.elasticity = 0.9
    pivot = pymunk.PivotJoint(static_body, body, (0, 0), (0, 0))
    pivot.max_bias = 0
    pivot.max_force = 1500
    tipo = ""
    # Espacio
    space.add(body, shape, pivot)
    return shape
