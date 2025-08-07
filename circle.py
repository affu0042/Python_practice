import pygame

run = True

pygame.init()
screen = pygame.display.set_mode([500,500])

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,0), (250,250),60,1)
    pygame.display.flip()
pygame.quit()


# import pygame
# import time
# run = True
# pygame.init()
# screen = pygame.display.set_mode([500,500])
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     screen.fill((255,255,255))
#     pygame.draw.circle(screen,(0,0,255),(250,250),75,width=1)
#     pygame.display.flip()
# pygame.quit()
