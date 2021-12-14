from tkinter import *


class MainWindow(Tk):
    Run = True

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title("Word beans")
        self.Words = Text(self)
        self.Words.grid(row=0, column=0)
        self.Word = Entry(self)
        self.Word.grid(row=1, column=0)

    def run(self):
        try:
            while self.Run:
                self.update()
        except:
            pass
