import random
import math
import pygame
from pygame import mixer
import time

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption("Race Car Game")
icon = pygame.image.load('racecar-icon.png')
pygame.display.set_icon(icon)

# define FPS (Frame per second)
FPS = 30

# Create player car
player_x = 0
player_y = 0
player_speed_x = 0
player_speed_y = 0
player_image = pygame.image.load('racecar-red.png')


def init_player_car():
    global player_x, player_y
    player_x = 400 - 72
    player_y = 520

def update_player_car_position():
    global player_x, player_y
    player_x = player_x + player_speed_x
    player_y = player_y - player_speed_y


# Draw player car
def draw_player_car():
    screen.blit(player_image, (int(player_x), int(player_y)))


# Define enemy cars
MAX_ENEMY_CARS = 20
level = 1
num_enemy_cars = 10
enemy_x = []
enemy_y = []
enemy_alive = []
enemy_speed_x = []
enemy_speed_y = []
enemy_image = []

for i in range(0, MAX_ENEMY_CARS):
    enemy_x.append(300 + random.randint(-300, 300))
    enemy_y.append(100 + random.randint(-100, 100))
    enemy_alive.append(True)
    enemy_speed_x.append(0)
    enemy_speed_y.append(0)
    n = random.randint(0, 2)
    if n == 0:
        enemy_image.append(pygame.image.load('racecar-green.png'))
    elif n == 1:
        enemy_image.append(pygame.image.load('racecar-blue.png'))
    else:
        enemy_image.append(pygame.image.load('racecar-gray.png'))


# Draw enemy car with index i
def draw_enemy_car(i):
    screen.blit(enemy_image[i], (int(enemy_x[i]), int(enemy_y[i])))


# Update enemy car location here
def update_enemy_car(i):
    pass


# Game Loop
clock = pygame.time.Clock()
init_player_car()
running = True
while running:
    dt = clock.tick(FPS)

    # RGB = Red, Green, Blue
    screen.fill((0, 50, 50))

    # process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed_x = -5
            if event.key == pygame.K_RIGHT:
                player_speed_x = 5
            if event.key == pygame.K_UP:
                if player_speed_y <= 0:
                    player_speed_y = 5
            if event.key == pygame.K_DOWN:
                if player_speed_y <= 0:
                    player_speed_y = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speed_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed_y = 0

    # handle player movement
    update_player_car_position()
    draw_player_car()

    # handle enemy movement
    for i in range(0, num_enemy_cars):
        if enemy_alive[i]:
            update_enemy_car(i)

    for i in range(0, num_enemy_cars):
        if enemy_alive[i]:
            draw_enemy_car(i)

    # redraw the screen
    pygame.display.update()
# end of while

pygame.quit()
