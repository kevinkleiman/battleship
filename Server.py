from flask import Flask, render_template, request
import sys

# Kevin Kleiman, Arynn Collins, Corey Lagor
# CSCI 466 Programming Assignemnt 1
# 9/23/19

PORT = sys.argv[1]
FILE_NAME = sys.argv[2]
own_board = []
opponent_board = []
C = 0
B = 0
R = 0
D = 0
S = 0
SUNK = 0
OUTCOME = ''
X = ' '
Y = ' '

app = Flask(__name__)


@app.route("/own_board.html")
def own_board_page():
    global OUTCOME
    read_own_board()
    s = '<table>'
    for row in own_board:
        s += '<tr>'
        for ch in row:
            s += '<td style="font-size:35px">{}</td>'.format(ch)
        s += "</tr>"
    s += "</table>"
    if OUTCOME == 'lose':
        return render_template("own_board.html", own_board=s,
                               outcome='You have lost the game! Better Luck Next Time!')
    return render_template("own_board.html", own_board=s)


@app.route("/x=<x>&y=<y>", methods=['GET', 'POST'])
def handle_fire(x, y):
    global C, B, R, S, D, SUNK, OUTCOME
    if request.method == 'POST':
        try:
            if own_board[int(x)][int(y)] == '_':
                response = app.response_class(status=200, response='hit=0')
                update_own_board(int(x), int(y), 'm')
            elif own_board[int(x)][int(y)] == 'H' or own_board[int(x)][int(y)] == 'M':
                response = app.response_class(status=410)
            elif own_board[int(x)][int(y)] == 'C':
                C += 1
                if C == 5:
                    SUNK += 1
                    response = app.response_class(status=200, response='hit=1/&sink=C')
                else:
                    response = app.response_class(status=200, response='hit=1')
                update_own_board(int(x), int(y), 'h')
            elif own_board[int(x)][int(y)] == 'B':
                B += 1
                if B == 4:
                    SUNK += 1
                    response = app.response_class(status=200, response='hit=1/&sink=B')
                else:
                    response = app.response_class(status=200, response='hit=1')
                update_own_board(int(x), int(y), 'h')
            elif own_board[int(x)][int(y)] == 'R':
                R += 1
                if R == 3:
                    SUNK += 1
                    response = app.response_class(status=200, response='hit=1/&sink=R')
                else:
                    response = app.response_class(status=200, response='hit=1')
                update_own_board(int(x), int(y), 'h')
            elif own_board[int(x)][int(y)] == 'S':
                S += 1
                if S == 3:
                    SUNK += 1
                    response = app.response_class(status=200, response='hit=1/&sink=S')
                else:
                    response = app.response_class(status=200, response='hit=1')
                update_own_board(int(x), int(y), 'h')
            elif own_board[int(x)][int(y)] == 'D':
                D += 1
                if D == 2:
                    SUNK += 1
                    response = app.response_class(status=200, response='hit=1/&sink=D')
                else:
                    response = app.response_class(status=200, response='hit=1')
                update_own_board(int(x), int(y), 'h')
        except IndexError:
            response = app.response_class(status=404)
        if SUNK == 5:
            response = app.response_class(status=200, response='win')
            OUTCOME = 'lose'
    return response


@app.route("/opponent_board.html")
def opponent_board_page():
    read_opponent_board()
    s = '<table>'
    for row in opponent_board:
        s += '<tr>'
        for ch in row:
            s += '<td style="font-size:35px">{}</td>'.format(ch)
        s += "</tr>"
    s += "</table>"
    return render_template("opponent_board.html", opponent_board=s)


def read_own_board():
    try:
        temp = []
        with open(FILE_NAME) as fileobj:
            for line in fileobj:
                row = []
                for ch in line:
                    if ch != '\n':
                        row.append(ch)
                temp.append(row)
        for i in range(10):
            for j in range(10):
                own_board[i][j] = temp[i][j]
    except IndexError:
        with open(FILE_NAME) as fileobj:
            for line in fileobj:
                row = []
                for ch in line:
                    if ch != '\n':
                        row.append(ch)
                own_board.append(row)


def read_opponent_board():
    temp = []
    with open("opponent_board.txt") as fileobj:
        for line in fileobj:
            row = []
            for ch in line:
                if ch != '\n':
                    row.append(ch)
            temp.append(row)
    for i in range(10):
        for j in range(10):
            opponent_board[i][j] = temp[i][j]


def update_own_board(x, y, result):
    temp = []
    with open(FILE_NAME) as fileobj:
        for line in fileobj:
            row = []
            for ch in line:
                if ch != '\n':
                    row.append(ch)
            temp.append(row)
    for i in range(10):
        for j in range(10):
            own_board[i][j] = temp[i][j]
    if result == 'h':
        own_board[x][y] = 'H'
    if result == 'm':
        own_board[x][y] = 'M'
    else:
        pass
    with open(FILE_NAME, "w") as board:
        for i in range(10):
            if i != 0:
                board.write('\n')
            for j in range(10):
                board.write(own_board[i][j])


def create_opponent_board():
    for i in range(10):
        row = []
        for j in range(10):
            row.append("_")
        opponent_board.append(row)

    with open("opponent_board.txt", "w") as board:
        for i in range(10):
            if i != 0:
                board.write('\n')
            for j in range(10):
                board.write(opponent_board[i][j])


if __name__ == "__main__":
    read_own_board()
    create_opponent_board()
    app.run(debug=True, host="0.0.0.0", port=5000)
