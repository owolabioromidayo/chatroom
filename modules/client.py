import socket
import select
import errno
import sys
import utils.file_handler as file_handler
from utils.threading_helper import multithread, singlethread

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234


class Client:
    def __init__(self, name):
        self.name = name
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((IP, PORT))
        self.socket.setblocking(False)

        username = self.name.encode("utf-8")
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
        self.socket.send(username_header + username)

        singlethread(self.receive_thread)

    def receive_thread(self):
        try:
            while True:
                # receive things
                username_header = self.socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    print("Connection Closed by the Server")
                    sys.exit()
                username_length = int(username_header.decode("utf-8").strip())
                username = self.socket.recv(username_length).decode("utf-8")

                message_header = self.socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode("utf-8").strip())
                message = self.socket.recv(message_length).decode("utf-8")

                print(f"{username} > {message}")

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('reading error', str(e))
                sys.exit()

        except Exception as e:
            print('General error', str(e))
            sys.exit()

    def send_thread(self, message=None):
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        self.socket.send(message_header + message)
