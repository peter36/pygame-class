# Lesson 2 - Function, Array (List in Python)

## Function

```
def say_hello(name):
    print("Hello {0}".format(name))
```

Try to run the following program:
```
def say_hello(name):
    print("Hello {0}".format(name))


say_hello('Peter')
say_hello('Isaac')

```

Function can also return a value
```
def add_number(a, b):
    c = a + b
    return c
```

What is the result if we do `print(add_number(3, 4))`?

What do you expect?

## List (or Array)
Python has 4 collection data types.  They are:
- __List__
- __Tuple__
- __Set__
- __Dictionary__ 

We will focus on List right now.  We will talk about other collection types if needed.
Python does not have a real "array" type out of the box, like other languages, but 
the __List__ structure can be used as __array__


```
my_favorite_fruits = ["apple", "orange", "strawberry"]
print(my_favorite_fruits)
```

```
my_favorite_fruits = ["apple", "orange", "strawberry"]
for fruit in my_favorite_fruits:
    print(fruit)
```

You can also access list item by index:
```
cars = ["Ford", "Toyota", "BMW", "Tesla"]
print(cars[0])
print(cars[1])
```

What do you expect if we do `print(cars[2])` and `print(cars[3])`?  What will happen if you do `print(cars[4])` or `print(cars[-1])` ?

## List of List (2-D Array)

To represent a 2-D data, you can use List of List (2-D Array).

For example, if you want to represent the 9 square in a Tic-Tac-Toe game, you can do this:

```
board = [ [0,0,0], [0, 0, 0], [0, 0, 0] ]
```

So then you can access the element by `board[0][0]`, `board[0][1]`, etc.


## While statement

A `while' loop evaluate the condition, and will exit from the loop if the condition is false.

Try this:
```
i = 1
while i < 6:
    print(i)
    i += 1
```

Typically in a game, we will do something like this:

```
gameover = False
while not gameover:
    # play game...
    # ...
    # ...
    if is_dead(player):
        gameover = True
```

## More advanced example.  How to print a circle?

For the basic formula, we can use Pythagorean Theorem

a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>

You can look at the illustration here:

https://www.mathopenref.com/coordbasiccircle.html

### Step 1.  Figure out the formula:

Let's say we want to draw a circle with radius = r:

x<sup>2</sup> + y<sup>2</sup> = r<sup>2</sup>

Let's rewrite this:

x<sup>2</sup> = r<sup>2</sup> - y<sup>2</sup>

And then rewrite this as:

x = sqrt( r<sup>2</sup> - y<sup>2</sup> )
 
### Step 2: Write a function to print a square

Look at this sample code:

```
import math

def print_circle(radius):
    size = radius * 2 + 1
    for y in range(0, size):
        line = ''
        for x in range(0, size):
            line = line + '*'
        print(line)

print_circle(4)
```

### Step 3: Use Pythagorean Theorem's formula to decide print "*" or " "

```
import math

def print_circle(radius):
    size = radius * 2 + 1
    center = radius
    for y in range(0, size):
        line = ''
        for x in range(0, size):
            # We need to get the integer value for the tx value below
            # tx = math.sqrt(radius*radius - (center-y)*(center-y))
            tx = int(math.sqrt(radius*radius - (center-y)*(center-y)) + 0.5)
            if (x == center + tx) or (x == center - tx):
                line = line + '*'
            else:
                line = line + ' '
        print(line)

print_circle(8)

```

# Homework
1. Write a function to print a rectangle with given width and height?  You should start your program as:

```
def print_rectangle(w, h):

```
Hint: Modify from the problem 2's program from last week's lesson.








