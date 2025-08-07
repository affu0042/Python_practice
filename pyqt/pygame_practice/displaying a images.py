import pygame 
pygame.init()
width, heigth = 500,600
screen = pygame.display.set_mode([width,heigth])
image = pygame.image.load(r"C:\Users\OMOLP76\Desktop\python\pygame_practice\car-racing-4394450_1280.jpg")
image = pygame.transform.scale(image,(200,200))
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    # screen.fill((0,0,0))
    image_position = (50,50)
    screen.blit(image, image_position)
    pygame.display.flip()
pygame.quit()