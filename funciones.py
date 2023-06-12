import random

import pygame
import pymunk
import pymunk.pygame_util
import pygame.mixer

pygame.mixer.init()


def play_music():
    pygame.mixer.music.play(-1)  # reproducir musica en bucle


# Funcion para actualizar las imagenes con hover
def update_image(hitbox, image, event, window, pos_x, pos_y):
    if hitbox.hover():
        window.blit(image, (pos_x, pos_y))


# Funcion para hacer resposive los botones
def resposive_hitbox(obj, pos, window):
    obj.x = (window.get_width() - 800) / 2 + pos
    obj.hitbox = pygame.Rect(obj.x, obj.y, obj.width, obj.height)


# Funcion para crear objetos del escenario
def create_table_border(poly_dims, space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (0, 0)
    shape = pymunk.Poly(body, poly_dims)
    shape.elasticity = 0.8

    space.add(body, shape)


# MODIFICACION DE LA CLASE CIRCLE DE PYMUNK
class MyCircle(pymunk.Circle):
    def __init__(self, body, radius, tipo=""):
        super().__init__(body, radius)
        self.tipo = tipo


# Funcion para crear objetos ball
def create_ball(rad, pos, static_body, space):
    body = pymunk.Body()
    body.position = pos
    shape = MyCircle(body, rad)
    shape.mass = 5
    shape.elasticity = 0.9
    shape.collision_type = 0  # Establecer el collision_type aquí
    pivot = pymunk.PivotJoint(static_body, body, (0, 0), (0, 0))
    pivot.max_bias = 0
    pivot.max_force = 1500
    # Espacio
    space.add(body, shape, pivot)
    return shape


def change_pos(a, b, balls):
    auxiliar = balls[a].body.position
    balls[a].body.position = balls[b].body.position
    balls[b].body.position = auxiliar


def make_new_game(balls, diam, static_body, space, potted_balls, potted_balls_lisa, potted_balls_rayada):
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

            '''COMO LAS BALLS NO SON OBJETOS, NO TIENEN ATRIBUTOS O PARAMETROS, SIMPLEMENTE
            ES UNA FUNCION QUE DEVUELVE CIERTOS NUMEROS
            ASI QUE SE MODIFICO LA CLASE CIRCLE DE PYMUNK, PARA PODER TENER OBJETOS'''

            if 8 > len(balls) > 0:
                # print(f"Lisas: {len(balls)}")
                new_ball = create_ball((diam / 2), pos, static_body, space)
                new_ball.tipo = "lisa"
            if len(balls) == 0:  # LA ITERACION 0 POR ALGUN MOTIVO ES LA NUMERO 15, Y ES RAYADA, POR ESO ES ESTE IF
                # print(f"Rayadas: {len(balls)}")
                new_ball = create_ball((diam / 2), pos, static_body, space)
                new_ball.tipo = "rayada"
            if len(balls) > 8:
                # print(f"Rayadas: {len(balls)}")
                new_ball = create_ball((diam / 2), pos, static_body, space)
                new_ball.tipo = "rayada"
            if len(balls) == 8:
                # print(f"Negra: {len(balls)}")
                new_ball = create_ball((diam / 2), pos, static_body, space)
                new_ball.tipo = "negra"

            if new_ball:
                balls.append(new_ball)
        rows -= 1

    # Cambiando las bolas de lugar

    change_pos(0, 14, balls)
    change_pos(1, 5, balls)
    change_pos(2, 13, balls)
    change_pos(13, 8, balls)
    change_pos(4, 12, balls)
    change_pos(4, 9, balls)
    change_pos(7, 10, balls)
    change_pos(10, 6, balls)
    change_pos(3, 12, balls)
    change_pos(12, 10, balls)

    # Bola blanca
    pos = (888, (678 / 2))
    print(pos)
    cue_ball = create_ball((diam / 2), pos, static_body, space)
    cue_ball.tipo = "blanca"
    balls.append(cue_ball)

    cont_balls = 0
    for i in balls:
        print(f"{cont_balls} : {i.tipo}")
        cont_balls = cont_balls + 1

    balls[0].tipo = "lisa"
    balls[8].tipo = "rayada"
    balls[7].tipo = "negra"

    potted_balls_lisa.clear()
    potted_balls.clear()
    potted_balls_rayada.clear()


def calcular_probabilidad(prob):
    if random.randint(0, 100) > prob:
        return True
    else:
        return False
