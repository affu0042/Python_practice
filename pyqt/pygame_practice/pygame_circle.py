import pygame
import time

pygame.init()

run = True
screen = pygame.display.set_mode([500,500])

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (0,0,255),(250,250),75,width=1)
    pygame.display.flip()
pygame.quit()
