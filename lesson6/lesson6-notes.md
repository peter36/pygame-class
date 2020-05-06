# Lesson 6 - Beginning PyGame

## Installation of PyGame Library

1. Go to Terminal (from bottom of the PyCharm)
```commandline
Microsoft Windows [Version 10.0.18362.778]
(c) 2019 Microsoft Corporation. All rights reserved.

(env) D:\Projects\github\pygame-class>
```

2. Install PyGame library
```commandline
pip install pygame
```

## Test PyGame

Create a new directory "lesson6" and create a file "main.py" under it.

```
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

## PyGame Events
```
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

```

|Event Type   | Parameters  | 
|QUIT | None  | 
|KEYDOWN| unicode, key, mod|
|KEYUP| key, mod|
