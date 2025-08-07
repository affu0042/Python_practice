import pygame 

pygame.init()
screen = pygame.display.set_mode([500,500])
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255,0,0), (100,200,400,100),1 )
    pygame.display.flip()

pygame.quit()