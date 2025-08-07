import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Grid configuration
GRID_SIZE = 10
CELL_SIZE = 60
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ROBOT_COLOR = (0, 100, 255)
OBJECT_COLOR = (255, 0, 0)
GRID_COLOR = (200, 200, 200)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Navigation Simulation")

# Robot starting position
robot_pos = [0, 0]

# Get object position from user
try:
    x = int(input(f"Enter object X (0 to {GRID_SIZE-1}): "))
    y = int(input(f"Enter object Y (0 to {GRID_SIZE-1}): "))
    assert 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE
    object_pos = [x, y]
except:
    print("Invalid input. Defaulting object to (5, 5)")
    object_pos = [5, 5]

# Draw grid + elements
def draw_grid():
    screen.fill(WHITE)
    
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

    # Draw object
    obj_x, obj_y = object_pos
    pygame.draw.rect(screen, OBJECT_COLOR, (obj_y * CELL_SIZE + 5, obj_x * CELL_SIZE + 5, CELL_SIZE - 10, CELL_SIZE - 10))
    
    # Draw robot
    rob_x, rob_y = robot_pos
    pygame.draw.circle(screen, ROBOT_COLOR, (rob_y * CELL_SIZE + CELL_SIZE // 2, rob_x * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

    pygame.display.update()

# Move robot one step
def move_robot():
    rx, ry = robot_pos
    ox, oy = object_pos

    if rx < ox:
        robot_pos[0] += 1
    elif rx > ox:
        robot_pos[0] -= 1
    elif ry < oy:
        robot_pos[1] += 1
    elif ry > oy:
        robot_pos[1] -= 1

# Main loop
draw_grid()
clock = pygame.time.Clock()
reached = False

while not reached:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move_robot()
    draw_grid()
    time.sleep(0.3)

    if robot_pos == object_pos:
        print("🎯 Robot reached the object!")
        reached = True

# Wait before exit
time.sleep(2)
pygame.quit()
