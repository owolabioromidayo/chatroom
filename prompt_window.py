import tkinter as tk

"""Collects Client Name"""

class PromptWindow:
    def __init__(self, message, title='Prompt Window'):
        self.message = message
        self.title = title
        
        self.buildui()

    def buildui(self):

            self.root = tk.Tk()
            self.root.title(self.title)
            self.label = tk.Label(self.root, text=self.message)
            self.label.grid(row=0,column=0)
            self.entry = tk.Entry(self.root)
            self.entry.grid(row=1,column=0, padx=0, pady=5)
            self.entry.bind('<Return>', self.on_enter) 
            self.button = tk.Button(self.root, text='Confirm',command=self.on_button_press)
            self.button.grid(row=2,column=0,pady=10)
            self.root.mainloop()


    def on_button_press(self):
        pass
    


    def on_enter(self, event):
        """Runs getcoord method when enter key pressed"""
        self.on_button_press()




if __name__ == "__main__":
    PromptWindow('This is a prompt window', 'Prompt')