import http.client
import sys
import Server as server


def fire(x, y, ip, port):
    server.update_opponent_board(int(x), int(y))
    try:
        connection = http.client.HTTPConnection(ip + ':' + port)
        # connection.request("GET", "/x=" + x + "&y=" + y)
        # r1 = connection.getresponse()
        # result = r1.read()
        # if r1.status == '200':
        #     server.update_opponent_board(x, y)
        # elif r1.status == '410':
        #     print('You have already fired to this location')
        #     server.update_opponent_board(-1, -1)

    except Exception:
        print('Error, Connection Refused')


if __name__ == '__main__':
    fire(sys.argv[3], sys.argv[4], sys.argv[1], sys.argv[2])

