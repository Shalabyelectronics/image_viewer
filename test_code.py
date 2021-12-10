import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

FONT = "Coiny"
BACKGROUND_COLOR = "#20574f"
ACTIVE_BACKGROUND = "#b7ffef"
FOREGROUND = "#62d9c7"


class PhotoAlbum(Tk):
    def __init__(self):
        super().__init__()
        self.add_window = None
        self.current_dir = None
        self.title("Image Viewer")
        self.geometry("+600+200")
        self.resizable(False, False)
        self.iconbitmap("img/app_img/my.ico")
        self.config(bg=BACKGROUND_COLOR, bd=5, relief="ridge")
        self.canvas = Canvas(self, width=600, height=350, bg="white", highlightthickness=0)
        self.photos_list = []
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
        self.add_b = Button(self, image=self.add_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0)
        self.status_bar = Label(self, text=f"Image 1 of Test", bd=2, relief=SUNKEN,
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
        if self.index_count < len(self.photos_list):
            self.status_bar.config(text=f"Image {self.status_number} of {len(self.photos_list)}")
            self.canvas.itemconfig(self.view_image, image=self.photos_list[self.index_count])
        else:
            self.index_count = len(self.photos_list) - 1
            self.status_number = len(self.photos_list)

    def go_back(self):
        print("Back Working")
        self.index_count -= 1
        self.status_number -= 1
        if self.index_count < 0:
            self.index_count = 0
            self.status_number = 1
        else:
            self.status_bar.config(text=f"Image {self.status_number} of {len(self.photos_list)}")
            self.canvas.itemconfig(self.view_image, image=self.photos_list[self.index_count])

    def open_add_window(self):
        self.current_dir = os.getcwd()
        self.add_window = Toplevel(bg=BACKGROUND_COLOR, bd=5, relief="groove")


test = PhotoAlbum()
# # -------------Set-Up my windows ----------#
# # ----Color  and Fonts --------#
# FONT = "Coiny"
# BACKGROUND_COLOR = "#20574f"
# FOREGROUND = "#62d9c7"
# # ------Window----------#
# root = Tk()
# root.title("Image Viewer")
# root.geometry("+600+200")
# root.resizable(False, False)
# root.iconbitmap("img/app_img/my.ico")
# root.config(bg=BACKGROUND_COLOR, bd=5, relief="ridge")
# # ----------- Additional
# tabs = ttk.Notebook(root)
# natural_frame = Frame(root, bg=BACKGROUND_COLOR)
# animals_frame = Frame(root, bg=BACKGROUND_COLOR)
# tabs.add(natural_frame, text="Natural Images")
# tabs.add(animals_frame, text="Animals Images")
# canvas = Canvas(natural_frame, width=600, height=350, bg=BACKGROUND_COLOR, highlightthickness=0)
# root.filename = filedialog.askopenfile()
# # -------------Natural Images--------#
# natural_img_1 = PhotoImage(file="img/neutral_img/n1.png")
# natural_img_2 = PhotoImage(file="img/neutral_img/n2.png")
# natural_img_3 = PhotoImage(file="img/neutral_img/n3.png")
# natural_img_4 = PhotoImage(file="img/neutral_img/n4.png")
# natural_img_5 = PhotoImage(file="img/neutral_img/n5.png")
# natural_img_6 = PhotoImage(file="img/neutral_img/n6.png")
# natural_img_7 = PhotoImage(file="img/neutral_img/n7.png")
#
# images_list = [natural_img_1, natural_img_2, natural_img_3, natural_img_4, natural_img_5, natural_img_6, natural_img_7]
#
# # ---------------Animals Images----------------#
#
# # ---------------Buttons Images----------------#
# self.forward_img = PhotoImage(file="img/app_img/fast-forwardr.png")
# self.backward_img = PhotoImage(file="img/app_img/fast-backwardr.png")
# self.exit_img = PhotoImage(file="img/app_img/exitr.png")
# self.auto_img = PhotoImage(file="img/app_img/auto_play.png")
# self.add_img = PhotoImage(file="img/app_img/plus.png")
# # ---------------Image viewer Function----------#
# # Counter
# index_count = 0
# status_number = 1
#
#
# # -----------Open add album window----------#
# def open_add_album():
#     add_album_window = Toplevel(bg=BACKGROUND_COLOR, bd=5, relief="groove")
#     add_album_window.geometry("+800+300")
#     add_album_window.minsize(width=300, height=300)
#     add_album_window.resizable(False,False)
#     add_album_window.iconbitmap("img/app_img/my.ico")
#     add_album_window.title("Add a new album")
#     test = Label(add_album_window, text="Welcom")
#     test.pack()
#
#
# # ----------Go forward Function ------------#
# def go_forward():
#     global status_number, index_count
#     index_count += 1
#     status_number += 1
#     if index_count < len(images_list):
#         status_bar.config(text=f"Image {status_number} of {len(images_list)}")
#         canvas.itemconfig(view_image, image=images_list[index_count])
#     else:
#         index_count = 6
#         status_number = 7
#
#
# # ----------Go backward Function ------------#
# def go_backward():
#     global status_number, index_count
#     index_count -= 1
#     status_number -= 1
#     if index_count < 0:
#         index_count = 0
#         status_number = 1
#     else:
#         status_bar.config(text=f"Image {status_number} of {len(images_list)}")
#         canvas.itemconfig(view_image, image=images_list[index_count])
#
#
# # --------------Widgets--------------#
#
# view_image = canvas.create_image(300, 175, image=images_list[index_count])
# forward_b = Button(natural_frame, image=self.forward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
#                    command=go_forward)
# backward_b = Button(natural_frame, image=self.backward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
#                     command=go_backward)
# self.exit_b = Button(natural_frame, image=self.exit_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
#                 command=root.quit)
# status_bar = Label(natural_frame, text=f"Image 1 of {len(images_list)}", bd=2, relief=SUNKEN, bg=BACKGROUND_COLOR,
#                    fg=FOREGROUND,
#                    font=(FONT, 15), pady=5)
# self.auto_b = Button(natural_frame, image=self.auto_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0)
# self.add_b = Button(natural_frame, image=self.add_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0, command= open_add_album)
# # --------Grid widgets positions---------#
# self.auto_b.grid(column=1, row=1, sticky=E)
# self.add_b.grid(column=3, row=1, sticky=W)
# canvas.grid(column=0, row=0, columnspan=5, padx=30, pady=15)
# backward_b.grid(column=0, row=1, pady=10, sticky=E)
# forward_b.grid(column=4, row=1, pady=10, sticky=W)
# self.exit_b.grid(column=2, row=1)
# status_bar.grid(column=0, row=2, columnspan=5, sticky=W + E)
# tabs.pack(expand=True, fill="both")
#
# root.mainloop()
