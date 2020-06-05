# Lesson 10: Shell Commands

pwd — return working directory name
```
$ pwd
/Users/peter
```

ls - list directory contents
```
$ ls
Projects/ Documents/
```

1) -l: (The lowercase letter “ell’’.) List in long format. (See below.) A total sum for all the file sizes is output on a line before the long listing
2) -h: used with the -l option, this changes the file sizes into something more readable, like 10G, 42M. In my head, I translate this to ‘human-readable’
3) -a: Short for ‘all’; include ‘hidden’ directory entries whose names begin with a dot (.)


You can combine the options:
```
$ ls -lha
```

cd — Change directory

```
$ cd Projects
```

cp — Copy

```
$ cp file1.txt file1.txt.bak
```

mv — Move

```
$ mv file1.txt file1.txt.bak
```

mkdir — Make directories

```
$ mkdir Projects
```
There’s one convenient argument to this command, -p. When you use it, any intermediate directories that don’t exist
yet will also be created. If you want to create your first project inside of “Projects” directly, you can do so with:
```
$ mkdir -p Projects/my_first_project
```

rmdir — Remove directories
```
$ rmdir Projects

```
-p also works
```
$ rmdir -p Projects/my_first_project
```
rm - To remove a file
```
rm myfile.txt
```


cat, less, tail, head — View the contents
You often want to quickly inspect the contents of a file. There are several ways to do this. Pick one that matches your use case:
```
cat — print everything on your screen
less — allows you to scroll through the file and even search inside it
tail — like cat, but only print the last 10 lines (by default)
head — like cat, but only shows the first 10 lines (by default)
```

echo - to show a prompt
```
echo "hello"
```

touch - to create an empty file
```
touch hello.py
```

Redirection and Pipe
```
> - Send command output to a new file
>> - Send command output to the end of an existing file
| - Send output of one command to the another command
```
