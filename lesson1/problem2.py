h = 4
w = 8
for i in range(0, h):
    line = ''
    if (i == 0) or (i == h - 1):
        for j in range(0, w):
          line = line + '*'
    else:
        line = '*'
        for j in range(0, w - 2):
            line = line + ' '
        line = line + '*'
    print(line)
