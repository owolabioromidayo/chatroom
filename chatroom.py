import client, server, file_handler
import tkinter as tk
import time, threading

class ChatRoom:
    def __init__(self):
        # self.username = input('Name:  ')
        self.prev_msg = ''
        self.x = 200
        self.y = 0

        
        # self.build()

        threads = [threading.Thread(target=self.build), threading.Thread(target=self.listen)]
        for thread in threads:
            thread.start()
            time.sleep(0.02)
        for thread in threads:
            thread.join()


    
    def build(self):
        self.root = tk.Tk()
        self.root.title("Sock Servc")

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        

        self.root.mainloop()

        # self.loadall()
        # while True:
        #     messages = file_handler.read()
        #     for line in messages:
        #         self.canvas.create_text(0,0, text=line)


        # while True:
        #     self.listen()
        #     time.sleep(2)
            

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


