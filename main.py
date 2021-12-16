from build_album import *

root = Tk()
root.geometry("+800+200")
root.iconbitmap(default="img/app_img/my.ico")
root.title("Photo Album App")
tab = ttk.Notebook()


def load_album():
    if os.path.isfile("data.json"):
        with open("data.json", "r") as data:
            data = json.load(data)
            for album in data:
                new_frame = AlbumFrame(root, album, tab_note=tab)
                new_frame.photos_list = [PhotoImage(file=image) for image in data[album]["photos list"]]
                new_frame.canvas.itemconfig(new_frame.view_image, image=new_frame.photos_list[0])
                new_frame.status_bar.config(text=f"Image {new_frame.status_number} of {len(new_frame.photos_list)}")
                new_frame.grid(column=0, row=0, columnspan=5)
                tab.add(new_frame, text=album)
                tab.grid(column=0, row=0)
    else:
        default_frame = AlbumFrame(root, album_name="defualt", tab_note=tab)
        default_frame.grid(column=0, row=0, columnspan=5)
        tab.add(default_frame, text="default")
        tab.grid(column=0, row=0)


load_album()

root.mainloop()
