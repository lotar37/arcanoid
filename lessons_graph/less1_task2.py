from tkinter import *


root = Tk()

frame_top = LabelFrame(text="Цифры")
frame_top.pack(side=LEFT)
label_1 = Label(frame_top, width=7, height=4, bg='yellow', text="1")
label_1.grid(row=1, column=1)

# label_1.pack()
label_2 = Label(frame_top, width=7, height=4, bg='orange', text="2")
label_2.grid(row=1, column=2)

frame_bottom = LabelFrame(text="Низ")
frame_bottom.pack()
label_3 = Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3")
label_3.pack()
label_4 = Label(frame_bottom, width=7, height=4, bg='lightblue', text="4")
label_4.pack(side=LEFT)

root.mainloop()