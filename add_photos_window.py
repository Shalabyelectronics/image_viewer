from tkinter import *
import os, sys, stat
import shutil
from tkinter import messagebox
from tkinter import filedialog

# ----Color  and Fonts --------#
FONT = "Coiny"
BACKGROUND_COLOR = "#20574f"
ACTIVE_BACKGROUND = "#b7ffef"
FOREGROUND = "#62d9c7"


class AddPhoto(Toplevel):
    def __init__(self):
        super().__init__()
        self.update_album = None
        self.album_folders = None
        self.new_album_folder = None
        self.photo_path = None
        self.current_dir = None
        self.album_data = None
        self.existed_album = None
        self.photos_paths_list = []
        self.exit_img = PhotoImage(file="img/app_img/exit_w.png")
        self.save_img = PhotoImage(file="img/app_img/save.png")
        self.search_img = PhotoImage(file="img/app_img/search.png")
        self.config(bg=BACKGROUND_COLOR, bd=5, relief="groove")
        self.wm_attributes('-topmost', 1)
        self.geometry("+800+300")
        self.minsize(width=300, height=300)
        self.resizable(False, False)
        self.iconbitmap("img/app_img/my.ico")
        self.title("Add a new album")
        self.main_label = Label(self, text="Here you can add a new album.", font=(FONT, 15),
                                bg=BACKGROUND_COLOR, fg="white")
        self.album_name_l = Label(self, text="Album name   :", font=(FONT, 12), bg=BACKGROUND_COLOR,
                                  fg="white")
        self.album_folder_l = Label(self, text="Album folder :", font=(FONT, 12), bg=BACKGROUND_COLOR,
                                    fg="white")
        self.exit_sub_w_b = Button(self, image=self.exit_img, bg=BACKGROUND_COLOR,
                                   activebackground=BACKGROUND_COLOR, border=0, command=self.destroy)
        self.save_album_b = Button(self, image=self.save_img, bg=BACKGROUND_COLOR,
                                   activebackground=BACKGROUND_COLOR, border=0, command=self.save)
        self.album_name_e = Entry(self, width=15, bg=BACKGROUND_COLOR, fg="white", font=(FONT, 12))
        self.album_name_e.focus()
        self.search_b = Button(self, image=self.search_img, bg=BACKGROUND_COLOR,
                               activebackground=BACKGROUND_COLOR, border=0, command=self.search)
        self.album_folder_b = Button(self, text="Select the photos.", font=(FONT, 12), bg=BACKGROUND_COLOR,
                                     fg="white", activebackground=ACTIVE_BACKGROUND, command=self.select_photo)
        self.numbers_of_images = Label(self, text="C:/here your folder path", font=(FONT, 12),
                                       background=BACKGROUND_COLOR, fg="white")

        self.main_label.grid(column=0, row=0, columnspan=4, pady=10)
        self.album_name_l.grid(column=0, row=1, pady=10, padx=5, sticky=W)
        self.album_name_e.grid(column=1, row=1, pady=10, padx=5)
        self.search_b.grid(column=2, row=1, pady=10, padx=5)
        self.album_folder_l.grid(column=0, row=2, pady=10, padx=5, sticky=W)
        self.album_folder_b.grid(column=1, row=2, pady=10, padx=5)
        self.numbers_of_images.grid(column=0, row=3, columnspan=3, sticky=E + W)
        self.exit_sub_w_b.grid(column=1, row=4, pady=30)
        self.save_album_b.grid(column=0, row=4, pady=30, sticky=E)

    # -----When user press search key if the data file is exist then will check if data file not empty
    # --Finally if not, and we have a data in the file get the entry data and check inside our dictionary if
    # -The album exist just update the photo list if not create a new entry.
    def search(self):
        self.album_folders = os.listdir(f"{os.getcwd()}/img")
        if len(self.album_name_e.get()) > 0 and self.album_name_e.get() in self.album_folders:
            self.wm_attributes('-topmost', 0)
            info = messagebox.showinfo(title="Album found", message=f"{self.album_name_e.get()} album is already "
                                                                    f"found "
                                                                    f"and you can update your photos by adding new "
                                                                    f"ones then hit save.")
            if info == "ok":
                self.wm_attributes('-topmost', 1)

        elif len(self.album_name_e.get()) > 0 and self.album_name_e.get() not in self.album_folders:
            self.wm_attributes('-topmost', 0)
            info = messagebox.showinfo(title="Search result",
                                       message=f"{self.album_name_e.get()} album not found "
                                               f"you can create a new album by adding new "
                                               f"photos then hit save.")
            if info == "ok":
                self.wm_attributes('-topmost', 1)
        else:
            self.wm_attributes('-topmost', 0)
            info = messagebox.showinfo(title="There is no data file",
                                       message="You need to create a new album as there is no "
                                               "any album stored in your data file yet.")
            if info == "ok":
                self.wm_attributes('-topmost', 1)

    def select_photo(self):
        self.album_folders = os.listdir(f"{os.getcwd()}/img")

        if len(self.album_name_e.get()) > 0 and self.album_name_e.get() in self.album_folders:
            self.geometry("+200+200")
            self.photo_path = list(filedialog.askopenfilenames(initialdir=self.current_dir, title="Select an image",
                                                               filetypes=(
                                                                   ("png files", "*.png"), ("all files", "*.*"))))
            self.update_album = f"img/{self.album_name_e.get()}"


        elif len(self.album_name_e.get()) > 0 and self.album_name_e.get() not in self.album_folders:
            self.photo_path = list(filedialog.askopenfilenames(initialdir=self.current_dir, title="Select an image",
                                                               filetypes=(
                                                                   ("png files", "*.png"), ("all files", "*.*"))))
            os.mkdir(f"img/{self.album_name_e.get()}")
            self.new_album_folder = f"img/{self.album_name_e.get()}"
        else:
            self.wm_attributes('-topmost', 0)
            info = messagebox.showinfo(title="Required", message="Please, do not leave album name empty.")
            if info == "ok":
                self.wm_attributes('-topmost', 1)

    def save(self):
        if self.new_album_folder is not None:
            self.save_update(self.new_album_folder)
        elif self.update_album is not None:
            self.save_update(self.update_album)
        else:
            self.wm_attributes('-topmost', 0)
            info = messagebox.showinfo(title="Album not Created", message=f"Please try again.")
            if info == "ok":
                self.wm_attributes('-topmost', 1)

    def save_update(self, album):
        for photo in self.photo_path:
            shutil.copy(photo, album)
        for photo in os.listdir(album):
            self.photos_paths_list.append(PhotoImage(file=f"{album}/{photo}"))
        self.wm_attributes('-topmost', 0)
        info = messagebox.showinfo(title="Album Created", message=f"You have created {self.album_name_e.get()} album "
                                                                  f"with {os.listdir(album)}.")
        if info == "ok":
            self.destroy()
        print(self.photos_paths_list)
