import socket, os

IP = 'localhost'
PORT = 80
BUFFER_SIZE = 1024

class Client:
    def __init__(self, remote_ip, remote_port):
        self.connected = False
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        # self.local_ip = local_ip
        # self.local_port = local_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open_connection(self):
        print("[*] Waiting for Server Connection")

        while not self.connected:
            try:
                self.socket.connect((self.remote_ip, self.remote_port))
                print("[*] Server Connection Established")
                self.connected = True

            except ConnectionRefusedError:
                pass

    def send_message(self, message):
        if self.connected:
            self.socket.send(message)

    def receive(self, buffer_size):
        return self.socket.recv(buffer_size)

    def close_connection(self):
       self.socket.close()
       self.connected = False

    def verify_connection(self):
        return self.connected


def handle_connecion(Client):
    Client.send_message("Client Test Message")
    message = ""
    while message != "quit":
        message = input(">> ")
        Client.send_message(message)
        Client.receive(BUFFER_SIZE)


if __name__ == '__main__':
    connection = Client(IP, PORT)
    connection.open_connection()
    handle_connecion(connection)


