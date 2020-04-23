def init_board():
    b = [[0,0,0], [0,0,0], [0,0,0]]
    return b

def print_board(board):
    for y in range(0, 3):
        line = ''
        for x in range(0, 3):
            if board[x][y] == 0:
                line = line + '-'
            elif board[x][y] == 1:
                line = line + 'X'
            elif board[x][y] == 2:
                line = line + 'O'
        print(line)


def print_line():
    print('')


def player1_move(board, x, y):
    board[x][y] = 1


def player2_move(board, x, y):
    board[x][y] = 2


def who_won(board):
    result = 0
    # check all 3 rows
    for y in range(0, 3):
        result = check_winning(board[0][y], board[1][y], board[2][y])
        if result > 0:
            return result
    # check all 3 columns
    for x in range(0, 3):
        result = check_winning(board[x][0], board[x][1], board[x][2])
        if result > 0:
            return result
    # check 2 diagonals
    result = check_winning(board[0][0], board[1][1], board[2][2])
    if result > 0:
        return result
    result = check_winning(board[2][0], board[1][1], board[0][2])
    if result > 0:
        return result
    return result


# return 1 if a, b, c are all 1
# return 2 if a, b, c, are all 2
def check_winning(a, b, c):
    if (a == 1) and (b == 1) and (c == 1):
        return 1
    elif (a == 2) and (b == 2) and (c == 2):
        return 2
    else:
        return 0


def is_full(board):
    result = True
    for y in range(0, 3):
        for x in range(0, 3):
            if board[x][y] == 0:
                result = False
                break
    return result


def input_player_move(player_number, board):
    # Python 2.7, You need to change input => raw_input
    input_valid = False
    while input_valid is False:
        x = input("Player {0}, enter your move X:".format(player_number))
        x = int(x)
        y = input("Player {0}, enter your move Y:".format(player_number))
        y = int(y)
        if (x >= 0 and x <= 2) and (y >= 0 and y <= 2):
            input_valid = True
        else:
            print("Invalid Move!")
        if input_valid and board[x][y] != 0:
            print("The space is taken!")
            input_valid = False
    return int(x), int(y)


def print_result(won):
    if won == 0:
        print("It is a tie!")
    else:
        print("Player {0} has won!!".format(won))

def main():
    board = init_board()
    won = 0
    turn = 1
    while (won == 0) and (is_full(board) is False):
        print_board(board)
        x, y = input_player_move(turn, board)
        if turn == 1:
            player1_move(board, x, y)
        else:
            player2_move(board, x, y)
        if turn == 1:
            turn = 2
        else:
            turn = 1
        won = who_won(board)
    # end of while-loop
    print_board(board)
    print_result(won)


main()

