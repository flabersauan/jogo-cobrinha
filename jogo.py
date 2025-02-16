import pygame
from pygame.locals import *
from sys import exit

pygame.init()

pygame.display.set_caption('Jogo da cobrinha')

largura = 640
altura = 480

tela = pygame.display.set_mode((largura,altura))


while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (0,255,0), (largura/2,altura/2,30,10))



    pygame.display.update()

