from flask import Flask
import Board as b
import Client as c

IP = ''
PORT = 5000


class Server:
    def __init__(self, ip):
        self.ip = ip


    def fire(self, x, y):
        c.fire(x, y)

    def result(self):
        pass

    def setup(self):
        self.ip = input("Enter Opponent's IP address: ")

    def get_ip(self):
        return self.ip


app = Flask(__name__)


@app.route("/own_board", methods=['GET', 'POST'])
def own_board_page():
    s = ''
    for row in b.get_own_board():
        s += '\n'
        for ch in row:
            s += ch
    return s


@app.route("/opponent_board")
def opponent_board_page():
    s = ''
    for row in b.get_opponent_board():
        s += '\n'
        for ch in row:
            s += ch
    return s



if __name__ == "__main__":
    b.create_opponent_board()
    b.read_own_board()

    app.run(debug=True, host="0.0.0.0", port=80)

