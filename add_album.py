from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

# ----Color  and Fonts --------#
FONT = "Coiny"
BACKGROUND_COLOR = "#20574f"
ACTIVE_BACKGROUND = "#b7ffef"
FOREGROUND = "#62d9c7"


class AddAlbum(Frame):
    def __init__(self, root_window):
        super().__init__()
        # --- objects images list
        self.img_objects_list = []
        # --- The name of the frame and the tab
        self.album_name_e = None
        # ---Counters
        self.index_count = 0
        self.status_number = 1
        # ----Application widgets images
        self.default_img = PhotoImage(file="img/app_img/defualt_img.png")
        self.forward_img = PhotoImage(file="img/app_img/fast-forwardr.png")
        self.backward_img = PhotoImage(file="img/app_img/fast-backwardr.png")
        self.exit_img = PhotoImage(file="img/app_img/exitr.png")
        self.auto_img = PhotoImage(file="img/app_img/auto_play.png")
        self.add_img = PhotoImage(file="img/app_img/plus.png")
        self.exit_sub_w_img = PhotoImage(file="img/app_img/exit_w.png")
        self.save_album_sub_w_img = PhotoImage(file="img/app_img/save.png")
        # ---Create Canvas object from create_album_frame
        self.canvas = None
        # --- save Canvas object to view image
        self.view_image = None
        # ---Status Bas counter
        self.status_bar = None
        # ---Add album window if there is no images in the list
        self.add_album_window = None
        # --- create an image objects list
        self.img_objects_list = []
        # ---Save files name by append it to self.img_objects_list
        self.image_file = None
        # --- it will take the length of the self.img_objects_list to update it to add images window
        self.numbers_of_images = None

    def create_album_win(self):

        self.config(bg=BACKGROUND_COLOR)
        self.img_objects_list.append(self.default_img)
        self.create_album_frame(self.TK)

    def create_album_frame(self, frame):
        self.canvas = Canvas(frame, width=600, height=350, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.view_image = self.canvas.create_image(300, 175, image=self.img_objects_list[self.index_count])
        forward_b = Button(frame, image=self.forward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                           border=0, command=self.forward)

        backward_b = Button(frame, image=self.backward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                            border=0, command=self.backward)
        exit_b = Button(frame, image=self.exit_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                        border=0,
                        command=self.root.quit)
        self.status_bar = Label(frame, text=f"Image 1 of {len(self.img_objects_list)}", bd=2, relief=SUNKEN,
                                bg=BACKGROUND_COLOR, fg=FOREGROUND,
                                font=(FONT, 15), pady=5)
        auto_b = Button(frame, image=self.auto_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                        border=0)
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
            self.index_count = len(self.img_objects_list) - 1
            self.status_number = len(self.img_objects_list)

    def backward(self):
        self.index_count -= 1
        self.status_number -= 1
        if self.index_count < 0:
            self.index_count = 0
            self.status_number = 1
        else:
            self.status_bar.config(text=f"Image {self.status_number} of {len(self.img_objects_list)}")
            self.canvas.itemconfig(self.view_image, image=self.img_objects_list[self.index_count])

    def add_images(self):
        current_dir = os.getcwd()
        self.add_album_window.geometry("+200+200")
        self.image_file = filedialog.askopenfilename(initialdir=current_dir, title="Select an image",
                                                     filetypes=(("png files", "*.png"), ("all files", "*.*")))
        self.img_objects_list.append(PhotoImage(file=self.image_file))
        self.numbers_of_images.config(text=str(len(self.img_objects_list)))

    def save_create_album(self):
        self.tab = ttk.Notebook(self.root)
        self.frame = Frame(self.root, bg=BACKGROUND_COLOR)
        self.tab.add(self.frame, text=self.album_name_e.get())
        self.create_album_frame(self.frame)
        self.tab.pack(expand=True, fill="both")
        self.add_album_window.destroy()

    def open_add_album(self):
        self.add_album_window = Toplevel(bg=BACKGROUND_COLOR, bd=5, relief="groove")
        self.add_album_window.wm_attributes('-topmost', 1)
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
                              activebackground=BACKGROUND_COLOR, border=0, command=self.save_create_album)
        self.album_name_e = Entry(self.add_album_window, width=15, bg=BACKGROUND_COLOR, fg="white", font=(FONT, 12))
        self.album_name_e.focus()
        album_folder_b = Button(self.add_album_window, text="Select the folder.", font=(FONT, 12), bg=BACKGROUND_COLOR,
                                fg="white", activebackground=ACTIVE_BACKGROUND, command=self.add_images)
        self.numbers_of_images = Label(self.add_album_window, text="C:/here your folder path", font=(FONT, 12),
                                       background=BACKGROUND_COLOR, fg="white")

        main_label.grid(column=0, row=0, columnspan=3, pady=10)
        album_name_l.grid(column=0, row=1, pady=10, padx=5, sticky=W)
        self.album_name_e.grid(column=1, row=1, pady=10, padx=5)
        album_folder_l.grid(column=0, row=2, pady=10, padx=5, sticky=W)
        album_folder_b.grid(column=1, row=2, pady=10, padx=5)
        self.numbers_of_images.grid(column=0, row=3, columnspan=3, sticky=E + W)
        exit_sub_w_b.grid(column=1, row=4, pady=30)
        save_album_b.grid(column=0, row=4, pady=30, sticky=E)


window = Tk()
window.title("Image Viewer")
window.geometry("+600+200")
window.resizable(False, False)
window.iconbitmap("img/app_img/my.ico")

window.mainloop()

