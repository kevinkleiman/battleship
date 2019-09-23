import http.client
import sys


IP = sys.argv[1]
PORT = sys.argv[2]
X = sys.argv[3]
Y = sys.argv[4]


def fire():
    try:
        coor = []
        connection = http.client.HTTPConnection(IP + ':' + PORT)
        connection.request("GET", "/x=" + X + "&y=" + Y)
        r1 = connection.getresponse()
        result = r1.read()

        if r1.status == '200':
            if '1' in str(result):
                coor.append(X)
                coor.append(Y)
                return coor
            if '0' in str(result):
                coor.append('M')
                return coor

    except Exception:
        print('Error, Connection Refused')

