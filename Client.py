import http.client
import sys


def get_r1():
    try:
        connection = http.client.HTTPConnection(IP + ':' + PORT)
        connection.request("GET", "/x=" + X + "&y=" + Y)
        r1 = connection.getresponse()
        return r1

    except Exception:
        print('Error, Connection Refused')


def get_response(r1):
    result = r1.read()
    coor = []
    if '1' in str(result):
        coor.append(X)
        coor.append(Y)
        return coor
    if '0' in str(result):
        coor.append(-1)
        return coor


if __name__ == '__main__':
    IP = sys.argv[1]
    PORT = sys.argv[2]
    X = sys.argv[3]
    Y = sys.argv[4]

