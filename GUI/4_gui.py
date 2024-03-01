from tkinter import *

root = Tk()
root.geometry("850x233")
root.title("VS Code")
f = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f.pack(side=LEFT, fill=Y, pady=1)
f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill=X, padx=0)
l2 = Label(
    f2,
    text="Welcome In VS Code",
    bg="navy",
    fg="white",
    font="Helvetica 12 bold ",
    padx=5,
    pady=5,
)
l = Label(
    f, text="Menu", bg="navy", fg="white", font="Helvetica 12 bold ", padx=5, pady=5
)

l.pack()
l2.pack()

root.mainloop()
