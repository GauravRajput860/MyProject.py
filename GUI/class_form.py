from tkinter import *


def getvals():
    print(f"The name is  : ", namevalue.get())
    print(f"The fatherrname is : ", fnamevalue.get())
    print(f"Age is : ", agevalue.get())
    print(f"Gender is : ", gendervalue.get())
    with open("record.txt", "a") as f:
        f.write(
            f"{namevalue.get(),fnamevalue.get(),agevalue.get(),gendervalue.get()}\n"
        )


root = Tk()
root.title("Entry Form")
root.geometry("700x400")
Label(
    root,
    text="Enter your deatils to join our page. ",
    font="comicsansms 13 bold ",
    pady=10,
    padx=0,
).grid(row=0, column=3)
# creating a name  input box ---------------------------------
name = Label(root, text=" Name : ", pady=10, padx=20)
name.grid()
namevalue = StringVar()
nameentry = Entry(root, textvariable=namevalue)
nameentry.grid(row=1, column=1)

# creating a father  name input box --------------------------
fname = Label(root, text="Father name : ", pady=10, padx=20)
fname.grid()
fnamevalue = StringVar()
fnameentry = Entry(root, textvariable=fnamevalue)
fnameentry.grid(row=2, column=1)
# creating a age  input box --------------------------
age = Label(root, text="Age : ", pady=10, padx=20)
age.grid()
agevalue = IntVar()
ageentry = Entry(root, textvariable=agevalue)
ageentry.grid(row=3, column=1)
# creating a gender  input box --------------------------
gender = Label(root, text="Gender : ", pady=10, padx=20)
gender.grid()
gendervalue = StringVar()
genderentry = Entry(root, textvariable=gendervalue)
genderentry.grid(row=4, column=1)

# check box for our form
foodservice = IntVar()
food = Checkbutton(text=" I agree with term and conditions. ", variable=foodservice)
food.grid(row=5, column=1, padx=10, pady=10)
# button to submit
Button(text="Send", command=getvals, pady=2, padx=30).grid()


root.mainloop()
