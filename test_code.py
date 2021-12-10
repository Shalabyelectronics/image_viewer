import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# ------Constants
FONT = "Coiny"
BACKGROUND_COLOR = "#20574f"
ACTIVE_BACKGROUND = "#b7ffef"
FOREGROUND = "#62d9c7"


# -----Photo Album Class inherited from Tk class
class PhotoAlbum(Tk):
    def __init__(self):
        super().__init__()
        self.tab = None
        self.image_path = None
        self.numbers_of_images = None
        self.select_img_b = None
        self.album_name_e = None
        self.save_album_b = None
        self.exit_sub_w_b = None
        self.select_img_l = None
        self.album_name_l = None
        self.main_label = None
        self.add_window = None
        self.current_dir = None
        self.title("Image Viewer")
        self.geometry("+600+200")
        self.resizable(False, False)
        self.iconbitmap("img/app_img/my.ico")
        self.config(bg=BACKGROUND_COLOR, bd=5, relief="ridge")
        self.canvas = Canvas(self, width=600, height=350, bg="white", highlightthickness=0)
        self.photos_list = []
        self.saved_photos_list = []
        # -----------Counters ------------------#
        self.index_count = 0
        self.status_number = 1
        # -----------Widgets photos ------------#
        self.forward_img = PhotoImage(file="img/app_img/fast-forwardr.png")
        self.backward_img = PhotoImage(file="img/app_img/fast-backwardr.png")
        self.exit_img = PhotoImage(file="img/app_img/exitr.png")
        self.auto_img = PhotoImage(file="img/app_img/auto_play.png")
        self.add_img = PhotoImage(file="img/app_img/plus.png")
        self.default_image = PhotoImage(file="img/app_img/defualt_img.png")
        self.exit_sub_w_img = PhotoImage(file="img/app_img/exit_w.png")
        self.save_album_img = PhotoImage(file="img/app_img/save.png")
        # ----------Set widgets ------------
        self.view_image = self.canvas.create_image(300, 175, image=self.default_image)
        self.next_b = Button(self, image=self.forward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                             border=0, command=self.go_next)
        self.back_b = Button(self, image=self.backward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                             border=0, command=self.go_back)
        self.exit_b = Button(self, image=self.exit_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                             border=0,
                             command=self.quit)
        self.auto_b = Button(self, image=self.auto_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                             border=0)
        self.add_b = Button(self, image=self.add_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
                            command=self.open_add_window)
        self.status_bar = Label(self, text=f"Image 1 of 1", bd=2, relief=SUNKEN,
                                bg=BACKGROUND_COLOR, fg=FOREGROUND, font=(FONT, 15), pady=5)

        # -------Widgets Grids--------
        self.canvas.grid(column=0, row=0, columnspan=5, padx=30, pady=15)
        self.next_b.grid(column=4, row=1, pady=10, sticky=W)
        self.back_b.grid(column=0, row=1, pady=10, sticky=E)
        self.exit_b.grid(column=2, row=1)
        self.auto_b.grid(column=1, row=1, sticky=E)
        self.add_b.grid(column=3, row=1, sticky=W)
        self.status_bar.grid(column=0, row=2, columnspan=5, sticky=W + E)

        self.mainloop()

    def go_next(self):
        print("next Working")
        self.index_count += 1
        self.status_number += 1
        if self.index_count < len(self.saved_photos_list):
            self.status_bar.config(text=f"Image {self.status_number} of {len(self.saved_photos_list)}")
            self.canvas.itemconfig(self.view_image, image=self.saved_photos_list[self.index_count])
        else:
            self.index_count = len(self.saved_photos_list) - 1
            self.status_number = len(self.saved_photos_list)

    def go_back(self):
        print("Back Working")
        self.index_count -= 1
        self.status_number -= 1
        if self.index_count < 0:
            self.index_count = 0
            self.status_number = 1
        else:
            self.status_bar.config(text=f"Image {self.status_number} of {len(self.saved_photos_list)}")
            self.canvas.itemconfig(self.view_image, image=self.saved_photos_list[self.index_count])

    def open_add_window(self):
        # -------Create Add Window
        # --Window canvas
        self.add_window = Toplevel(bg=BACKGROUND_COLOR, bd=5, relief="groove")
        self.add_window.wm_attributes('-topmost', 1)
        self.add_window.geometry("+800+300")
        self.add_window.minsize(width=300, height=300)
        self.add_window.resizable(False, False)
        self.add_window.iconbitmap("img/app_img/my.ico")
        self.add_window.title("Add a new album")
        # --Window widgets
        self.main_label = Label(self.add_window, text="Here you can add a new album.", font=(FONT, 15),
                                bg=BACKGROUND_COLOR, fg="white")
        self.album_name_l = Label(self.add_window, text="Album name   :", font=(FONT, 12), bg=BACKGROUND_COLOR,
                                  fg="white")
        self.select_img_l = Label(self.add_window, text="Album folder :", font=(FONT, 12), bg=BACKGROUND_COLOR,
                                  fg="white")
        self.exit_sub_w_b = Button(self.add_window, image=self.exit_sub_w_img, bg=BACKGROUND_COLOR,
                                   activebackground=BACKGROUND_COLOR, border=0, command=self.add_window.destroy)
        self.save_album_b = Button(self.add_window, image=self.save_album_img, bg=BACKGROUND_COLOR,
                                   activebackground=BACKGROUND_COLOR, border=0, command=self.save_create_album)
        self.album_name_e = Entry(self.add_window, width=15, bg=BACKGROUND_COLOR, fg="white", font=(FONT, 12))
        self.album_name_e.focus()
        self.select_img_b = Button(self.add_window, text="Select the folder.", font=(FONT, 12), bg=BACKGROUND_COLOR,
                                   fg="white", activebackground=ACTIVE_BACKGROUND, command=self.select_image)
        self.numbers_of_images = Label(self.add_window, text="Number of images.", font=(FONT, 12),
                                       background=BACKGROUND_COLOR, fg="white")
        # --Widgets grid
        self.main_label.grid(column=0, row=0, columnspan=3, pady=10)
        self.album_name_l.grid(column=0, row=1, pady=10, padx=5, sticky=W)
        self.select_img_l.grid(column=0, row=2, pady=10, padx=5, sticky=W)
        self.exit_sub_w_b.grid(column=1, row=4, pady=30)
        self.save_album_b.grid(column=0, row=4, pady=30, sticky=E)
        self.album_name_e.grid(column=1, row=1, pady=10, padx=5)
        self.select_img_b.grid(column=1, row=2, pady=10, padx=5)
        self.numbers_of_images.grid(column=0, row=3, columnspan=3, sticky=E + W)

    def select_image(self):
        # ------ Locate the current directory
        self.current_dir = os.getcwd()
        self.add_window.geometry("+200+200")
        self.image_path = filedialog.askopenfilename(initialdir=self.current_dir, title="Select an image",
                                                     filetypes=(("png files", "*.png"), ("all files", "*.*")))
        self.photos_list.append(PhotoImage(file=self.image_path))
        self.add_window.geometry("+800+300")
        self.numbers_of_images.config(text=str(len(self.saved_photos_list)))

    def save_create_album(self):
        self.saved_photos_list = list(self.photos_list)
        self.photos_list = []
        self.canvas.itemconfig(self.view_image, image=self.saved_photos_list[self.index_count])
        self.status_bar.config(text=f"Image {self.status_number} of {len(self.saved_photos_list)}")
        self.add_window.destroy()


test = PhotoAlbum()
