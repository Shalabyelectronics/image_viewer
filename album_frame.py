# Today goal is to build an simple fram class that can be nested to the root window and add tab to it
from add_photos_window import AddPhoto
from tkinter import *
from tkinter import ttk
import os
import json

FONT = "Coiny"
BACKGROUND_COLOR = "#20574f"
ACTIVE_BACKGROUND = "#b7ffef"
FOREGROUND = "#62d9c7"


class AlbumFrame(Frame):
    def __init__(self, root_window):
        super().__init__()
        # ----Frame name
        # ----Widgets images objects.
        self.forward_img = PhotoImage(file="img/app_img/fast-forwardr.png")
        self.backward_img = PhotoImage(file="img/app_img/fast-backwardr.png")
        self.exit_img = PhotoImage(file="img/app_img/exitr.png")
        self.delete_album_img = PhotoImage(file="img/app_img/delete_album.png")
        self.add_img = PhotoImage(file="img/app_img/plus.png")
        self.default_image = PhotoImage(file="img/app_img/defualt_img.png")
        self.exit_sub_w_img = PhotoImage(file="img/app_img/exit_w.png")
        self.save_album_img = PhotoImage(file="img/app_img/save.png")
        # ----Frame background colors
        self.config(bg=BACKGROUND_COLOR)
        # ----Create the canvas object where we are going to place the photo.
        self.canvas = Canvas(self, width=600, height=350, bg=BACKGROUND_COLOR, highlightthickness=0)

        # ----Set the default image in the canvas.
        self.view_image = self.canvas.create_image(300, 175, image=self.default_image)
        # ----Interactive Buttons-------#
        # ---next photo button
        self.next_b = Button(self, image=self.forward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                             border=0, command=self.go_next)
        # ---back photo Button
        self.back_b = Button(self, image=self.backward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                             border=0, command=self.go_back)
        # ---exit photo album app
        self.exit_b = Button(self, image=self.exit_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                             border=0,
                             command=self.quit)
        # ---activate auto photo switch.
        self.delete_album_b = Button(self, image=self.delete_album_img, bg=BACKGROUND_COLOR,
                                     activebackground=BACKGROUND_COLOR,
                                     border=0)
        # ---add a new album or add photo in an existed  album
        self.add_b = Button(self, image=self.add_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0, command=AddPhoto)
        # ---Status bar where show the total photos and the current photo number.
        self.status_bar = Label(self, text="You are in default mode.", bd=2, relief=SUNKEN,
                                bg=BACKGROUND_COLOR, fg=FOREGROUND, font=(FONT, 15), pady=5)
        # ----Grid widgets
        self.canvas.grid(column=0, row=0, columnspan=5, padx=30, pady=15)
        self.next_b.grid(column=4, row=1, pady=10, sticky=W)
        self.back_b.grid(column=0, row=1, pady=10, sticky=E)
        self.exit_b.grid(column=2, row=1)
        self.delete_album_b.grid(column=1, row=1, sticky=E)
        self.add_b.grid(column=3, row=1, sticky=W)
        self.status_bar.grid(column=0, row=2, columnspan=5, sticky=W + E)
        # -----Counters ----------#
        # --index_count it is for photos index
        self.data_file = None
        self.index_count = 0
        # --status number to update the status bar
        self.status_number = 1
        # -----Photo List -----------#
        self.photos_list = []
        # ----Check if self.photos_list are not empty
        self.check_photos_list()

    # ------Methods ---------------------#
    # ----- Go next Method to switch to the next photo ------
    def go_next(self):
        print("next Working")
        if len(self.photos_list) > 0:
            self.index_count += 1
            self.status_number += 1
            if self.index_count < len(self.photos_list):
                self.status_bar.config(text=f"Image {self.status_number} of {len(self.photos_list)}")
                self.canvas.itemconfig(self.view_image, image=self.photos_list[self.index_count])
            else:
                self.index_count = len(self.photos_list) - 1
                self.status_number = len(self.photos_list)
        else:
            self.photos_list.append(self.default_image)

    # ---- Go back to switch to the previous photo.
    def go_back(self):
        print("Back Working")
        if len(self.photos_list) > 0:
            self.index_count -= 1
            self.status_number -= 1
            if self.index_count < 0:
                self.index_count = 0
                self.status_number = 1
            else:
                self.status_bar.config(text=f"Image {self.status_number} of {len(self.photos_list)}")
                self.canvas.itemconfig(self.view_image, image=self.photos_list[self.index_count])
        else:
            self.photos_list.append(self.default_image)

    # --- This function will remove the default photo and place the first index photo from photos_list.
    def check_photos_list(self):
        self.data_file = "data.json"
        if os.path.isfile(self.data_file) and os.path.getsize(self.data_file) > 0:
            with open(self.data_file, "r") as data:
                data = json.load(data)
                photos_list_temp = data["animals"]["photo"]
                for photo in photos_list_temp:
                    self.photos_list.append(PhotoImage(file=photo))
            self.canvas.itemconfig(self.view_image, image=self.photos_list[self.index_count])
            self.status_bar.config(text=f"Image {self.status_number} of {len(self.photos_list)}")

    # ----Call top level add photos window from add photo button
    # def open_add_window(self):
    #     AddPhoto()


root = Tk()
root.geometry("+800+200")
tab = ttk.Notebook()
frame_1 = AlbumFrame(root)
frame_2 = AlbumFrame(root)
frame_2.config(bg="red")
frame_1.grid(column=0, row=0, columnspan=5)
frame_2.grid(column=0, row=0, columnspan=5)
tab.add(frame_1, text="frame one")
# test = AddPhoto()
tab.add(frame_2, text="frame 2")
tab.grid(column=0, row=0)
root.mainloop()
# print(os.path.getsize("data.json"))
# with open("data.json", "r") as data:
#     data = json.load(data)
#     print(type(data))
    # if len(data) == 0:
    #     print("data file is empty.")
    # else:
    #     print("it is not empty.")


# def check_album():
#     album_data = os.path.isfile("data.json")
#     album_name = input("What is your album name : ")
#     add_photo = [1, 2, 3, 4, 5]
#     if album_data:
#         print("yes there is data file")
#         with open("data.json", "r") as photo_data:
#             json.load(photo_data)
#             print(photo_data[album_name]["photo"])
#     else:
#         print("Add a new a photo album")
#         album_data = {
#             album_name: {
#                 "photo": add_photo
#             }
#         }
#
#         with open("data.json", "w") as photo_data:
#             json.dump(album_data, photo_data)
#         with open("data.json", "r") as photo_data:
#             read_data = json.load(photo_data)
#             print(read_data)

# check_album()
#
# with open("data.json", "r") as data:
#     read_data = json.load(data)
#     if "animals" in read_data:
#         print("Do you want to add photo to animals? ")
#         add_new = int(input("add new photo: "))
#         add_to_album = read_data["animals"]["photo"]
#         add_to_album.append(add_new)
#         read_data.update(read_data)
#     else:
#         Creat a new entry
#
# with open("data.json","w") as data:
#     json.dump(read_data, data)
