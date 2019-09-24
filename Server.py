from flask import Flask, render_template
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = sys.argv[1]
FILE_NAME = sys.argv[2]
own_board = []
opponent_board = []

app = Flask(__name__)


@app.route("/own_board.html", methods=['GET', 'POST'])
def own_board_page():
    s = '<table>'
    for row in get_own_board():
        s += '<tr>'
        for ch in row:
            s += '<td style="font-size:35px">{}</td>'.format(ch)
        s += "</tr>"
    s += "</table>"
    return render_template("own_board.html", own_board=s)


@app.route("/opponent_board.html")
def opponent_board_page():
    s = '<table>'
    for row in opponent_board:
        s += '<tr>'
        for ch in row:
            s += '<td style="font-size:35px">{}</td>'.format(ch)
        s += "</tr>"
    s += "</table>"
    return render_template("opponent_board.html", opponent_board=s)


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
        except:
            self.send_response(404)
        self.end_headers()


def read_own_board():
    with open(FILE_NAME) as fileobj:
        for line in fileobj:
            row = []
            for ch in line:
                if ch != '\n':
                    row.append(ch)
            own_board.append(row)


def read_opponent_board():
    with open("opponent_board.txt") as fileobj:
        for line in fileobj:
            row = []
            for ch in line:
                if ch != '\n':
                    row.append(ch)
            opponent_board.append(row)


def get_own_board():
    return own_board


def update_own_board(x, y):
    own_board[x][y] = 'H'

    with open(FILE_NAME, "w") as board:
        for i in range(10):
            if i != 0:
                board.write('\n')
            for j in range(10):
                board.write(own_board[i][j])


if __name__ == "__main__":
    read_own_board()
    read_opponent_board()
    app.run(debug=True, host="0.0.0.0", port=5000)
