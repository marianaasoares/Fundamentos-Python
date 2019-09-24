"""Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta),
toda vez que a tecla espaço for pressionada ou o botão direito for clicado."""
import random
import pygame
from random import randint

from pygame.constants import K_SPACE, KEYDOWN

pygame.init()
pygame.font.init()
# Definir dimensões da tela
largura = 800
altura = 600
# criando a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Quadrado Amarelo")
# Definindo cor
amarelo = (255, 255, 0)
branco = (255, 255, 255)
# dimensões do quadrado
tamanho = 50
#pos_x = randint(0, (largura - tamanho) / 10) * 10
#pos_y = randint(0, (altura - tamanho) / 10) * 10

# Classe quadrado
class Quadrado():
    def __init__(self):
      self.largura = 50
      self.altura = 50
      self.x = random.randint(0, largura-self.largura)
      self.y = random.randint(20, altura-self.altura)
      self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
      self.cor = amarelo
    # funcao desenhar quadrado
    def desenha(self, tela):
      pygame.draw.rect(tela, self.cor, self.area)


saiu = False

quadrado = Quadrado()
desenha_quadrado = False
lista = []

while not saiu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            saiu = True
        if event.type == KEYDOWN and event.key == K_SPACE:
            tela.fill(branco)
            lista.append(pygame.mouse.get_pos())
            desenha_quadrado = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            tela.fill(branco)
            lista.append(pygame.mouse.get_pos())
            desenha_quadrado = True
        if desenha_quadrado == True:
            quadrado.desenha(tela)
            
    pygame.display.update()


pygame.quit()
