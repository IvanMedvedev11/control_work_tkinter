from tkinter import *
def calculate(event):
    lbl['text'] = eval(ent.get())
root = Tk()
ent = Entry(root)
ent.place(x=10, y=10)
btn = Button(root, text='=')
btn.place(x=10, y=40)
lbl = Label()
lbl.place(x=10, y=70)
btn.bind('<Button-1>', calculate)
root.mainloop()
