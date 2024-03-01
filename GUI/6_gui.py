from tkinter import * 
root = Tk()
can_width=400
can_height=500
root.geometry(f"{can_width}x{can_height}")
root.title("My GUi")
can_widget=Canvas(root, width=can_width, height=can_height)
can_widget.pack()
# can_widget.create_line(0,0,400,200, fill="red")
# can_widget.create_rectangle(3,5,700,300,fill="blue")
# can_widget.create_text(200,200,text="Gaurav Rajput ")
can_widget.create_oval(3,5,400,300,fill="grey")
root.mainloop()