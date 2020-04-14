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

#Homework:
## Printing with pattern

Try this and run:
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
You will see a pattern like this:
```
    *
   **
  ***
 ****
*****
```

Now, how will you modify the program, so that it can print a pattern like this:
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
