import pygame
import time
run = True
screen = pygame.display.set_mode([500,500])
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255,255,0))
    pygame.display.flip()
pygame.quit()
