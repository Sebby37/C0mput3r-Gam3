import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


# functions
def updateGIF(count) -> None:  
    for i in range(100):  
        imgR = img[count]
        count += 1
        if count == frames:
            count = 0 # reset to first frame
        imgPanel.configure(image=imgR)
    #GUI.after(1000, updateGIF(count)) #error on this line

# create tkinter instance
GUI = tk.Tk()

# set basic properties
GUI.geometry("500x500")
GUI.title("C0mput3r Gam3")

# initilise elements

# render image
currPath = os.path.abspath(os.getcwd())
path = currPath + '\\assets\\mrhousemoving.gif'
print(path)
#img = ImageTk.PhotoImage(Image.open(path + "\\assets\\mrhouse2.png"))

imgPanel = tk.Label(GUI)

imgData = Image.open(path)
# frames = []
# frames.append(ImageTk.PhotoImage(imgData.copy()))
# print(frames)

frames = imgData.n_frames

img = [PhotoImage(file=path,format = f'gif -index {i}') for i in range(frames)]

print("..")
print(img[0])

count = 0

updateGIF(count)

imgPanel.pack(side = "bottom", fill = "both", expand = "yes")

GUI.mainloop()


