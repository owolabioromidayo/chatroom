import socket, select, errno, sys, threading
import file_handler

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234






# def run(name, reader=False):

#     my_username = name
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((IP,PORT))
#     client_socket.setblocking(False)

#     username = my_username.encode("utf-8")
#     username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
#     client_socket.send(username_header + username)



#     while True:
#         if reader:
#             message= ""
#         else:
#             message = input(f"{my_username} > ")
#         # message = "" use this only for the reader client

#         if message:
#             message = message.encode('utf-8')
#             message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
#             client_socket.send(message_header + message)
        
#         try:
#             while True:
#                 #receive things
#                 username_header = client_socket.recv(HEADER_LENGTH)
#                 if not len(username_header):
#                     print("connection closed by the server")
#                     sys.exit()
#                 username_length = int(username_header.decode("utf-8").strip())
#                 username = client_socket.recv(username_length).decode("utf-8") 

#                 message_header = client_socket.recv(HEADER_LENGTH)
#                 message_length = int(message_header.decode("utf-8").strip())
#                 message = client_socket.recv(message_length).decode("utf-8")

#                 print(f"{username} > {message}")


#         except IOError as e:
#             if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
#                 print('reading error', str(e))
#                 sys.exit()
#             continue



#         except Exception as e:
#             print('General error', str(e))
#             sys.exit()




class Client:
    def __init__(self, name, isReader=False):
        self.name = name
        self.isReader = isReader

    
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((IP,PORT))
        self.socket.setblocking(False)

        username = self.name.encode("utf-8")
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
        self.socket.send(username_header + username)


        threads = [threading.Thread(target=self.receive_thread)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()



    def receive_thread(self):
        try:
            while True:
                #receive things
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
        # while True:
        #     # if self.isReader:
        #     # message= ""
        #     # else:
        #     #     message = input(f"{my_username} > ")
        #     # message = "" use this only for the reader client

        #     if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        self.socket.send(message_header + message)

