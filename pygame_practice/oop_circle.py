import pygame 
from random import randint
pygame.init()

run = True

clock = pygame.time.Clock()
screen = pygame.display.set_mode([500,500])

class circle:
    def __init__(self):
        self.x = randint(-50,500)
        self.y = randint(0,500)
        self.r = randint(10,50)
        self.color = (randint(0,255), randint(0,255), randint(0,255))
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

circles = [circle() for _ in range(10)]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    for c in circles:
        c.draw()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()