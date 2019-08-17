#!/usr/local/bin/python
from Tkinter import * 
import json


class loginButtons(Frame): 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createButtons()

    def createButtons(self):
        self.quitButton = Button(self, text="Save", command=self.save)
        self.quitButton.grid(row=0, column=0, ipadx=50)
        self.quitButton = Button(self, text="Quit", command=self.quit)
        self.quitButton.grid(row=0, column=1, ipadx=50)

    def save(self): 

        with open("../json_data/dataa.json", 'r') as c:
            cache = json.load(c)

        cache["ok"][len(cache["ok"]) -1] = "ssssok"

        with open("../json_data/dataa.json", 'w') as c:
            json.dump(cache, c, indent=4)


class loginEntries(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=0)
        self.createLabels()
        self.createInputs()

    def createLabels(self):
        self.userNameLable = Label(self.master, text="username : ")
        self.passwordLabel = Label(self.master, text="password : ")
        self.userNameLable.grid(row=0, column=0, sticky=E)
        self.passwordLabel.grid(row=1, column=0, sticky=E)

    def createInputs(self): 
        self.userNameEntry = Entry(self.master)
        self.passwordEntry = Entry(self.master)
        self.userNameEntry.grid(row=0, column=1)
        self.passwordEntry.grid(row=1, column=1)


class SaveInfoButtons(Frame): 
    pass


class FilesInfoFrame(Frame): 
    pass