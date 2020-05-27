import socket
import select
import utils.file_handler as file_handler


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234


class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # To reuse same port on restart
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((IP, PORT))

        self.socket.listen()

        self.sockets_list = [self.socket]

        self.clients = {}

        self.run()

    def receive_message(self, client_socket):
        try:
            message_header = client_socket.recv(HEADER_LENGTH)

            if not len(message_header):
                return False

            message_length = int(message_header.decode('utf-8').strip())
            return {"header": message_header, "data": client_socket.recv(message_length)}

        except:
            return False

    def run(self):
        while True:
            read_sockets, _, exception_sockets = select.select(
                self.sockets_list, [], self.sockets_list)
            for notified_socket in read_sockets:
                if notified_socket == self.socket:
                    client_socket, client_address = self.socket.accept()

                    user = self.receive_message(client_socket)
                    if user is False:
                        continue

                    self.sockets_list.append(client_socket)
                    self.clients[client_socket] = user

                    file_handler.send(
                        f"{user['data'].decode('utf-8')} [{client_address[0]}:{client_address[1]}] joined the server!")

                else:
                    message = self.receive_message(notified_socket)

                    if message is False:
                        print(
                            f"{self.clients[notified_socket]['data'].decode('utf-8')} left the server.")
                        self.sockets_list.remove(notified_socket)
                        del self.clients[notified_socket]
                        continue

                    user = self.clients[notified_socket]
                    file_handler.send(
                        f"{user['data'].decode('utf-8')} > {message['data'].decode('utf-8')}  ")

                    for client_socket in self.clients:
                        if client_socket != notified_socket:
                            client_socket.send(
                                user['header'] + user['data'] + message['header'] + message['data'])

            for notified_socket in exception_sockets:
                self.sockets_list.remove(notified_socket)
                del self.clients[notified_socket]


if __name__ == "__main__":
    Server()
