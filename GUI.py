import os
import tkinter as tk
from tkinter import Canvas, PhotoImage
from tkinter.constants import NW
from tkinter import *
from PIL import ImageTk, Image


# get path
currPath: str = os.getcwd()

if os.name == "nt":
    file: str = currPath + "\\assets\\mantest.png" # put image here
else:
    file: str = currPath + "/assets/mantest.png"


class GUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # edit root window properties
        self.title("c0mput3er")
        self.geometry("500x500")

        # initilise components
        self.canvas = Canvas(self, width=500, height=500) # set to window dimensions

    def _rendercomponents(self) -> None:
        self.img = ImageTk.PhotoImage(Image.open(file))
        #self.imgR = self.img.resize((400, 400), Image.ANTIALIAS)
        self.canvas.create_image(0,0, image=self.img, anchor=NW)

    def _drawcomponents(self) -> None:
        self.canvas.pack()

    def _start(self) -> None:
        self.mainloop()
        #print("hi")


if __name__ == "__main__":
    App = GUI()
    App._rendercomponents()
    App._drawcomponents()
    App._start()



