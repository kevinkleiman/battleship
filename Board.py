own_board = []
opponent_board = []


def read_own_board():
    with open("board.txt") as fileobj:
        for line in fileobj:
            row = []
            for ch in line:
                if ch != '\n':
                    row.append(ch)
            own_board.append(row)


def create_opponent_board():
    for i in range(10):
        row = []
        for j in range(10):
            row.append("_")
        opponent_board.append(row)


def get_own_board():
    return own_board


def get_opponent_board():
    return opponent_board


def update_opponent_board(x, y, result):
    if result == 'h':
        opponent_board[x][y] = 'H'
    if result == 'm':
        opponent_board[x][y] = 'M'