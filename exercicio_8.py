"""Usando a biblioteca ‘pygame’, escreva um programa que desenha um botão (círculo) com o texto “clique” sobre ele
na parte superior da tela. Quando o botão for clicado, ele deve chamar uma função que desenha um retângulo em uma
posição aleatória na tela. Caso um retângulo apareça na mesma posição que um já existente, ambos devem ser eliminados."""

import pygame
import random

pygame.init()

largura = 600
altura = 400

verde_escuro = (155, 225, 152)
verde_claro = (173, 223, 179)
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0) 
tela = pygame.display.set_mode((largura, altura))

def botao(mensagem, x, y, raio, clica = None):
    posicao_mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
        
    if x+raio > posicao_mouse[0] > x and y+raio > posicao_mouse[1] > y:
        pygame.draw.circle(tela, verde_claro, [x, y], raio)
        if click[0] == 1 and clica != None:
            if clica == "cliquei":
                quadrado = Quadrado()
                lista.append(quadrado)            
    else:
        pygame.draw.circle(tela, verde_escuro, [x, y], raio)  
            
    fonte = pygame.font.Font("Roboto-Thin.ttf", 20)
    texto = fonte.render(mensagem, True, preto)
    texto_retangulo = texto.get_rect()
    texto_retangulo.center = ( (250+(100/2)), (75+(50/2)))
    tela.blit(texto, texto_retangulo)


class Quadrado():
    def __init__(self):
      self.largura = 50
      self.altura = 50
      self.x = random.randint(0, largura-self.largura)
      self.y = random.randint(20, altura-self.altura)
      self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
      self.cor = vermelho
    # funcao desenhar quadrado
    def desenha(self, tela):
      pygame.draw.rect(tela, self.cor, self.area)

lista = []

for i in lista:
    quadrado = Quadrado()
    quadrado.desenha(tela)
    lista.append(quadrado)



sair = False

while not sair:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
            
        tela.fill(branco)
        botao("Clique", 300, 100, 50, "cliquei")
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            quadrado = Quadrado()
            lista.append(quadrado)
            
        for i in lista:
            i.desenha(tela)
        
                
    
pygame.quit()