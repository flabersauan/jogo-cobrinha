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

velocidade = 5

x_controle = velocidade
y_controle = 0

x_comida = randint(40,600)
y_comida = randint(50,430)

contador = 0

fonte = pygame.font.SysFont('Poppins', 30, bold=True, italic = False)

tela = pygame.display.set_mode((largura,altura))

relogio = pygame.time.Clock()

comprimento_inicial = 5

morreu = False
lista_corpo = []

def aumentar_cobra(lista_corpo):
    for XeY in lista_corpo:
        pygame.draw.rect(tela,(0,255,0), (XeY[0], XeY[1],20,20))

def reiniciar_jogo():
    global pontos,contador,comprimento_inicial,x_cobra,y_cobra,lista_corpo,lista_cabeca,x_comida,y_comida,morreu
    contador = 0
    comprimento_inicial = 5
    x_cobra = largura/2
    y_cobra = altura/2
    lista_corpo =[]
    lista_cabeca = []
    x_comida = randint(40,600)
    y_comida = randint(50,430)
    morreu = False


while True:
    relogio.tick(20)
    tela.fill((0,0,0))
    mensagem = f'Pontos {contador}'
    texto_formatado = fonte.render(mensagem, False, (255,255,255))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

        if evento.type == KEYDOWN:
            if evento.key == K_LEFT:
                if x_controle == velocidade:
                    exit()
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if evento.key == K_RIGHT:
                if x_controle == -velocidade:
                    exit()
                else:
                    x_controle = velocidade
                    y_controle = 0
            if evento.key == K_UP:
                if y_controle == velocidade:
                    exit()
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if evento.key == K_DOWN:
                if y_controle == -velocidade:
                    exit()
                else:
                    y_controle = velocidade
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
        comprimento_inicial += 3
    
    
    

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    if len(lista_corpo) > comprimento_inicial:
        del lista_corpo[0]
    lista_cabeca.append(y_cobra)
    lista_corpo.append(lista_cabeca)

    if lista_corpo.count(lista_cabeca) > 1 or  x_cobra >= largura or y_cobra >= altura or x_cobra <0 or y_cobra <0:
        morreu = True
        while morreu:
            fonte = pygame.font.SysFont('Poppins', 20, bold=True, italic = False)
            mensagem = 'Para reiniciar pressione a tecla "R"'
            texto_formatado = fonte.render(mensagem, False, (255,255,255))
            tela.fill((0,0,0))
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                if evento.type == KEYDOWN:
                    if evento.key == K_r:
                        reiniciar_jogo()

            tela.blit(texto_formatado, ((largura/2 - 100),altura/2))
            pygame.display.update()
    aumentar_cobra(lista_corpo)

    
    tela.blit(texto_formatado, (10,10))

    pygame.display.update()