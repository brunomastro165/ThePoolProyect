import pygame, sys

import pymunk
from pygame.locals import *

ImagePalo = pygame.image.load("Assets/Images/paloNeutro.png")
# pos = pygame.mouse.get_pos()


class Palo:
    def __init__(self, pos):
        self.originalImage = ImagePalo
        self.angle = 0
        self.image = pygame.transform.rotate(self.originalImage, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, angle):
        self.angle = angle

    def draw(self, surface):
        self.image = pygame.transform.rotate(self.originalImage, self.angle)
        surface.blit(self.image,
                     ((self.rect.centerx - self.image.get_width() / 2),
          (self.rect.centery - self.image.get_height() / 2 )))
