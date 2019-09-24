from flask import Flask, render_template, request
import sys

PORT = sys.argv[1]
FILE_NAME = sys.argv[2]
own_board = []
opponent_board = []
X = ' '
Y = ' '

app = Flask(__name__)


@app.route("/own_board.html")
def own_board_page():
    read_own_board()
    s = '<table>'
    for row in get_own_board():
        s += '<tr>'
        for ch in row:
            s += '<td style="font-size:35px">{}</td>'.format(ch)
        s += "</tr>"
    s += "</table>"
    return render_template("own_board.html", own_board=s)


@app.route("/x=<x>&y=<y>", methods=['GET', 'POST'])
def handle_fire(x, y):
    if request.method == 'POST':
        update_own_board(int(x), int(y))
    return render_template('handle_connection.html')


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


def get_own_board():
    return own_board


def update_own_board(x, y):
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
    own_board[x][y] = 'H'
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
