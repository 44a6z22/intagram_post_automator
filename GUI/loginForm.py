#!/usr/local/bin/python
from Tkinter import *
from Frames import *

def loginPage():
    root = Tk()
    root.title("InstaPy Login GUI")
    
    Menus(root)
    loginEntries(root)
    loginButtons(root)  
    
    root.mainloop()



if __name__ == "__main__":
    
    

    
    loginPage()
