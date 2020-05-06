import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print("You pressed {0:c}".format(event.key))
        elif event.type == pygame.KEYUP:
            print("You released {0:c}".format(event.key))

pygame.quit()
