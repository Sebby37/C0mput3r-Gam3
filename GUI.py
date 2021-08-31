import os
import tkinter as tk
from tkinter import Canvas, PhotoImage
from tkinter.constants import NW
from tkinter import *
from PIL import ImageTk, Image


# get path
currPath = os.getcwd()

if os.name == "nt":
    file: str = currPath + "\\assets\\mrhouse2.png" # put image here
else:
    file: str = currPath + "/assets"


class GUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # edit root window properties
        self.title("c0mput3er")
        self.geometry("500x500")

        # initilise components
        self.canvas = Canvas(self, width=500, height=500) # set to window dimensions

    def renderComponents(self):
        self.img = ImageTk.PhotoImage(Image.open(file))
        self.canvas.create_image(0,0, image=self.img, anchor=NW)

    def drawComponents(self):
        self.canvas.pack()

    def start(self):
        self.mainloop()
        #print("hi")


if __name__ == "__main__":
    App = GUI()
    App.renderComponents()
    App.drawComponents()
    App.start()



