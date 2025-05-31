from tkinter import *
def show_up(event):
    global lbl
    lbl['text'] = "верх"

def show_down(event):
    global lbl
    lbl['text'] = "низ"

def show_left(event):
    global lbl
    lbl['text'] = "лево"


def show_right(event):
    global lbl
    lbl['text'] = "право"
root = Tk()
lbl = Label(root)
lbl.place(x=100, y=100)
root.bind('<Up>', show_up)
root.bind('<Down>', show_down)
root.bind('<Left>', show_left)
root.bind('<Right>', show_right)
root.mainloop()
