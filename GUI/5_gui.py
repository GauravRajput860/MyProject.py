from tkinter import *
def getvals():
            print(f"The value of username is : " , uservalue.get())
            print(f"The value of password is : ", passvalue.get())
root = Tk()
root.title("Entry Form") # for title of the form 
root.geometry("800x400") # height and the weidth  of the window 

# creating a user input box ---------------------------------
user = Label(root, text="Username") # for username entry 
user.grid()  # packing the user name with grid functions 
uservalue = StringVar() # taking the uservalue as an string 
userentry = Entry(root, textvariable=uservalue) #puting the box  in the root window
userentry.grid(row=0, column=1)# setting the position of the userentry 

# creating a password input box --------------------------
password = Label(root, text="Password")# for password entry 
password.grid()# packing the password withh grid functions 
passvalue = StringVar() # taking the passvalue as an string 
passentry = Entry(root, textvariable=passvalue)#puting thr box in the root window 
passentry.grid(row=1, column=1)# setting the position of the passentry  

# creating a submit button ----------------
Button(text="Submit", command=getvals).grid() # making a sumit button for the form 


root.mainloop()
