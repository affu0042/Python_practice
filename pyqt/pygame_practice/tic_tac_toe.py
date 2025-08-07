import pygame
import sys

# Initialize pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# Font
font = pygame.font.Font(None, 80)

# Game variables
board = ["-" for _ in range(9)]
current_player = "X"
winner = None
game_running = True

# Draw grid lines
def draw_lines():
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), LINE_WIDTH)

# Draw X and O marks
def draw_marks():
    for i in range(9):
        row = i // 3
        col = i % 3
        x = col * 100 + 30
        y = row * 100 + 20
        if board[i] == 'X':
            text = font.render("X", True, BLACK)
            screen.blit(text, (x, y))
        elif board[i] == 'O':
            text = font.render("O", True, RED)
            screen.blit(text, (x, y))

# Check for a win
def check_winner():
    global winner, game_running
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        a, b, c = condition
        if board[a] == board[b] == board[c] != "-":
            winner = board[a]
            game_running = False
            return

# Check for a tie
def check_tie():
    global game_running
    if "-" not in board and winner is None:
        game_running = False

# Game loop
while True:
    screen.fill(WHITE)
    draw_lines()
    draw_marks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_running and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // 100
            col = x // 100
            idx = row * 3 + col
            if board[idx] == "-":
                board[idx] = current_player
                check_winner()
                check_tie()
                current_player = "O" if current_player == "X" else "X"

    if not game_running:
        if winner:
            result_text = font.render(f"{winner} wins!", True, RED)
        else:
            result_text = font.render("Tie!", True, BLACK)
        screen.blit(result_text, (60, 130))

    pygame.display.update()
