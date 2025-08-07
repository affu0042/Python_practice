import pygame
import random

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Shooter")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)

# Player
player = pygame.Rect(300, 370, 30, 20)

# Bullets and blocks
bullets = []
blocks = []
for _ in range(20):
    x = random.randint(0, WIDTH - 20)
    y = random.randint(0, 300)
    blocks.append(pygame.Rect(x, y, 20, 20))

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
run = True
while run:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Fire bullet from player's position
            bullet = pygame.Rect(player.x + 12, player.y, 5, 10)
            bullets.append(bullet)

    # Move player with mouse
    mouse_x = pygame.mouse.get_pos()[0]
    player.x = mouse_x

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= 5
        if bullet.y < 0:
            bullets.remove(bullet)

    # Check collision with blocks
    for bullet in bullets[:]:
        for block in blocks[:]:
            if bullet.colliderect(block):
                bullets.remove(bullet)
                blocks.remove(block)
                score += 1
                break

    # Draw player
    pygame.draw.rect(screen, RED, player)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, BLACK, bullet)

    # Draw blocks
    for block in blocks:
        pygame.draw.rect(screen, BLUE, block)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
