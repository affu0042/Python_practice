import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Avoid Game")

clock = pygame.time.Clock()

# Load player car
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\OMOLP76\Desktop\python\pygame_practice\car-racing-4394450_1280.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 0

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Load enemy cars
class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\OMOLP76\Desktop\python\pygame_practice\car-racing-4394450_1280.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-200, -100)
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# Groups
all_sprites = pygame.sprite.Group()
enemy_cars = pygame.sprite.Group()

# Create player
player = PlayerCar()
all_sprites.add(player)

# Enemy spawn timer
enemy_spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_spawn_event, 1000)  # every 1 second

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == enemy_spawn_event:
            enemy = EnemyCar()
            all_sprites.add(enemy)
            enemy_cars.add(enemy)

    # Key press detection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.speed = -5
    elif keys[pygame.K_RIGHT]:
        player.speed = 5
    else:
        player.speed = 0

    # Update sprites
    all_sprites.update()

    # Collision detection
    if pygame.sprite.spritecollide(player, enemy_cars, False):
        print("Collision! Game Over!")
        running = False

    # Drawing
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
