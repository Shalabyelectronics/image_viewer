from tkinter import *

# ----Color  and Fonts --------#
FONT = "Coiny"
BACKGROUND_COLOR = "#20574f"
FOREGROUND = "#62d9c7"


class Add_album:
    def __init__(self, root, album_name, photos_list):
        self.album_name = album_name
        self.photos_list = photos_list
        self.img_objects_list = []
        self.add_photos_list()
        self.index_count = 0
        self.status_number = 1
        self.forward_img = PhotoImage(file="img/app_img/fast-forwardr.png")
        self.backward_img = PhotoImage(file="img/app_img/fast-backwardr.png")
        self.exit_img = PhotoImage(file="img/app_img/exitr.png")
        self.auto_img = PhotoImage(file="img/app_img/auto_play.png")
        self.add_img = PhotoImage(file="img/app_img/plus.png")
        self.exit_sub_w_img = PhotoImage(file="img/app_img/exit_w.png")
        self.save_album_img = PhotoImage(file="img/app_img/save.png")
        self.view_image = None
        self.status_bar = None
        self.canvas = None
        self.add_album_window = None
        self.root = root

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
        exit_b = Button(frame, image=self.exit_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
                        command=self.root.quit)
        self.status_bar = Label(frame, text=f"Image 1 of {len(self.img_objects_list)}", bd=2, relief=SUNKEN,
                                bg=BACKGROUND_COLOR, fg=FOREGROUND,
                                font=(FONT, 15), pady=5)
        auto_b = Button(frame, image=self.auto_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0)
        add_b = Button(frame, image=self.add_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
                       command=self.open_add_album)
        auto_b.grid(column=1, row=1, sticky=E)
        add_b.grid(column=3, row=1, sticky=W)
        self.canvas.grid(column=0, row=0, columnspan=5, padx=30, pady=15)
        backward_b.grid(column=0, row=1, pady=10, sticky=E)
        forward_b.grid(column=4, row=1, pady=10, sticky=W)
        exit_b.grid(column=2, row=1)
        self.status_bar.grid(column=0, row=2, columnspan=5, sticky=W + E)

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

    def open_add_album(self):
        self.add_album_window = Toplevel(bg=BACKGROUND_COLOR, bd=5, relief="groove")
        self.add_album_window.geometry("+800+300")
        self.add_album_window.minsize(width=300, height=300)
        self.add_album_window.resizable(False, False)
        self.add_album_window.iconbitmap("img/app_img/my.ico")
        self.add_album_window.title("Add a new album")
        main_label = Label(self.add_album_window, text="Here you can add a new album.", font=(FONT, 15),
                           bg=BACKGROUND_COLOR, fg="white")
        album_name_l = Label(self.add_album_window, text="Album name   :", font=(FONT, 12), bg=BACKGROUND_COLOR,
                             fg="white")
        album_folder_l = Label(self.add_album_window, text="Album folder :", font=(FONT, 12), bg=BACKGROUND_COLOR,
                               fg="white")
        exit_sub_w_b = Button(self.add_album_window, image=self.exit_sub_w_img, bg=BACKGROUND_COLOR,
                              activebackground=BACKGROUND_COLOR, border=0, command=self.add_album_window.destroy)
        save_album_b = Button(self.add_album_window, image=self.save_album_img, bg=BACKGROUND_COLOR,
                              activebackground=BACKGROUND_COLOR, border=0)

        main_label.grid(column=0, row=0, columnspan=3, pady=10)
        album_name_l.grid(column=0, row=1, pady=10, padx=5, sticky=W)
        album_folder_l.grid(column=0, row=2, pady=10, padx=5, sticky=W)
        exit_sub_w_b.grid(column=2, row=3, pady=20)
        save_album_b.grid(column=0, row=3, pady=20)
