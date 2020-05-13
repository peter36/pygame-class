# Lesson 7 Notes: Player event

## Step 1: Set up the game loop
```python
import pygame

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    # process events, like key strokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # redraw the screen 
    pygame.display.update()

```

## Step 2: Set caption and icon

Add it after before the line with "# Game Loop"

```python
# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
```

## Step 3: Define player image and variables

Add the following lines before the line with "# Game Loop"

```python
# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))
```

Add the following to draw the player before "pygame.display.update()"

```python
player(playerX, playerY)
```

## Step 4: Add Keyboard interaction

Add the following lines in the event loop (for event...)

```python
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
```

## Step 5: Compute the player's new position

Add the following lines before "player(playerX, playerY)"

```python
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
```
