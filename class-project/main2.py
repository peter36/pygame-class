import random
import math
import pygame
from pygame import mixer
import time

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemyAlive = []
num_of_enemies = 1

for i in range(0, num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)
    enemyAlive.append(True)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

# Score

current_score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 600
textY = 10


# Game Over
gameover_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(current_score), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_gameover_text():
    gameover_text = gameover_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameover_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (int(x), int(y)))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (int(x), int(y)))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (int(x + 16), int(y + 16)))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) * (enemyX - bulletX) + (enemyY - bulletY) * (enemyY - bulletY))
    if distance < 27:
        return True
    else:
        return False


def num_enemies_alive():
    num_alive = 0
    for i in range(0, num_of_enemies):
        if enemyAlive[i]:
            num_alive += 1
    return num_alive


def recreate_enemies():
    global num_of_enemies
    for i in range(0, num_of_enemies):
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(50, 150)
        enemyAlive[i] = True
    num_of_enemies += 1
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)
    enemyAlive.append(True)


# Game Loop
running = True
gameover = False
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
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # handle player movement
    playerX = playerX + playerX_change
    if playerX <= 0:
        playerX = 736
    elif playerX >= 736:
        playerX = 0

    # handle enemy movement
    for i in range(0, num_of_enemies):
        if enemyAlive[i]:
            if enemyY[i] > 440:
                show_gameover_text()
                running = False
                gameover = True

            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                current_score += 1
                enemyAlive[i] = False
            else:
                enemyX[i] = enemyX[i] + enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 0.3
                    enemyY[i] = enemyY[i] + enemyY_change[i]
                if enemyX[i] >= 736:
                    enemyX_change[i] = -0.3
                    enemyY[i] = enemyY[i] + enemyY_change[i]

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bulletY = bulletY - bulletY_change
        fire_bullet(bulletX, bulletY)

    player(playerX, playerY)

    if num_enemies_alive() == 0:
        recreate_enemies()

    for i in range(0, num_of_enemies):
        if enemyAlive[i]:
            enemy(enemyX[i], enemyY[i], i)

    show_score(textX, textY)

    # redraw the screen
    pygame.display.update()

    if gameover:
        time.sleep(5) # wait for 5 seconds

# end of while
pygame.quit()
