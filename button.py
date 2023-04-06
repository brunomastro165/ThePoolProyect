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


    #Me falta terminar esto, ya voy a ver bien cómo hacerlo, pero voy bien, es una clase para no tener que hacer mil botones diferentes
    def is_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        if(self.hitbox.collidepoint(mouse_pos)):
            print("COLISIÓN")
            if pygame.event.get(MOUSEBUTTONDOWN):
                return True