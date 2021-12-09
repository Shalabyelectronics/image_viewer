from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# -------------Set-Up my windows ----------#
# ----Color  and Fonts --------#
FONT = "Coiny"
BACKGROUND_COLOR = "#20574f"
FOREGROUND = "#62d9c7"
# ------Window----------#
root = Tk()
root.title("Image Viewer")
root.geometry("+600+200")
root.resizable(False, False)
root.iconbitmap("img/app_img/my.ico")
root.config(bg=BACKGROUND_COLOR, bd=5, relief="ridge")
# ----------- Additional
tabs = ttk.Notebook(root)
natural_frame = Frame(root, bg=BACKGROUND_COLOR)
animals_frame = Frame(root, bg=BACKGROUND_COLOR)
tabs.add(natural_frame, text="Natural Images")
tabs.add(animals_frame, text="Animals Images")
canvas = Canvas(natural_frame, width=600, height=350, bg=BACKGROUND_COLOR, highlightthickness=0)
root.filename = filedialog.askopenfile()
# -------------Natural Images--------#
natural_img_1 = PhotoImage(file="img/neutral_img/n1.png")
natural_img_2 = PhotoImage(file="img/neutral_img/n2.png")
natural_img_3 = PhotoImage(file="img/neutral_img/n3.png")
natural_img_4 = PhotoImage(file="img/neutral_img/n4.png")
natural_img_5 = PhotoImage(file="img/neutral_img/n5.png")
natural_img_6 = PhotoImage(file="img/neutral_img/n6.png")
natural_img_7 = PhotoImage(file="img/neutral_img/n7.png")

images_list = [natural_img_1, natural_img_2, natural_img_3, natural_img_4, natural_img_5, natural_img_6, natural_img_7]

# ---------------Animals Images----------------#

# ---------------Buttons Images----------------#
forward_img = PhotoImage(file="img/app_img/fast-forwardr.png")
backward_img = PhotoImage(file="img/app_img/fast-backwardr.png")
exit_img = PhotoImage(file="img/app_img/exitr.png")
auto_img = PhotoImage(file="img/app_img/auto_play.png")
add_img = PhotoImage(file="img/app_img/plus.png")
# ---------------Image viewer Function----------#
# Counter
index_count = 0
status_number = 1


# -----------Open add album window----------#
def open_add_album():
    add_album_window = Toplevel(bg=BACKGROUND_COLOR, bd=5, relief="groove")
    add_album_window.geometry("+800+300")
    add_album_window.minsize(width=300, height=300)
    add_album_window.resizable(False,False)
    add_album_window.iconbitmap("img/app_img/my.ico")
    add_album_window.title("Add a new album")
    test = Label(add_album_window, text="Welcom")
    test.pack()


# ----------Go forward Function ------------#
def go_forward():
    global status_number, index_count
    index_count += 1
    status_number += 1
    if index_count < len(images_list):
        status_bar.config(text=f"Image {status_number} of {len(images_list)}")
        canvas.itemconfig(view_image, image=images_list[index_count])
    else:
        index_count = 6
        status_number = 7


# ----------Go backward Function ------------#
def go_backward():
    global status_number, index_count
    index_count -= 1
    status_number -= 1
    if index_count < 0:
        index_count = 0
        status_number = 1
    else:
        status_bar.config(text=f"Image {status_number} of {len(images_list)}")
        canvas.itemconfig(view_image, image=images_list[index_count])


# --------------Widgets--------------#

view_image = canvas.create_image(300, 175, image=images_list[index_count])
forward_b = Button(natural_frame, image=forward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
                   command=go_forward)
backward_b = Button(natural_frame, image=backward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
                    command=go_backward)
exit_b = Button(natural_frame, image=exit_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
                command=root.quit)
status_bar = Label(natural_frame, text=f"Image 1 of {len(images_list)}", bd=2, relief=SUNKEN, bg=BACKGROUND_COLOR,
                   fg=FOREGROUND,
                   font=(FONT, 15), pady=5)
auto_b = Button(natural_frame, image=auto_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0)
add_b = Button(natural_frame, image=add_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0, command= open_add_album)
# --------Grid widgets positions---------#
auto_b.grid(column=1, row=1, sticky=E)
add_b.grid(column=3, row=1, sticky=W)
canvas.grid(column=0, row=0, columnspan=5, padx=30, pady=15)
backward_b.grid(column=0, row=1, pady=10, sticky=E)
forward_b.grid(column=4, row=1, pady=10, sticky=W)
exit_b.grid(column=2, row=1)
status_bar.grid(column=0, row=2, columnspan=5, sticky=W + E)
tabs.pack(expand=True, fill="both")

root.mainloop()
