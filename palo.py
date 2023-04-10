import pygame,sys

import pymunk
from pygame.locals import *

ImagePalo = pygame.image.load("Assets/Images/paloNeutro.png")
#pos = pygame.mouse.get_pos()
class Palo():
    def __init__(self, pos):
        self.originalImage = ImagePalo
        self.angle = 45
        self.image = pygame.transform.rotate(self.originalImage, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (888, 600)

    def draw(self, surface):
        self.image = pygame.transform.rotate(self.originalImage, self.angle)
        surface.blit(self.image, self.rect)