import socket

IP = 'localhost'
PORT = 80
BUFFER_SIZE = 1024

class Server:
    def __init__(self, remote_ip, remote_port):
        self.connected = False
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        # self.local_ip = local_ip
        # self.local_port = local_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open_connection(self):
        print("[*] Waiting for Client Connection")
        self.socket.bind((self.remote_ip, self.remote_port))
        self.socket.listen(1)

        while self.connected == False:
            try:
                self.addr = self.socket.accept()
                print("[*] Connected to Client at " + str(self.addr))
                self.connected = True

            except ConnectionRefusedError:
                pass


    def send_message(self, message):
        if self.connected:
            self.socket.send(message)

    def receive(self, buffer_size):
        return self.addr.recv(buffer_size)

    def close_connection(self):
       self.socket.close()
       self.connected = False


def handle_connection(Server):
    print("Client: " + Server.receive(BUFFER_SIZE))

    message = ""
    while message != "quit":
        message = input(">> ")
        Server.send_message(message)
        Server.receive(BUFFER_SIZE)


if __name__ == '__main__':
    connection = Server(IP, PORT)
    connection.open_connection()
    handle_connection(connection)

