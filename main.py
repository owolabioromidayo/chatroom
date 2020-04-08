import os, threading
import server, chatroom, client

def server_thread():
    server.run()


def app_thread():
    chatroom.ChatRoom()


# def reader_thread():
#     client.run('Anonymous', reader=True)


def client_thread():
    name = input('Name: ')
    client.run(name)




if __name__ == "__main__":

    threads = [threading.Thread(target=server_thread),
                threading.Thread(target=client_thread),
                threading.Thread(target=app_thread)
                # threading.Thread(target=reader_thread)
                ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()