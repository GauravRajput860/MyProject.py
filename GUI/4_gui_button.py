from tkinter import *

root = Tk()
root.title("Button")
root.geometry("1000x400")
f = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f.pack(side=LEFT, fill=Y, pady=1)
f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill=X, padx=0)
l2 = Label(
    f2,
    text="Welcome In VS Code",
    fg="black",
    font="Helvetica 12 bold ",
    padx=5,
    pady=5,
)
l2.pack()
btn = Button(
    f2,
    background="red",
    fg="white",
    text="Quit",
)
btn.place(x=880,y=5)


l = Label(f, text="Menu", fg="black", font="Helvetica 12 bold ", padx=2, pady=2)
l.pack(anchor="e")

fram = Frame(root, borderwidth=2, relief=SUNKEN)
fram.pack(
    side=BOTTOM,
    fill=X,
)
b1 = Button(fram, background="grey", fg="black", text="Ok")
b1.pack(padx=90, pady=5, side=LEFT)
b2 = Button(fram, background="grey", fg="black", text="Wait")
b2.pack(padx=90, pady=5, side=LEFT)
b3 = Button(fram, background="grey", fg="black", text="Cancel")
b3.pack(padx=90, pady=5, side=LEFT)
b4 = Button(fram, background="grey", fg="black", text="Back ")
b4.pack(padx=90, pady=5, side=LEFT)


root.mainloop()
