import modules.server as server
import modules.chatroom as chatroom
from utils.threading_helper import multithread

if __name__ == "__main__":
    multithread([lambda: server.Server(), lambda: chatroom.ChatRoom()])
