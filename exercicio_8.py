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
tela = pygame.display.set_mode((largura, altura))

      
sair = False

while not sair:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
            
        tela.fill(branco)
        
        posicao_mouse = pygame.mouse.get_pos()
        
        if 250+100 > posicao_mouse[0] > 250 and 50+50 > posicao_mouse[1] > 50:
            pygame.draw.rect(tela, verde_claro,(250, 50, 100, 50))
        else:
            pygame.draw.rect(tela, verde_escuro,(250, 50, 100, 50))
        
                
    
pygame.quit()