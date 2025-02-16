import pygame
from pygame.locals import *
from sys import exit

pygame.init()

pygame.display.set_caption('Jogo da cobrinha')

largura = 640
altura = 480

x = largura/2
y = altura/2


tela = pygame.display.set_mode((largura,altura))

relogio = pygame.time.Clock()

while True:
    relogio.tick(20)
    tela.fill((0,0,0))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_LEFT]:
        x = x-10
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x+10
    if pygame.key.get_pressed()[K_UP]:
        y -= 10
    if pygame.key.get_pressed()[K_DOWN]:
        y+= 10
             
    pygame.draw.rect(tela, (0,255,0), (x,y,30,10))


    pygame.display.update()

