from build_album import AlbumFrame, AddPhoto
from tkinter import *


root = Tk()
root.geometry("+800+200")
default_frame = AlbumFrame(root)
default_frame.grid(column=0, row=0, columnspan=5)
root.mainloop()