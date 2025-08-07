import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([500, 500])

# Start from visible positions
x1 = 250
y1 = 250

x2 = 400
y2 = 100

x3 = 100
y3 = 400

x4 = 50
y4 = 50

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))  # Clear screen

    # Draw circles
    pygame.draw.circle(screen, (0, 0, 0), (x1, y1), 20, 1)
    pygame.draw.circle(screen, (255, 0, 0), (x2, y2), 25, 1)
    pygame.draw.circle(screen, (0, 0, 255), (x3, y3), 30, 1)
    pygame.draw.circle(screen, (0, 255, 0), (x4, y4), 40, 1)

    pygame.display.flip()

    # Update positions
    x1 -= 3
    y1 -= 3

    x2 -= 4
    y2 += 4

    x3 -= 5
    y3 += -5

    x4 += 7
    y4 += 7

    clock.tick(1)

pygame.quit()
