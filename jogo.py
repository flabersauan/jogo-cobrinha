import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer.music.load('musica_fundo.mp3')
som_colisao = pygame.mixer.Sound('som_colisao.wav')
som_colisao.set_volume(0.5)
pygame.mixer.music.play(-1)
pygame.display.set_caption('Jogo da cobrinha') #Alterar nome da tela


largura = 640 #Largura da tela
altura = 480 #Altura da tela

x_cobra = largura/2 #Posição inicial da cobrinha na tela
y_cobra = altura/2

x_controle = 20
y_controle = 0

x_comida = randint(40,600)
y_comida = randint(50,430)

contador = 0

fonte = pygame.font.SysFont('Poppins', 30, bold=True, italic = False)

tela = pygame.display.set_mode((largura,altura))

relogio = pygame.time.Clock()

comprimento_inicial = 1
lista_corpo = []
def aumentar_cobra(lista_corpo):
    for XeY in lista_corpo:
        pygame.draw.rect(tela,(0,255,0), (XeY[0], XeY[1],20,20))

while True:
    relogio.tick(25)
    tela.fill((0,0,0))
    mensagem = f'Pontos {contador}'
    texto_formatado = fonte.render(mensagem, False, (255,255,255))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

        if evento.type == KEYDOWN:
            if evento.key == K_LEFT:
                x_controle = -20
                y_controle = 0
            if evento.key == K_RIGHT:
                x_controle = 20
                y_controle = 0
            if evento.key == K_UP:
                y_controle = -20
                x_controle = 0
            if evento.key == K_DOWN:
                y_controle = 20
                x_controle = 0

        x_cobra+= x_controle
        y_cobra+= y_controle

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    comida = pygame.draw.rect(tela, (255,0,0), (x_comida,y_comida, 20,20))

    if cobra.colliderect(comida):
        x_comida = randint(40,600)
        y_comida = randint(50,430)
        contador+=1
        som_colisao.play()
        comprimento_inicial += 1
    
    if x_cobra >= largura or y_cobra >= altura:
        exit()
    

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    if len(lista_corpo) > comprimento_inicial:
        del lista_corpo[0]
    lista_cabeca.append(y_cobra)
    lista_corpo.append(lista_cabeca)
    aumentar_cobra(lista_corpo)

    
    tela.blit(texto_formatado, (10,10))

    pygame.display.update()