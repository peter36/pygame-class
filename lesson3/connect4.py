# connect-4

# Define the board's Width and Height as constant
WIDTH = 7
HEIGHT = 6


def init_board():
    b = []
    for x in range(0, WIDTH):
        b.append([])
        for y in range(0, HEIGHT):
            b[x].append(0)
    return b


def player1_move(board, x, y):
    board[x][y] = 1


def player2_move(board, x, y):
    board[x][y] = 2


def print_board(board):
    for y in range(0, HEIGHT):
        line = ''
        for x in range(0, WIDTH):
            if board[x][y] == 0:
                line = line + '-'
            elif board[x][y] == 1:
                line = line + 'X'
            elif board[x][y] == 2:
                line = line + 'O'
        print(line)


def who_won(board):
    # 0 means no one win, 1 means player 1 wins, 2 means player 2 wins
    result = 0
    # check row
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH - 4 + 1):
            result = check_winning(board[x][y], board[x+1][y], board[x+2][y], board[x+3][y])
            if result > 0:
                return result
    # check col
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT - 4 + 1):
            # print("{0} {1}".format(x, y))
            result = check_winning(board[x][y], board[x][y+1], board[x][y+2], board[x][y+3])
            if result > 0:
                return result
    # check diagonal NW to SE:
    for x in range(0, WIDTH - 4 + 1):
        for y in range(0, HEIGHT - 4 + 1):
            result = check_winning(board[x][y], board[x+1][y+1], board[x+2][y+2], board[x+3][y+3])
            if result > 0:
                return result
    # check diagonal NE to SW:
    for x in range(WIDTH - 4, WIDTH):
        for y in range(0, HEIGHT - 4 + 1):
            # print("{0} {1}".format(x, y))
            result = check_winning(board[x-3][y+3], board[x-2][y+2], board[x-1][y+1], board[x][y])
            if result > 0:
                return result

    return result


def check_winning(a, b, c, d):
    if (a == 1) and (b == 1) and (c == 1) and (d == 1):
        return 1
    elif (a == 2) and (b == 2) and (c == 2) and (d == 2):
        return 2
    else:
        return 0


def print_line():
    print("")


def is_full(board):
    result = True
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            if board[x][y] == 0:
                result = False
                break
    return result


def input_player_move(board, player_number):
    # Python 2.7, You need to change input => raw_input
    input_valid = False
    while input_valid is False:
        x = input("Player {0}, enter your move X:".format(player_number))
        x = int(x)
        if x >= 0 and x <= WIDTH - 1:
            input_valid = True
        if (input_valid):
            y = find_top_of_column(board, x)

    return x, y


def find_top_of_column(board, x):
    result = -1
    for y in range(0, HEIGHT):
        if board[x][y] == 0:
            result = y
    return result


def main():
    board = init_board()
    won = 0
    turn = 1
    while (won == 0) and (is_full(board) is False):
        print_board(board)
        print_line()
        x, y = input_player_move(board, turn)
        if turn == 1:
            player1_move(board, x, y)
        if turn == 2:
            player2_move(board, x, y)
        won = who_won(board)
        if turn == 1:
            turn = 2
        else:
            turn = 1
    print_board(board)
    print_line()
    if won > 0:
        print("Player {0} has won!!".format(won))
    else:
        print("It is a tie.")

'''
    print(board)
    print(board[0][0])
    print(board[0][1])
    print_board(board)
    print_line()
    player1_move(board, 1, 1)
    print_board(board)
    print_line()
    player2_move(board, 1, 0)
    print_board(board)
    print_line()
    player1_move(board, 0, 0)
    x, y = input_player_move(1)
    print("{0}, {1}".format(x, y))
'''

if __name__ == "__main__":
    main()

