#!/usr/local/bin/python
from Tkinter import *
from Frames import *


if __name__ == "__main__":
    
    root = Tk()

    inputs = loginEntries(root)
    loginButtons = loginButtons(root)

    root.mainloop()
