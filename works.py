"""A4 inclass Python 
Name: Jinfeng He(komi) student ID: 991775848
"""

#import statements to build GUI
import random
from tkinter import *
from tkinter import messagebox

#create a GUI app to change the background color of the window

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

        #10 colors

        self.colorList = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black"]

        self.colorVar = StringVar()
        self.createWidgets()

    def createWidgets(self):
        #Label 

        self.inputLabel = Label(self, text="Input color",bg ="black", fg="white", width=15 )
        self.inputLabel.grid(row=0, column=0)

        #Entry
        self.inputEntry = Entry(self, textvariable=self.colorVar, width=15)
        self.inputEntry.grid(row=0, column=1)

        #button for input color
        self.inputButton = Button(self, text="Input", command=self.changeInputColor)
        self.inputButton.grid(row=0, column=2)
        
        #button for black
        self.blackButton = Button(self, text="Black", width=15, command=self.changeBlack)
        self.blackButton.grid(row=1, column=0)

        #button for blue
        self.blueButton = Button(self, text="Blue", width=15, command=self.changeBlue)
        self.blueButton.grid(row=1, column=1)

        #button for random color
        self.randomButton = Button(self, text="Random Color", width=15, command=self.changeRandom)
        self.randomButton.grid(row=1, column=2)

        #Input color options,for user reference
        self.optionsLabel = Label(self, text="Color options:red, orange, yellow, green, blue, purple, pink", width=45)
        self.optionsLabel.grid(row=3, column=0, columnspan=3)

        self.optionsLabel = Label(self, text=" brown, gray, black", width=35)
        self.optionsLabel.grid(row=4, column=0, columnspan=3)

        #exit button
        self.exitButton = Button(self, text="Exit", width=15, command=root.destroy)
        self.exitButton.grid(row=2, column=1)
    
    def changeInputColor(self):
        colorName = self.colorVar.get()

        if colorName in self.colorList:
            root["bg"] = colorName
            self["bg"] = colorName
        
        else:
            messagebox.showinfo(title="invalid color", message="Please input a valid color name")
    
    def changeBlack(self):
        root["bg"] = "black"
        self["bg"] = "black"
    
    def changeBlue(self):
        root["bg"] = "blue"
        self["bg"] = "blue"
    
    def changeRandom(self):
        colorName = random.choice(self.colorList)
        root["bg"] = colorName
        self["bg"] = colorName
    
root = Tk()
app = Application(master=root)
root.title("Color App ")
root.geometry("350x100")
app.mainloop()
