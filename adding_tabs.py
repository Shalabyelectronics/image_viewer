from add_album import *

FONT = "Coiny"
BACKGROUND_COLOR = "#20574f"
FOREGROUND = "#62d9c7"
# ------Window----------#
root = Tk()
root.title("Image Viewer")
root.geometry("+600+200")
root.resizable(False, False)
root.iconbitmap("img/app_img/my.ico")
root.config(bg=BACKGROUND_COLOR)
tab = ttk.Notebook(root)
neutral = Frame(root, bg=BACKGROUND_COLOR)
animals = Frame(root, bg=BACKGROUND_COLOR)
tab.add(neutral, text="Neutral")
tab.add(animals, text="Animals")

neutral_album = Add_album(album_name="Neutral", photos_list=[
    "img/neutral_img/n1.png",
    "img/neutral_img/n2.png",
    "img/neutral_img/n3.png",
    "img/neutral_img/n4.png",
    "img/neutral_img/n5.png",
    "img/neutral_img/n6.png",
    "img/neutral_img/n7.png"])
neutral_album.create_album_frame(neutral, background_color=BACKGROUND_COLOR)

animals_album = Add_album(album_name="Animals", photos_list=[
    "img/animals_img/a_1.png",
    "img/animals_img/a_2.png",
    "img/animals_img/a_3.png",
    "img/animals_img/a_4.png",
    "img/animals_img/a_5.png",
    "img/animals_img/a_6.png",
    "img/animals_img/a_7.png"
])
animals_album.create_album_frame(animals, background_color=BACKGROUND_COLOR)
tab.pack(expand=True, fill="both")
root.mainloop()
