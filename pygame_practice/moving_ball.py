import pygame 

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([500,500])
x = 250
y = 250
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0), (x,y), 40, 1)
    pygame.display.flip()
    x+=1
    y+=1

    clock.tick(30)

pygame.quit()
    