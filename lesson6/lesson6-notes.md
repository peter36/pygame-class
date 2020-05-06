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
|-------------|-------------|
|QUIT | None  | 
|KEYDOWN| unicode, key, mod|
|KEYUP| key, mod|

## Homework

Modify the program in "PyGame Events" to response to "q" key, so that user can quit by pressing "q" key.

Before, you make changes to the program, you need to find out how to detect "q" key.  Let's do it together!

Step 1: Set a break point and observe what is in an "event". (_Hint:_ You can set breakpoint by clicking your mouse
next to the line number)

![Set Breakpoint](images/set_breakpoint.png)

Step 2: Click debug button (_Hint:_ The button that looks like a bug, which is next to the run button).  When debugging
started, press some key (like 'a', 'b' ... and 'q').  This picture below shows what you will see when you press
letter 'a'

![Debug Watch](images/debug_watch.jpg)

The value for the __event.key__ is actually 97 for letter 'a'.

Step 3:  After you figure out what value is letter 'q', you can modify the program to check if __event.key__
represent 'q', and then you can change the variable __running__ to False

