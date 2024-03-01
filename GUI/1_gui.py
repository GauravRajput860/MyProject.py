from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("My File")
# Load the image file using Pillow
image_path = "mypic.png"
image = Image.open(image_path)
h = 800
v = 600
size = image.resize((h, v))
photo = ImageTk.PhotoImage(image)

# Create a label widget to display the image
label = Label(root, image=photo)

# Keep a reference to the image to prevent it from being garbage collected
label.image = photo

# Pack the label into the Tkinter window
label.pack()

root.mainloop()
