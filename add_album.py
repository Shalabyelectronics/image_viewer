from tkinter import *
from tkinter import ttk

# ----Color  and Fonts --------#
FONT = "Coiny"
BACKGROUND_COLOR = "#20574f"
FOREGROUND = "#62d9c7"


class Add_album:
    def __init__(self, album_name, photos_list):
        self.album_name = album_name
        self.photos_list = photos_list
        self.img_objects_list = []
        self.add_photos_list()
        self.index_count = 0
        self.status_number = 1
        self.forward_img = PhotoImage(file="img/app_img/fast-forwardr.png")
        self.backward_img = PhotoImage(file="img/app_img/fast-backwardr.png")
        self.exit_img = PhotoImage(file="img/app_img/exitr.png")
        self.view_image = None
        self.status_bar = None
        self.canvas = None

    def add_photos_list(self):
        if type(self.photos_list) == list:
            self.img_objects_list = [PhotoImage(file=img) for img in self.photos_list]
        else:
            print("only list type accepted")

    def create_album_frame(self, frame, background_color):
        self.canvas = Canvas(frame, width=600, height=350, bg=background_color, highlightthickness=0)
        self.view_image = self.canvas.create_image(300, 175, image=self.img_objects_list[self.index_count])
        forward_b = Button(frame, image=self.forward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                           border=0, command=self.forward)
        backward_b = Button(frame, image=self.backward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                            border=0, command=self.backward)
        exit_b = Button(frame, image=self.exit_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0)
        self.status_bar = Label(frame, text=f"Image 1 of {len(self.img_objects_list)}", bd=2, relief=SUNKEN,
                                bg=BACKGROUND_COLOR, fg=FOREGROUND,
                                font=(FONT, 15), pady=5)
        self.status_bar.grid(column=0, row=2, columnspan=3, sticky=W + E)
        exit_b.grid(column=1, row=1)
        backward_b.grid(column=0, row=1, pady=10, sticky=E)
        forward_b.grid(column=2, row=1, pady=10, sticky=W)
        self.canvas.grid(column=0, row=0, columnspan=3, padx=30, pady=15)

    def forward(self):
        self.index_count += 1
        self.status_number += 1
        if self.index_count < len(self.img_objects_list):
            self.status_bar.config(text=f"Image {self.status_number} of {len(self.img_objects_list)}")
            self.canvas.itemconfig(self.view_image, image=self.img_objects_list[self.index_count])
        else:
            self.index_count = 6
            self.status_number = 7

    def backward(self):
        self.index_count -= 1
        self.status_number -= 1
        if self.index_count < 0:
            self.index_count = 0
            self.status_number = 1
        else:
            self.status_bar.config(text=f"Image {self.status_number} of {len(self.img_objects_list)}")
            self.canvas.itemconfig(self.view_image, image=self.img_objects_list[self.index_count])
