import random
import math
import pygame
from pygame import mixer

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#background = pygame.image.load("background.png")

# Caption and Icon
pygame.display.set_caption("My Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 16))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) * (enemyX - bulletX) + (enemyY - bulletY) * (enemyY - bulletY))
    if distance < 27:
        return True
    else:
        return False


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
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        explosionSound = mixer.Sound("explosion.wav")
        explosionSound.play()
        bulletY = 480
        bullet_state = "ready"
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)


    # handle player movement
    playerX = playerX + playerX_change
    if playerX <= 0:
        playerX = 736
    elif playerX >= 736:
        playerX = 0

    # handle enemy movement
    enemyX = enemyX + enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY = enemyY + enemyY_change
    if enemyX >= 736:
        enemyX_change = -0.3
        enemyY = enemyY + enemyY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        bulletY = bulletY - bulletY_change
        fire_bullet(bulletX, bulletY)

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # redraw the screen
    pygame.display.update()

# end of while
pygame.quit()
