import http.client
import sys


opponent_board = []


def fire(x, y, ip, port):
    try:
        connection = http.client.HTTPConnection(ip + ':' + port)
        connection.request('POST', "/x=" + x + "&y=" + y)
        r1 = connection.getresponse()
        if r1.status == 200:
            update_opponent_board(int(x), int(y))
        elif r1.status == 410:
            print('You have already fired to this location')
            update_opponent_board(-1, -1)

    except Exception:
        print('Error, Connection Refused')


def update_opponent_board(x, y):
    try:
        if x != -1:
            opponent_board[x][y] = 'H'
        else:
            opponent_board[x][y] = 'M'
    except IndexError:
        with open("opponent_board.txt") as fileobj:
            for line in fileobj:
                row = []
                for ch in line:
                    if ch != '\n':
                        row.append(ch)
                opponent_board.append(row)
        if x != -1:
            opponent_board[x][y] = 'H'
        else:
            opponent_board[x][y] = 'M'

    with open("opponent_board.txt", "w") as board:
        for i in range(10):
            if i != 0:
                board.write('\n')
            for j in range(10):
                board.write(opponent_board[i][j])


if __name__ == '__main__':
    fire(sys.argv[3], sys.argv[4], sys.argv[1], sys.argv[2])

