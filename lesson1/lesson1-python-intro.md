# Python Tutorial

## What is Python?

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

## What can Python do?

- Python can be used on a server to create web applications

- Python can be used to handle big data and perform complex mathematics, Machine Learning / Artificial Intelligence

- Python is good for teaching programming to beginners

## Why Python?

- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).

- Python has a simpler syntax

- Python runs on an interpreter, which means your program can be executed as you type it (No need to compile first) 

## Python version

Latest release is Python 3.  It has slight syntax difference from Python 2.  But Python 2 is installed
in many systems by default, like Mac OS X.  You can use either version in the beginning when we go through the lessons,
but later on, we will focus on Python 3 later.

# Python: Getting Started

To check your default python version, you can type this on your command shell.

```
$ python --version
```

For Mac users, I highly recommend install iterm2.

You can download here:

https://www.iterm2.com/downloads.html


For Windows users, I recommend either use Git bash (which comes from installation of Git on Windows), or just the 
default CMD prompt, but install GnuWin32 utilities, and GNU Make utility.  We will go over in later lesson. 


# Python Version

Type this in your shell:

```
$ python --version
```

You will see the version of your Python interpreter.  Either you will see something like 2.7 or 3.6, 3.7 or 3.8.

Note:  When you see $ in the beginning, it means a shell command, you do not need to type "$"

## To start python interpreter

Type this in your shell:

```
$ python
```

## Python syntax

Type this:

```
>>> print("Hello, World!")
Hello, World!
```

Note: When you see >>> in the beginning, it means it is from the Python interpreter interactive window,
you do not need to type ">>>"

Or if you have saved your file as "hello.py"

You can type:

```
$ python hello.py
```

## Python Indentation

Indentation refers to the spaces at the beginning of a code line.

Some other programming languages do not care indentation (just to improve readability), but in Python, correct
indentation is important, because it indicate a code block

```
score = 100
if score > 90:
    print("Great job!")
```

You cannot type like this, without indentation, it will give you error:

 ```
score = 100
if score > 90:
print("Great job!")
```

Python doesn't care how many spaces you use for indentation, but it must be consistent for the whole program.  Through
out this tutorial, let's use 4 spaces (which is the default in PyCharm editor).

You can have nested code block:

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

## Comments

Comments in Python.  Any line start with '#' is a comment, and will be ignored

```
# This is a comment
print("Hello, friend!!")
```
