import tkinter as tk
import tkinter.messagebox as messagebox

"""Collects Client Name"""


class PromptWindow:
    def __init__(self, parent, message, title='Prompt Window'):
        self.message, self.title, self.parent = message, title, parent
        self.build()

    def build(self):
        self.root = tk.Tk()
        self.root.title(self.title)

        self.label = tk.Label(self.root, text=self.message)
        self.label.grid(row=0, column=0)

        self.entry = tk.Entry(self.root)
        self.entry.grid(row=1, column=0, padx=0, pady=5)
        self.entry.bind('<Return>', lambda e: self.on_button_press())

        self.button = tk.Button(
            self.root, text='Confirm', command=self.on_button_press
        )
        self.button.grid(row=2, column=0, pady=10)

        self.root.mainloop()

    def on_button_press(self):
        user_input = self.entry.get()
        if user_input != "":
            self.parent.username = user_input
            self.root.destroy()
        else:
            messagebox.showerror(
                title="Input Error", message="Username cannot be null"
            )


if __name__ == "__main__":
    PromptWindow('This is a prompt window', 'Prompt')
