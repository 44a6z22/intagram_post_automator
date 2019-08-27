#!/usr/local/bin/python
from Tkinter import * 

from PIL import ImageTk, Image
import json
import time



class Menus(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=0)
        self.setMenu()

    def setMenu(self): 
        # how to make a sub menu layout
        # menu = Menu(self.master)
        # self.master.config(menu=menu)
        # subMenu = Menu(menu)
        # menu.add_cascade(label="account", menu=subMenu)
        # subMenu.add_command(label="login", command=self.quit)

        # how to make a simple menu layout
        menu = Menu(self.master)
        self.master.config(menu=menu)
        menu.add_command(label="Quit", command=self.quit)

class loginEntries(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=1, ipady=20, ipadx=20)
        self.createLabels()
        self.createInputs()

    def createLabels(self):
        self.userNameLable = Label(self.master, text="username : ")
        self.passwordLabel = Label(self.master, text="password : ")
        self.pathLabel = Label(self.master, text="folder's path : ")

        self.userNameLable.grid(row=0, sticky=E, ipadx= 20)
        self.passwordLabel.grid(row=1, sticky=E, ipadx=20)
        self.pathLabel.grid(row=3, sticky=E, ipadx=20)

    def createInputs(self):
        self.userNameEntry = Entry(self.master)
        self.passwordEntry = Entry(self.master)
        self.pathEntry = Entry(self.master)
        self.userNameEntry.grid(row=0, column=1, ipadx=20)
        self.passwordEntry.grid(row=1, column=1, ipadx=20)
        self.pathEntry.grid(row=3, column=1, ipadx=20)


class loginButtons(Frame): 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=4, columnspan=2, ipady=10, sticky=S)
        self.createButtons()

    def createButtons(self):
        self.quitButton = Button(self, text="Login", command=self.save)
        self.quitButton.grid(row=4, column=0, ipadx=40)
        self.quitButton = Button(self, text="Quit", command=self.quit)
        self.quitButton.grid(row=4, column=1, ipadx=40)

    def save(self): 

        with open("../json_data/dataa.json", 'r') as c:
            cache = json.load(c)

        cache["ok"][0] = "ssssok"

        with open("../json_data/dataa.json", 'w') as c:
            json.dump(cache, c, indent=4)

        label = Label(self.master, text ="Done")
        label.grid(row=4, columnspan=2)


    ########################################
    #     safe the file info interface     #
    ########################################

class ImageFrame(Frame): 
    def __init__(self, master=None, fileName = None):
        Frame.__init__(self, master)
        self.fileName = fileName
        


class FilesInfoFrame(Frame):

    def __init__(self, master=None, fileName=None):
        Frame.__init__(self, master)
        self.fileName = fileName
        self.createEntries()


    def createEntries(self):
        self.fileCaption = Entry(self.master, text="ok this is a caption")
        self.fileTime = Entry(self.master)
        self.fileTags = Entry(self.master)

        self.captionLabel = Label(self.master, text="Caption : ")
        self.timeLabel = Label(self.master, text="Time : ")
        self.tagsLabel = Label(self.master, text="tags : ")

        self.fileCaption.grid(row=1, column=1)
        self.fileTime.grid(row=2, column=1)
        self.fileTags.grid(row=3, column=1)

        self.captionLabel.grid(row=1, column=0, sticky=E)
        self.timeLabel.grid(row=2, column=0, sticky=E)
        self.tagsLabel.grid(row=3, column=0, sticky=E)


class SaveInfoButtons(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=4, columnspan=2)
        self.createButtons()


    def createButtons(self):
        self.saveButton = Button(self, text="Login", command=self.save)
        self.saveButton.grid(row=4, column=0, ipadx=40)
        self.quitButton = Button(self, text="Quit", command=self.quit)
        self.quitButton.grid(row=4, column=1, ipadx=40)

    def save(self): 
        self.doneLabel = Label(self.master, text="Done")
        self.doneLabel.grid(row=5, columnspan=2)

