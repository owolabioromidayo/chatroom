def send(msg):
    with open('messages.txt', 'a') as f:
        f.write("\n" + msg.strip())


def read():
    with open('messages.txt', 'r') as f:
        return f.readlines()
