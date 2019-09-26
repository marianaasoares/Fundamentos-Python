"""Usando o código anterior, escreva um novo programa que, quando as teclas ‘w’, ‘a’, ‘s’ e ‘d’ forem pressionadas,
ele movimente o círculo com o texto“ clique” nas direções corretas.Caso colida com algum retângulo,
  o retângulo que participou da colisão deve desaparecer."""


import pygame

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))

preto = (0, 0, 0)
branco = (255, 255, 255)

x,y = 0

moveX,moveY = 0

clock= pygame.time.Clock()

sair = False

while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveX = -5
            if event.key == K_RIGHT:
                moveX = 5
            if event.key == K_UP:
                moveY = -5
            if event.key == K_DOWN:
                moveY = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveX = 0
            if event.key == K_RIGHT:
                moveX = 0
            if event.key == K_UP:
                moveY = 0
            if event.key == K_DOWN:
                moveY = 0
        tela.fill(branco)
        x+=moveX
        y+=moveY
        
        pygame.draw.circle(tela, preto, (x,y), 50)
        
        clock.tick(50)
        
        pygame.display.update()
        
pygame.quit()
        
