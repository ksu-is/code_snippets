from tkinter import *

root = Tk()

def callback(event):
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=400, height=400)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
