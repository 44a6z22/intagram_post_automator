#!/usr/local/bin/python 
from Tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master) 
        self.grid() 
        self.createWidgets()


    def createWidgets(self):
        self.quitButton = Button(self, text="Quit",
            command = self.quit) 
        self.quitButton.grid()






if __name__ == "__main__":
    app = Application() 
    app.master.title("that the window title.") 
    app.mainloop()

