import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# Wrapping the GIF Image in a class, many variables could be removed as this was just a direct translation of some previous code to a class
class GifImage(tk.Label):
    def __init__(self, master, path):
        super().__init__(master)
        self.image_data = Image.open(path)
        self.frames = self.image_data.n_frames
        self.img = [PhotoImage(file = path, format = f'gif -index {i}') for i in range(self.frames)]
        self.count = 0
        self._updateGIF()
    def _updateGIF(self):
        imgR = self.img[self.count]
        self.count += 1
        if self.count == self.frames:
            self.count = 0
        self.configure(image=imgR)
        self.master.after(round(1000 / self.frames), self._updateGIF) # This gif refresh rate solution needs to be better, perhaps use https://stackoverflow.com/a/53365469/14128844

# Create tkinter instance
GUI = tk.Tk()
GUI.geometry("500x500")
GUI.title("C0mput3r Gam3")

# Image
imag = GifImage(GUI, "assets\\mrhousemoving.gif")
imag.pack(side = "bottom", fill = "both", expand = "yes")

# Running the tkinter instance
GUI.mainloop()
