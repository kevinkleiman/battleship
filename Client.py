import http.client
import sys


coor = []


def fire(x, y, ip, port):
    try:
        connection = http.client.HTTPConnection(ip + ':' + port)
        connection.request("GET", "/x=" + x + "&y=" + y)
        r1 = connection.getresponse()
        result = r1.read()
        if r1.status == '200':
            coor.append(x)
            coor.append(y)
        elif r1.status == '410':
            print('You have already fired to this location')
            coor.append(-1)

    except Exception:
        print('Error, Connection Refused')


def get_coor():
    return coor


if __name__ == '__main__':
    fire(sys.argv[3], sys.argv[4], sys.argv[1], sys.argv[2])

