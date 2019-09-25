import http.client
import sys

# Kevin Kleiman, Arynn Collins, Corey Lagor
# CSCI 466 Programming Assignemnt 1
# 9/23/19


opponent_board = []


def fire(x, y, ip, port):
    try:

        connection = http.client.HTTPConnection(ip + ':' + port)
        connection.request('POST', "/x=" + x + "&y=" + y)
        r1 = connection.getresponse()
        result = r1.read()
        sinks = 0
        if result.decode('utf-8') == 'win':
            print('You Won!')
            update_opponent_board(int(x), int(y), 'h')
        elif result.decode('utf-8') == 'hit=1':
            update_opponent_board(int(x), int(y), 'h')
        elif result.decode('utf-8') == 'hit=0':
            update_opponent_board(int(x), int(y), 'm')
        elif result.decode('utf-8') == 'hit=1/&sink=C':
            update_opponent_board(int(x), int(y), 'h')
            print('You sunk a Carrier')
            sinks += 1
        elif result.decode('utf-8') == 'hit=1/&sink=B':
            update_opponent_board(int(x), int(y), 'h')
            print('You sunk Battleship')
            sinks += 1
        elif result.decode('utf-8') == 'hit=1/&sink=R':
            update_opponent_board(int(x), int(y), 'h')
            print('You sunk Frigate')
            sinks += 1
        elif result.decode('utf-8') == 'hit=1/&sink=S':
            update_opponent_board(int(x), int(y), 'h')
            print('You sunk Submarine')
            sinks += 1
        elif result.decode('utf-8') == 'hit=1/&sink=D':
            update_opponent_board(int(x), int(y), 'h')
            print('You sunk a Destroyer')
            sinks += 1
        elif r1.status == 410:
            print('You have already fired to this location')
        elif r1.status == 404:
            print('Coordinates are out of bounds')
        elif r1.status == 400:
            print('Fire message not formatted correctly')

    except ConnectionRefusedError:
        print('Error, Connection Refused')


def update_opponent_board(x, y, result):
    try:
        if result == 'h':
            opponent_board[x][y] = 'H'
        elif result == 'm':
            opponent_board[x][y] = 'M'
        else:
            pass
    except IndexError:
        with open("opponent_board.txt") as fileobj:
            for line in fileobj:
                row = []
                for ch in line:
                    if ch != '\n':
                        row.append(ch)
                opponent_board.append(row)
        if result == 'h':
            opponent_board[x][y] = 'H'
        elif result == 'm':
            opponent_board[x][y] = 'M'
        elif result == 'x':
            pass

    with open("opponent_board.txt", "w") as board:
        for i in range(10):
            if i != 0:
                board.write('\n')
            for j in range(10):
                board.write(opponent_board[i][j])


if __name__ == '__main__':
    fire(sys.argv[3], sys.argv[4], sys.argv[1], sys.argv[2])

