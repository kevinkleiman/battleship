from flask import Flask, render_template
import sys
import Client as c

PORT = sys.argv[1]
FILE_NAME = sys.argv[2]
own_board = []
opponent_board = []

app = Flask(__name__)


@app.route("/own_board.html", methods=['GET', 'POST'])
def own_board_page():
    update_own_board(2, 4)
    s = ''
    for row in get_own_board():
        s += '\n'
        for ch in row:
            s += ch
    return render_template("own_board.html", own_board=s)


@app.route("/opponent_board.html")
def opponent_board_page():
    s = ''
    for row in get_opponent_board():
        s += '\n'
        for ch in row:
            s += ch
    update_opponent_board(c.get_response(c.get_r1())[0], c.get_response(c.get_r1())[1])
    return render_template("opponent_board.html", opponent_board=s)


def read_own_board():
    with open(FILE_NAME) as fileobj:
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


def update_own_board(x, y):
    own_board[x][y] = 'H'

    with open("board.txt", "w") as board:
        for i in range(10):
            board.write('\n')
            for j in range(10):
                board.write(own_board[i][j])
        board.close()


def update_opponent_board(x, y):
    if x != -1:
        opponent_board[x][y] = 'H'
    else:
        opponent_board[x][y] = 'M'


if __name__ == "__main__":
    create_opponent_board()
    read_own_board()
    app.run(debug=True, host="0.0.0.0", port=5000)

