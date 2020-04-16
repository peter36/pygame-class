h = 4
w = 8
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
