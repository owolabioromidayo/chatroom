import time
import tkinter as tk
import modules.client as client
import modules.prompt_window as prompt_window
import utils.file_handler as file_handler
from utils.threading_helper import multithread, singlethread


class ChatRoom:

    def __init__(self):
        singlethread(self.handle_chatroom)

    def handle_chatroom(self):
        self.x, self.y = 50, 20
        self.username = ''
        self.prev_msg = ''

        prompt_window.PromptWindow(self, 'Input Username to Proceed:')
        self.client = client.Client(self.username)
        multithread([self.build, self.listen], 0.02)

    def build(self):
        self.root = tk.Tk()
        self.root.title("Chatroom")
        self.root.bind('<Return>', self.handle_click)
        self.root.resizable(width=False, height=False)

        # CANVAS AND SCROLLBAR
        self.canvas_frame = tk.Frame(self.root, width=800, height=600)
        self.canvas_frame.pack(expand=True, fill=tk.BOTH)

        self.canvas = tk.Canvas(
            self.canvas_frame, width=800, height=600, bg="#FFFFFF", scrollregion=(0, 0, 800, 2000)
        )

        self.canvas_scrollbar = tk.Scrollbar(
            self.canvas_frame, orient=tk.VERTICAL)
        self.canvas_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_scrollbar.config(command=self.canvas.yview)

        self.canvas.pack(expand=True, fill=tk.BOTH)

        self.bottom_frame = tk.Frame(self.root, width=800, height=200)

        self.label = tk.Label(self.bottom_frame, text=self.username)
        self.label.pack()

        self.entry = tk.Entry(self.bottom_frame, width=50)
        self.entry.pack()

        self.send_btn = tk.Button(
            self.bottom_frame, text='Send', command=self.handle_click
        )
        self.send_btn.pack(pady=5)

        self.new_instance_btn = tk.Button(
            self.bottom_frame, text='New window', command=lambda: singlethread(ChatRoom)
        )
        self.new_instance_btn.pack(pady=5)

        self.bottom_frame.pack()

        self.root.mainloop()

    def handle_click(self, event=None):
        msg = self.entry.get()
        self.entry.delete(0, tk.END)
        self.client.send_thread(msg)

    def listen(self):
        while True:
            msg = file_handler.read()[-1]
            if msg != self.prev_msg:
                self.canvas.create_text(self.x, self.y, text=msg, anchor=tk.W)
                self.y += 30
                self.prev_msg = msg

    def _listen2(self):
        """Less efficient, loads all messages before instance creation"""
        while True:
            messages = file_handler.read()
            for line in messages:
                self.canvas.create_text(self.x, self.y, text=line)
                self.y += 30

    def _loadall(self):
        """Loads text file into chatroom"""
        print(file_handler.read())
        for line in file_handler.read():
            self.canvas.create_text(text=line)
