import requests


def fire(x, y):
    payload = {'x': x, 'y': y}
    res = requests.post('localhost', data=payload)
    print(res.text)


