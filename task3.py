from tkinter import *
def move(event):
    global oval
    canvas.move(oval, event.x - 50 - canvas.coords(oval)[0], event.y - 50 - canvas.coords(oval)[1])
root = Tk()
root.geometry("500x500")
canvas = Canvas(root, width=500, height=500, bg='lightblue')
oval = canvas.create_oval([100, 100], [200, 200], fill='yellow')
canvas.bind('<Button-1>', move)
canvas.pack()
root.mainloop()
