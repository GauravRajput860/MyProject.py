from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("455x244")
# photo=PhotoImage(file="mypic.png")
img = Image.open("mypic.png")
photo = ImageTk.PhotoImage(img)
lbl = Label(image=photo)
lbl.pack()
root.mainloop()
