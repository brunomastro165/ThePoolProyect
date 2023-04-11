import pygame
import pymunk
import pymunk.pygame_util

# Pymunk space
space = pymunk.Space()
static_body = space.static_body




class Ball:
    # Funcion para crear bolas
    def __init__(self, rad, pos):
        self.body = pymunk.Body()
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, rad)
        self.shape.mass = 5
        self.shape.elasticity = 0.9
        # use pivot joint to add friction
        self.pivot = pymunk.PivotJoint(static_body, self.body, (0, 0), (0, 0))
        self.pivot.max_bias = 0  # Disable joint correction
        self.pivot.max_force = 500  # emulate linear friction

        space.add(self.body, self.shape, self.pivot)