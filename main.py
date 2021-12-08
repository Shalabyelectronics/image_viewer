from tkinter import *

# -------------Set-Up my windows ----------#
# ----Color  and Fonts --------#
FONT = "Coiny"
BACKGROUND_COLOR = "#20574f"
FOREGROUND = "#62d9c7"
# ------Window
root = Tk()
root.title("Image Viewer")
root.geometry("+600+200")
root.resizable(False, False)
root.iconbitmap("img/my.ico")
root.config(bg=BACKGROUND_COLOR)
canvas = Canvas(width=600, height=350, bg=BACKGROUND_COLOR, highlightthickness=0)
# -------------Natural Images--------#
natural_img_1 = PhotoImage(file="img/n1.png")
natural_img_2 = PhotoImage(file="img/n2.png")
natural_img_3 = PhotoImage(file="img/n3.png")
natural_img_4 = PhotoImage(file="img/n4.png")
natural_img_5 = PhotoImage(file="img/n5.png")
natural_img_6 = PhotoImage(file="img/n6.png")
natural_img_7 = PhotoImage(file="img/n7.png")

images_list = [natural_img_1, natural_img_2, natural_img_3, natural_img_4, natural_img_5, natural_img_6, natural_img_7]
# ---------------Buttons Images----------------#
forward_img = PhotoImage(file="img/fast-forwardr.png")
backward_img = PhotoImage(file="img/fast-backwardr.png")
exit_img = PhotoImage(file="img/exitr.png")
# ---------------Image viewer Function----------#
# Counter
index_count = 0
status_number = 1


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
forward_b = Button(image=forward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
                   command=go_forward)
backward_b = Button(image=backward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
                    command=go_backward)
exit_b = Button(image=exit_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0, command=root.quit)
status_bar = Label(text=f"Image 1 of {len(images_list)}", bd=2, relief=SUNKEN, bg=BACKGROUND_COLOR, fg=FOREGROUND,
                   font=(FONT, 15), pady=5)

# --------Grid widgets positions---------#

canvas.grid(column=0, row=0, columnspan=3, padx=30, pady=15)
backward_b.grid(column=0, row=1, pady=10, sticky=E)
forward_b.grid(column=2, row=1, pady=10, sticky=W)
exit_b.grid(column=1, row=1)
status_bar.grid(column=0, row=2, columnspan=3, sticky=W + E)

root.mainloop()
