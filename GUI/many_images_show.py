import tkinter as tk
from PIL import Image, ImageTk
import os  # the main work of the os library in this code is to facilitate the listing of files in a directory and filtering those files based on their extensions. This helps in obtaining a list of relevant image files from the specified directory for further processing and display in the Tkinter GUI.

img_dir = "mydir"
img_files = [
    each_file
    for each_file in os.listdir(img_dir)
    if each_file.endswith((".png", ".png", ".png"))
]

root = tk.Tk()
root.title("Image Viewer")

for img_file in img_files:
    img_path = os.path.join(img_dir, img_file)
    img = Image.open(img_path)
    img = img.resize((200, 300))
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

root.mainloop()
