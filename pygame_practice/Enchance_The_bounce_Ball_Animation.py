import pygame
from random import randint

screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()

class circle:
    def __init__(self):
        self.x = randint(0,500)
        self.y = randint(0,500)
        self.r = randint(10,50)
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.x_speed = randint(-2,2)
        self.y_speed = randint(-2,2)

    
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
    
    def wall_Collide(self):
        if self.x + self.r > 500:
            self.x_speed = self.x_speed * -1
            self.color = (randint(0,255), randint(0,255), randint(0,255))
        if self.x + self.r < 0:
            self.x_speed = self.x_speed * -1
            self.color = (randint(0,255), randint(0,255), randint(0,255))
        if self.y + self.r > 500:
            self.y_speed = self.y_speed * -1
            self.color = (randint(0,255), randint(0,255), randint(0,255))
        if self.y + self.r < 0:
            self.y_speed = self.y_speed * -1
            self.color = (randint(0,255), randint(0,255), randint(0,255))

class fast(circle):
    def __init__(self):
        super().__init__()
    def move(self):
        self.x += (self.x_speed*2)
        self.y += (self.y_speed*2)
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r,3)

class slow(circle):
    def __init__(self):
        super().__init__()
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r,1)

cir = []
for i in range(5):
    cir.append(fast())

for i in range(5):
    cir.append(slow())

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for i in range(10):
        cir[i].draw()
    for i  in range(10):
        cir[i].move()
    for i in range(10):
        cir[i].wall_Collide()
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()























# import pygame
# from random import randint

# pygame.init()

# screen = pygame.display.set_mode([500,500])
# clock = pygame.time.Clock()

# class circle:
#     def __init__(self):
#         self.x = randint(0,255)
#         self.y = randint(0,255)
#         self.r = randint(0,255)

#         self.color = (randint(0,255), randint(0,255), randint(0,255))

#         self.x_speed = randint(-2,2)
#         self.y_speed = randint(-2,2)
#     def move(self):
#         self.x += self.x_speed
#         self.y += self.y_speed
#     def wall_collide(self):
#         if self.x + self.r > 500:
#             self.x_speed *= -1
#             self.color = (randint(0,255), randint(0,255), randint(0,255))
#         if self.x + self.r < 0:
#             self.x_speed *= -1
#             self.color = (randint(0,255), randint(0,255), randint(0,255))
#         if self.y + self.r > 500:
#             self.y_speed *= -1
#             self.color = (randint(0,255), randint(0,255), randint(0,255))
#         if self.y + self.r < 0:
#             self.y_speed *= -1
#             self.color = (randint(0,255), randint(0,255), randint(0,255))
# class fastCircle(circle):
#     def __init__(self):
#         super().__init__()

#     def move(self):
#         self.x += (self.x_speed*2)
#         self.y += (self.y_speed*2)

#     def draw(self):
#         pygame.draw.circle(screen, self.color, (self.x,self.y), self.r, 2)
# class slowCircle(circle):
#     def __init__(self):
#         super().__init__()

#     def draw(self):
#         pygame.draw.circle(screen, self.color, (self.x,self.y), self.r, 2)

# cir = []
# for i in range(5):
#     cir.append(fastCircle())
# for i in range(5):
#     cir.append(slowCircle())

# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
    
#     # screen.fill(255,255,255)

#     for i in range(10):
#         cir[i].draw()
    
#     for i in range(10):
#         cir[i].move()
    
#     for i in range(10):
#         cir[i].wall_collide()
        
    
#     pygame.display.flip()
#     clock.tick(30)

# pygame.quit()





