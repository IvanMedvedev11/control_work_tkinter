import tkinter as tk
def animate_circle(start_x, start_y, target_x, target_y, steps=20, delay=20):
    dx = (target_x - start_x) / steps 
    dy = (target_y - start_y) / steps 

    def move_step(step=0):
        if step < steps:
            new_x = start_x + dx * (step + 1)
            new_y = start_y + dy * (step + 1)
            canvas.coords(circle, new_x - radius, new_y - radius,
                          new_x + radius, new_y + radius)
            root.after(delay, move_step, step + 1)
    move_step()
def on_click(event):
    x1, y1, x2, y2 = canvas.coords(circle)
    current_x = (x1 + x2) / 2
    current_y = (y1 + y2) / 2
    animate_circle(current_x, current_y, event.x, event.y)
root = tk.Tk()
root.title("Плавное перемещение круга")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()
radius = 30
start_x, start_y = 200, 200
circle = canvas.create_oval(
    start_x - radius, start_y - radius,
    start_x + radius, start_y + radius,
    fill="blue", outline="black"
)
canvas.bind("<Button-1>", on_click)

root.mainloop()
