from tkinter import *

# -------------Set-Up my windows ----------#
# ----Color
BACKGROUND_COLOR = "#20574f"
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
index_count = 0


def go_forward():
    global index_count
    index_count += 1
    try:
        canvas.itemconfig(view_image, image=images_list[index_count])
    except IndexError:
        index_count = 0
        canvas.itemconfig(view_image, image=images_list[index_count])


# ------------Go back word Function------------#
def go_backward():
    global index_count
    index_count -= 1
    try:
        canvas.itemconfig(view_image, image=images_list[index_count])
    except IndexError:
        index_count = -1
        canvas.itemconfig(view_image, image=images_list[index_count])


# --------------Widgets--------------#

view_image = canvas.create_image(300, 175, image=images_list[index_count])
forward_b = Button(image=forward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
                   command=go_forward)
backward_b = Button(image=backward_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0,
                    command=go_backward)
exit_b = Button(image=exit_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, border=0, command=root.quit)
# --------Grid widgets positions---------#

canvas.grid(column=0, row=0, columnspan=3, padx=30, pady=15)
backward_b.grid(column=0, row=1, pady=10, sticky=E)
forward_b.grid(column=2, row=1, pady=10, sticky=W)
exit_b.grid(column=1, row=1)

root.mainloop()
