#!/usr/local/bin/python
from Tkinter import *
from Frames import *


if __name__ == "__main__":
    
    root = Tk()
    root.title("InstaPy Login GUI")

    
    menu = Menus(root)
    inputs = loginEntries(root)
    loginButtons = loginButtons(root)

    root.mainloop()
