#!/usr/local/bin/python
from Tkinter import *
from Frames import *


def saveInfoFrom(imageName):
    root = Tk()
    root.title("File information ")
    FilesInfoFrame(root, imageName)
    SaveInfoButtons(root)
    
    root.mainloop()


if __name__ == "__main__":
    saveInfoFrom("lol.jpg")
