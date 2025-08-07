import pygame 
pygame.init()

Width, Height = 480, 480
screen = pygame.display.set_mode([Width,Height])
square_size = Width//8

white = (255,255,255)
black = (0,0,0)

def chessBowards():
    for row in range(8):
        for col in range(8):
            color = white if (col + row)%2 ==0 else black
            pygame.draw.rect(screen , color, (col*square_size,row*square_size,square_size,square_size))
            pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    chessBowards()

pygame.quit()    














# import pygame
# import sys

# pygame.init()
# WIDTH,HEIGHT = 480,480

# SQUARE_SIZE = WIDTH//8

# screen = pygame.display.set_mode([WIDTH, HEIGHT])

# WHITE,BLACK = (255,255,255), (0,0,0)

# run = True
# def draw_chessboard():
#     for row in range(8):
#         for col in range(8):
#             color = WHITE if (row + col)%2==0 else BLACK
#             pygame.draw.rect(screen, color, (col*SQUARE_SIZE,row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     draw_chessboard()
#     pygame.display.flip()