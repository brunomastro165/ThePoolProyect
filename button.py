import pygame,sys
from pygame.locals import *

class Button:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.height = heigth

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        # dibujar el objeto
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def up(self,event):
        mouse_pos = pygame.mouse.get_pos()

        if(self.hitbox.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP):
            if event.button == 1:
                return True

    def down(self, event):
        mouse_pos = pygame.mouse.get_pos()

        if (self.hitbox.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 1:
                return True

    def hover(self, event):
        mouse_pos = pygame.mouse.get_pos()

        if(self.hitbox.collidepoint(mouse_pos)):
            return True
