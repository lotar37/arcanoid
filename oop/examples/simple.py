import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width = 500, height = 500)
canvas.pack()
radius = 40
bbox = -radius, -radius, radius, radius
oval = canvas.create_oval(*bbox, fill="red")
def move_oval():
    canvas.move(oval, 1, 1)
    canvas.after(10, move_oval)
# Start moving!
move_oval()
root.mainloop()