import pygame 
from random import randint
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode([500,500])

class circle:
    def __init__(self):
        self.x = randint(0,500)
        self.y = randint(0,500)
        self.r = randint(0,50)
        self.x_speed = randint(-2,2)
        self.y_speed = randint(-2,2)
        self.color = (randint(0,255), randint(0,255), randint(0,255))
    def draw(self):
        pygame.draw.circle(screen, self.color,(self.x, self.y),self.r)
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
cir = [circle() for _ in range(5)]
run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    for c in cir:
        c.draw()
    for c in cir:
        c.move()
    pygame.display.flip()
    clock.tick(20)
pygame.quit()  





# import pygame 
# from random import randint

# pygame.init()
# screen = pygame.display.set_mode([500,500])

# clock = pygame.time.Clock()

# class moving_circle:
#     def __init__(self):
#         self.y = randint(0,500)
#         self.x = randint(-50,500)
#         self.r = randint(10,30)
#         self.color = (randint(0,255),randint(0,255),randint(0,255))
#         self._y_speed = randint(-2,2)
#         self._x_speed = randint(-2,2)
#     def draw(self):
#         pygame.draw.circle(screen, self.color, (self.x,self.y),self.r)
#     def move(self):
#         self.y += self._y_speed  
#         self.x += self._x_speed
# circles = [moving_circle() for _ in range(10)]
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     screen.fill((0,0,0))
#     for c in circles:
#         c.draw()
#     for c in circles:
#         c.move()
    
#     pygame.display.flip()
#     clock.tick(60)
# pygame.quit()
