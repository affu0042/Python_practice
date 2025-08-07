import pygame 
pygame.init()

size = height, Wifth = 600,600

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

image = pygame.image.load(r"C:\Users\OMOLP76\Desktop\python\pygame_practice\car-racing-4394450_1280.jpg")

image_default_size = (200,200)

image = pygame.transform.scale(image, image_default_size)

image = pygame.transform.rotate(image,180)

defaul_image_position = (200,200)



run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    screen.fill((0,0,0))
    screen.blit(image,defaul_image_position)
    pygame.display.flip()
    clock.tick(1)

pygame.quit()    






# import pygame

# # Initialize Pygame
# pygame.init()

# # Set screen size
# SIZE = WIDTH, HEIGHT = 600, 600
# screen = pygame.display.set_mode(SIZE)

# # Set up the clock
# clock = pygame.time.Clock()

# # Load image
# image = pygame.image.load(r'C:\Users\OMOLP76\Desktop\python\pygame_practice\Modern_British_LED_Traffic_Light.jpg')

# # Resize image (optional, if needed)
# DEFAULT_IMAGE_SIZE = (200, 200)
# image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

# # Rotate image 180 degrees
# image = pygame.transform.rotate(image, 180)

# # Set image position on screen
# DEFAULT_IMAGE_POSITION = (200, 200)

# # Start the game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Fill screen with black
#     screen.fill((0, 0, 0))

#     # Draw the image
#     screen.blit(image, DEFAULT_IMAGE_POSITION)

#     # Update the screen
#     pygame.display.flip()

#     # Cap the frame rate
#     clock.tick(30)

# # Quit Pygame
# pygame.quit()
