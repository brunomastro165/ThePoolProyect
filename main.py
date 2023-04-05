import pygame, sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PoolGame")

posX = 0
posY = 0
pantalla_principal = pygame.image.load("PLAY (1).png")

#cantidad de pixeles que se moverá la imagen
velocidad = 200
blanco=(255,255,255)
derecha= False
izquierda = False
arriba = False
abajo = False

rectangulo_hitbox = pygame.Rect(231,568, 575-231, 675-568)
window.blit(pantalla_principal,(posX, posY))
game = False

while True:
    mouse_x,mouse_y = pygame.mouse.get_pos()
    if(game == True):
        window.fill(blanco)
        #window.blit(mesa_pool_, (posX, posY))

    for event in pygame.event.get():
        #1 = izquierdo 2 = rueda 3 = derecho
        #and ((mouse_x >= 229 and mouse_y >= 568) and (mouse_x >= 567 and mouse_y >= 658))
        if event.type == pygame.MOUSEBUTTONDOWN and game == False:
            mouse_pos = pygame.mouse.get_pos()

            if rectangulo_hitbox.collidepoint(mouse_pos):
                if event.button == 1:
                    game = True

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Mover imágenes con el mouse

        '''
    posX, posY = (pygame.mouse.get_pos())
    posX = posX-100
    posY = posY-100
        '''

    print(pygame.mouse.get_pos())
    pygame.display.update()