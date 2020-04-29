# Lesson 4 - Review What We Have Learned

# Array:
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

## Mathematical operators:

```
+ add
- minus
* multiply
/ divide
% modulus (get the remainder in a division)
```

Try this:
```
a = 20 
b = 4
c = a + b
print(c)
```
Exercise: Try to use different mathematical operators, and see what is the result.

Now try
```
a = 15
b = 7
c = a % b
print(c)
```
Exercise: Try to use different value for a and b, and see what is the result.

## Comparison Operators

```
> means greater than
< means smaller than
>= means greater than or equal to
<= menas smaller than or equal to
== means equal
```

```
a = 20
b = 15
if a > b:
    print("Yes!")
else:
    print("No!")
```
Exercise: Try to replace with different comparison operators and see what is the result.  Try to
change the value of a and b and see.

## Logical operator
```
and ==> A and B ==> return True if both A and B are True (otherwise, return False)
or  ==> A or B ==> return True if one of A or B needs to be True (otherwise, return False)
not ==> not A ==> return True if A is False (return False if A is True)
```


```
a = 20
b = 15
c = 80
d = 100
if a > b and c < d:
    print("Yes!")
else:
    print("No!")

```

A and B == not(not A or not B))


# For-Loop

To scan value in an array one by one, you can use for-loop.

Example - Find the maximum value in an array:
```
def find_max(arr):
    max = arr[0]
    n = len(a)
    for i in range(0, n):
        if arr[i] > max:
            max = arr[i]
    return max

a = [325, 123, 21, 52, 789, 2, 32]
m = find_max(a)
print(m)
```

## A note on debugging

You can use:

1) print() to inspect value.
2) Set breakpoint and inspect variables.  Let me show you how to do this in PyCharm.

# Homework:
1. Write a function find_min() to find the minimum value in an array of number

_Hint_: Modify find_max() in the example above.

2. Write a function find_average() to get the average value of an array of number

_Hint_: Average means that you need to add all the numbers in an array, and divide by the number of elements

 