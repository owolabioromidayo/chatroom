import client, server, file_handler
import tkinter as tk
import time, threading



class ChatRoom:
    rooms = []
    def __init__(self):
        room = threading.Thread(target=self.handle_chatroom)
        ChatRoom.rooms.append(room)
        room.start()
        # for room in ChatRoom.rooms:
        #     room.join()
    

        



    def handle_chatroom(self):
        self.username = input('Name:  ')
        self.prev_msg = ''
        self.x = 200
        self.y = 0
        self.client = client.Client(self.username)


        threads = [threading.Thread(target=self.build), threading.Thread(target=self.listen)]
        for thread in threads:
            thread.start()
            time.sleep(0.02)
        for thread in threads:
            thread.join()



    
        


    def build(self):
        self.root = tk.Tk()
        self.root.title("Sock Servc")
        self.root.bind('<Return>', self.handle_click)

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()


        self.label = tk.Label(self.root, text=self.username)
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text='Send', command=self.handle_click)
        self.button.pack()

        self.new_instance = tk.Button(self.root, text='New window', command= self.create_new_instance)
        self.new_instance.pack()
        

        self.root.mainloop()

        # self.loadall()
        # while True:
        #     messages = file_handler.read()
        #     for line in messages:
        #         self.canvas.create_text(0,0, text=line)


        # while True:
        #     self.listen()
        #     time.sleep(2)


    def handle_click(self, event=None):
        msg = self.entry.get()
        self.entry.delete(0, tk.END)
        self.client.send_thread(msg)


    def create_new_instance(self):
        thread = threading.Thread(target=ChatRoom)
        thread.start()
        thread.join()
            
            

    def listen2(self):
        while True:
            messages = file_handler.read()
            for line in messages:
                self.canvas.create_text(self.x, self.y,text=line)
                self.y += 30

        


    def loadall(self):
        print(file_handler.read())
        for line in file_handler.read():
            self.canvas.create_text(text=line)


    def listen(self):
        while True:
            msg = file_handler.read()[-1]
            if msg != self.prev_msg:
                self.canvas.create_text(self.x, self.y, text=msg)
                self.y += 30
                self.prev_msg = msg


