import pygame


# clase del objeto mesa, funciona igual que en java
class MesaObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # crear la hitbox
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        # dibujar el objeto
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def check_collision(self, other_rect):
        # comprobar si hay colision con otra hitbox
        return self.hitbox.colliderect(other_rect)
