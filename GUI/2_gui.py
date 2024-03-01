from tkinter import *

root = Tk()
root.geometry("350x200")
root.title("My GUI")
test = Label(
    text="Python3 installed Successfuly...",
    bg="lightblue",
    fg="black",
    padx=10,
    pady=10,
    font=("comicsansms", 12, "italic"),
    borderwidth=10,
)
test.pack(side=LEFT, fill=Y, padx=30, pady=30)

root.mainloop()
