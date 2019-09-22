from flask import Flask
import Board as b
import Client as c

IP = ''
PORT = 5000


app = Flask(__name__)


@app.route("/own_board", methods=['GET', 'POST'])
def own_board_page():
    # b.update_own_board(2, 4)
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

