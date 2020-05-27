<<<<<<< Updated upstream
import os
import threading
import server
import chatroom
import client

=======
import os, threading
import server, chatroom, client, server_class
>>>>>>> Stashed changes

def server_thread():
    # server_class.Server()
    server.run()


def app_thread():
    chatroom.ChatRoom()


if __name__ == "__main__":

    threads = [threading.Thread(target=server_thread),
               # threading.Thread(target=client_thread),
               threading.Thread(target=app_thread)
               # threading.Thread(target=reader_thread)
               ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
