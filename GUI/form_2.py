from tkinter import *
from PIL import Image, ImageTk

def new_window():
    username = e1.get()
    password = e2.get()

    if not username.strip() or not password.strip():
        # If either the username or password is empty, show an error message
        error_label.config(text="Username and Password are required * ", fg="red")
    else:
        # Both fields have valid inputs, proceed with the login
        error_label.config(text="")
        root.withdraw()
        new_window = Toplevel(root)
        new_window.minsize(500, 400)
        new_window.maxsize(500, 400)
        label = Label(new_window, text="Log In successful...", font="comicsansms 13 italic")
        label.pack(padx=20, pady=20)
        image = Image.open("logo.png")
        global photo  # Keep a reference to the image object
        photo = ImageTk.PhotoImage(image)
        label = Label(new_window, image=photo)
        label.image = photo  # Keep a reference to the image
        label.pack()
       

root = Tk()
root.title("Entry Form ")
root.minsize(500, 500)
root.maxsize(500, 500)

image = Image.open("logo.png")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo, padx=20, pady=20)
label.image = photo
label.place(x=130, y=30)

l = Label(root, text="Log In", font="comicsansms 20 bold").place(x=195, y=230)

l2 = Label(root, text="Username : ", font="comicsansms 10 bold").place(x=140, y=280)
e1 = StringVar()
entry_username = Entry(root, textvariable=e1)
entry_username.place(x=225, y=280)

l3 = Label(root, text="Password : ", font="comicsansms 10 bold").place(x=140, y=310)
e2 = StringVar()
entry_password = Entry(root, textvariable=e2)
entry_password.place(x=225, y=310)

error_label = Label(root, text="", fg="red")
error_label.place(x=140, y=350)

Button(text="Log In", command=new_window, pady=2, padx=30).place(x=225, y=380)

root.mainloop()
