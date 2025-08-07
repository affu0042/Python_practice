import pygame 
pygame.init()

screen = pygame.display.set_mode([600, 500])
clock = pygame.time.Clock()

base_font = pygame.font.Font(None, 32)
user_text = ''

# Fix: use pygame.Rect instead of tuple
input_rect = pygame.Rect(100, 200, 140, 40)
active_color = pygame.Color('red')
passive_color = pygame.Color('blue')

color = passive_color
active = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]  # Fix: remove last character
                else:
                    user_text += event.unicode

    color = active_color if active else passive_color
    screen.fill((255, 255, 255))
    
    pygame.draw.rect(screen, color, input_rect, 2)

    text_surface = base_font.render(user_text, True, (0, 0, 0))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(100, text_surface.get_width() + 10)

    pygame.display.flip()
    clock.tick(60)
