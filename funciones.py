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
    space.add(body, shape, pivot)
    return shape


def change_pos(a, b, balls):
    auxiliar = balls[a].body.position
    balls[a].body.position = balls[b].body.position
    balls[b].body.position = auxiliar


def calcular_probabilidad(prob):
    if random.randint(0, 100) > prob:
        return True
    else:
        return False
