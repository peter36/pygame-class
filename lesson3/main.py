
def init_board(w, h):
    b = []
    for y in range(0, h):
        b.append([])
        for x in range(0, w):
            b[y].append(0)
    return b


board = init_board(3, 3)
print(board)
