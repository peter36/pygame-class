# tic-tac-toe


def init_board():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def player1_move(board, x, y):
    board[x][y] = 1


def player2_move(board, x, y):
    board[x][y] = 2


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


def who_won(board):
    # 0 means no one win, 1 means player 1 wins, 2 means player 2 wins
    result = 0
    # check row
    for y in range(0, 3):
        result = check_winning(board[0][y], board[1][y], board[2][y])
        if result > 0:
            return result
    # check col
    for x in range(0, 3):
        result = check_winning(board[x][0], board[x][1], board[x][2])
        if result > 0:
            return result
    # check diagonal:
    result = check_winning(board[0][0], board[1][1], board[2][2])
    if result > 0:
        return result
    result = check_winning(board[2][0], board[1][1], board[0][2])
    if result > 0:
        return result
    return 0


def check_winning(a, b, c):
    if (a == 1) and (b == 1) and (c == 1):
        return 1
    elif (a == 2) and (b == 2) and (c == 2):
        return 2
    else:
        return 0


def print_line():
    print("")


def is_full(board):
    result = True
    for y in range(0, 3):
        for x in range(0, 3):
            if board[x][y] == 0:
                result = False
                break
    return result


def input_player_move(player_number):
    x = input("Player {0}, enter your move X:".format(player_number))
    y = input("Player {0}, enter your move Y:".format(player_number))
    return int(x), int(y)


def computer_move(player_number, board):
    best_x = -1
    best_y = -1
    best_score = -1
    for y in range(0, 3):
        for x in range(0, 3):
            score = evaluate_move(player_number, x, y, board)
            if score > best_score:
                best_x = x
                best_y = y
                best_score = score
    return best_x, best_y


def evaluate_move(player_number, tx, ty, board):
    score = 0
    # already occupied ==> invalid move
    if board[tx][ty] > 0:
        return -999999
    # propose move
    board[tx][ty] = player_number
    # horizontal
    score += get_score(player_number, get_board(board, tx-2, ty), get_board(board, tx - 1, ty), get_board(board, tx,ty))
    score += get_score(player_number, get_board(board, tx-1, ty), get_board(board, tx, ty), get_board(board, tx + 1, ty))
    score += get_score(player_number, get_board(board, tx, ty), get_board(board, tx + 1, ty), get_board(board, tx + 2, ty))
    # vertical
    score += get_score(player_number, get_board(board, tx, ty-2), get_board(board, tx, ty-1), get_board(board, tx, ty))
    score += get_score(player_number, get_board(board, tx, ty-1), get_board(board, tx, ty), get_board(board, tx, ty+1))
    score += get_score(player_number, get_board(board, tx, ty), get_board(board, tx, ty+1), get_board(board, tx, ty+2))
    # diagonal NW -> SE
    score += get_score(player_number, get_board(board, tx-2, ty-2), get_board(board, tx-1, ty-1), get_board(board, tx, ty))
    score += get_score(player_number, get_board(board, tx-1, ty-1), get_board(board, tx, ty), get_board(board, tx+1, ty+1))
    score += get_score(player_number, get_board(board, tx, ty), get_board(board, tx+1, ty+1), get_board(board, tx+2, ty+2))
    # diagonal NE -> SW
    score += get_score(player_number, get_board(board, tx+2, ty-2), get_board(board, tx+1, ty-1), get_board(board, tx, ty))
    score += get_score(player_number, get_board(board, tx+1, ty-1), get_board(board, tx, ty), get_board(board, tx-1, ty+1))
    score += get_score(player_number, get_board(board, tx, ty), get_board(board, tx-1, ty+1), get_board(board, tx-2, ty+2))
    # undo move
    board[tx][ty] = 0
    return score


def get_score(player_number, a, b, c):
    if check_mate(player_number, a, b, c):
        return 1000000
    if counter_check(player_number, a, b, c):
        return 1000
    if check_opponent(player_number, a, b, c):
        return 100
    if has_potential(player_number, a, b, c):
        return 10
    return 0


def check_mate(player_number, a, b, c):
    if a == player_number and b == player_number and c == player_number:
        return True
    else:
        return False


def counter_check(player_number, a, b, c):
    if (a == player_number) and (b > 0 and b != player_number) and (c > 0 and c != player_number):
        return True
    elif (a > 0 and a != player_number) and (b == player_number) and (c > 0 and c != player_number):
        return True
    elif (a > 0 and a != player_number) and (b > 0 and b != player_number) and c == player_number:
        return True
    return False


def check_opponent(player_number, a, b, c):
    if (a == 0) and (b == player_number) and (c == player_number):
        return True
    elif (a == player_number) and (b == 0) and (c == player_number):
        return True
    elif (a == player_number) and (b == player_number) and (c == 0):
        return True
    return False


def has_potential(player_number, a, b, c):
    if (a == player_number) and (b == 0) and (c == 0):
        return True
    elif (a == 0) and (b == player_number) and (c == 0):
        return True
    elif (a == 0) and (b == 0) and (c == player_number):
        return True
    return False


def get_board(board, x, y):
    if x < 0 or x > 2 or y < 0 or y > 2:
        return -1
    else:
        return board[x][y]


def main():
    board = init_board()
    won = 0
    turn = 2
    computer_player = True
    while (won == 0) and (is_full(board) is False):
        print_board(board)
        print_line()
        if (turn == 1) or ((turn == 2) and (computer_player is False)):
            x, y = input_player_move(turn)
        else:
            x, y = computer_move(turn, board)
            print("Computer move to {0} {1}".format(x, y))
            print_line()
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
        if computer_player and won == 2:
            print("Computer has won!")
        else:
            print("Player {0} has won!!".format(won))
    else:
        print("It is a tie.")


if __name__ == "__main__":
    main()
