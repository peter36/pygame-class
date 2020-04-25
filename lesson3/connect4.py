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

...
...
...


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


if __name__ == "__main__":
    main()

