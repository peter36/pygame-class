import random
import math
import pygame
from pygame import mixer
import time

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# define constants


#background = pygame.image.load("background.png")

# Caption and Icon
# pygame.display.set_caption("My Space Invader")
# icon = pygame.image.load('ufo.png')
# pygame.display.set_icon(icon)

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    # draw background image
    # screen.blit(background, (0, 0))

    # process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_LEFT:
            #    playerX_change = -0.3
            #if event.key == pygame.K_RIGHT:
            #    playerX_change = 0.3
            #if event.key == pygame.K_SPACE:
            #    bulletSound = mixer.Sound("laser.wav")
            #    bulletSound.play()
            print("key down")
        #if event.type == pygame.KEYUP:
        #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #        playerX_change = 0

    # handle player movement

    # handle enemy movement

    # update score

    # redraw the screen
    pygame.display.update()

# end of while
pygame.quit()
