import pygame
import sys
import time
from queue import PriorityQueue

# === Grid Settings ===
GRID_SIZE = 10
CELL_SIZE = 60
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE

# === Colors ===
WHITE = (255, 255, 255)
ROBOT_COLOR = (0, 100, 255)
OBJECT_COLOR = (255, 0, 0)
OBSTACLE_COLOR = (50, 50, 50)
PATH_COLOR = (0, 255, 0)

# === Initialize Pygame ===
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot - Clean Visual (No Grid)")
clock = pygame.time.Clock()

# === Directions (including diagonals) ===
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

# === Robot & Object ===
robot_pos = [0, 0]
object_pos = None  # user will click to place

# === Fixed Obstacles (3 walls) ===
obstacles = {
    (0, 5),  # Top center
    (9, 4),  # Bottom center-left
    (5, 9),  # Right center
}

# === A* Heuristic ===
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# === A* Pathfinding ===
def a_star(start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for dx, dy in DIRECTIONS:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < GRID_SIZE and 0 <= neighbor[1] < GRID_SIZE:
                if neighbor in obstacles:
                    continue

                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    open_set.put((f_score, neighbor))
    return None

# === Draw Screen (No grid) ===
def draw(path=[]):
    screen.fill(WHITE)

    # Obstacles
    for ox, oy in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, (oy*CELL_SIZE+5, ox*CELL_SIZE+5, CELL_SIZE-10, CELL_SIZE-10))

    # Path
    for px, py in path:
        pygame.draw.rect(screen, PATH_COLOR, (py*CELL_SIZE+20, px*CELL_SIZE+20, CELL_SIZE-40, CELL_SIZE-40))

    # Object
    if object_pos:
        ox, oy = object_pos
        pygame.draw.rect(screen, OBJECT_COLOR, (oy*CELL_SIZE+10, ox*CELL_SIZE+10, CELL_SIZE-20, CELL_SIZE-20))

    # Robot
    rx, ry = robot_pos
    pygame.draw.circle(screen, ROBOT_COLOR, (ry*CELL_SIZE + CELL_SIZE//2, rx*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//3)

    pygame.display.update()

# === Move Robot Step-by-Step ===
def move_along_path(path):
    for step in path:
        pygame.event.pump()  # Prevent freeze
        robot_pos[0], robot_pos[1] = step
        draw(path)
        time.sleep(0.3)

# === Main Loop ===
path = []
running = True
waiting_for_click = True

while running:
    draw(path)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Click to place object
        if event.type == pygame.MOUSEBUTTONDOWN and waiting_for_click:
            mx, my = pygame.mouse.get_pos()
            grid_x, grid_y = my // CELL_SIZE, mx // CELL_SIZE

            if (grid_x, grid_y) not in obstacles:
                object_pos = [grid_x, grid_y]
                print(f"🎯 Object placed at {object_pos}")
                path = a_star(tuple(robot_pos), tuple(object_pos))

                if path:
                    move_along_path(path)
                    print("✅ Robot reached the object.")
                else:
                    print("❌ No path to object.")
                waiting_for_click = False

pygame.quit()
