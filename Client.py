import http.client
import sys



def fire():
    global R1
    try:
        connection = http.client.HTTPConnection(IP + ':' + PORT)
        connection.request("GET", "/x=" + X + "&y=" + Y)
        R1 = connection.getresponse()

    except Exception:
        print('Error, Connection Refused')


def get_response():
    global R1
    result = R1.read()
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
    fire()

