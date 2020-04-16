# Print statement
Try this and run:
```
print("hello, my friend!!")
```

# Variable
## Integer type
Type this and run:
```
a = 10
print(a)
```
## Floating point number type
Type this and run:
```
a = 10.2
print(a)
```
## String variable
```
name = 'Peter'
print(name)
```

# Operator
## Numbers (include both Integer and Floating point number types)
Type this and run:
```
a = 20
b = 5
c = a + b
print(c)
```
Exercise: Try to change the '+' sign to other operators ( '-' for minus, '*' for multiply, '/' for divide)

You can also use parenthesis:

Try this and run: 
 ```
x = 3
y = (x * 2) + 1
print(y)
```
Exercise: Try to change variable 'x' to 'i', 'y' to 'j' and run
 
## String operator

String concatenation (join two strings together)

Type this and run:
```
name = 'Peter'
greeting = 'Hello'
phrase = greeting + name + '!!'
print(phrase)
```
Exercise: 
1) Try to fix the program above to print properly as 'Hello Peter!!'
2) Try to change the name to your own name and run

## For-loop
Use to repeat the same action for a number of times.
Type this and run:
 ```
for i in range(0, 5):
    print(i)
```
Type this and run:
```
for i in range(0, 5):
    print('*')
```
Exercise: Try to change the range from (0, 5) to (0, 10), and run

## Nested For-loop

You can also have For-loop inside a For-loop.

Try this:
```
for i in range(0, 3):
    print('i = {0}'.format(i))
    for j in range(0, 4):
        print('j = {0}'.format(j))
```

Exercise:
1. Try to change the range of i from range(0,3) to range(0, 5) or other value.
2. Try to change the range of For-j to range(0, i)  (instead of 0, 10)

Let's get back to our example of printing stars.  Try this:
```
for i in range(0, 5):
    stars = ''
    for j in range(0, i):
        stars = stars + '*'
    print(stars)
 ```
Exercise:  Try to change the range of second for-loop to range(0, i + 1), and run.  What is the difference?

## If-statement

If-statement is used to make decision.

Try this:
```
score = 100
if score < 50:
    print("You failed!")
else:
    print("You passed!")
```
Exercise: Try to change score to 90, 40, and run.  What do you see at the output?

More complex decision making.  'elif' is a short-hand for "else if".

Try this:
```
score = 100
if score < 50:
    print("You failed!")
else:
    print("You passed!")
    if score > 90:
        print("You got an A")
    elif score > 80:
        print("You got a B")
    elif score > 70:
        print("You got a C")
    else:
        print("You got a D")
``` 
Exercise: Try to change score to 90, 85, 75, 60, 40, 30 and run.  What do you see at the output?

# Homework:
## Printing with pattern

Instruction: To submit your homework, please commit your code to your own 'pygame-class' GitHub repository,
under 'lesson1' directory by midnight 4/18 (Sunday).  Please save your solution as 'problem1.py' and 
'problem2.py'

### Problem 1.

We are given this program to print out a pattern:

```
for i in range(0, 5):
    spaces = ''
    for j in range(0, 5 - i - 1):
        spaces = spaces + ' '
    stars = ''
    for j in range(0, i + 1):
        stars = stars + '*'
    print(spaces + stars)
```
Try and run.  You will see a pattern like this:


```
    *
   **
  ***
 ****
*****
```

Now, how will you modify the program, so that it can print a pattern like this?
```
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
```
Hint: You just need to analyze the pattern, and change the range.  Think about using multiplication and relate
variable i and j.  Be careful with indentation when you run the code.



### Problem 2.

We are given a program to print square.  We would like to modify this to print rectangle.

```
n = 5
for i in range(0, n):
    line = ''
    if (i == 0) or (i == n - 1):
        for j in range(0, n):
          line = line + '*'
    else:
        line = '*'
        for j in range(0, n - 2):
            line = line + ' '
        line = line + '*'
    print(line)
```

Try the above program.  Also try to change the first line (n = 5) to different values, like 8, 10, etc.
Can you try also n = 1, and n = 2, n = 3?  Why does it still work when n = 1 or 2?

Now, we would like to modify the above program and print out a rectangle, with given width and height.
Can you modify the above program?

You should start your program like this:
```
h = 4
w = 8
# copy and modify the for-loops in the square-printing program here
```

With h = 4 and w = 8, we would like to see a pattern like this:
```
********
*      *
*      *
********
```

Hint: You can reuse the code to print square, by modifying n => h or n => w.  The key is to find out
where n should be changed to w, and where n should be change to h.
