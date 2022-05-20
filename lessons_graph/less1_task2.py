from tkinter import *


root = Tk()
frame_top = LabelFrame(text="")
frame_top.pack(side=LEFT)
label_1 = Label(frame_top, width=7, height=4, bg='yellow', text="1")
label_1.grid(row=1, column=1)

# label_1.pack()
label_2 = Label(frame_top, width=7, height=4, bg='orange', text="2")
label_2.grid(row=1, column=2)

frame_bottom = LabelFrame(text="Низ")
frame_bottom.pack(side=BOTTOM)
label_3 = Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3")
label_3.pack()
label_4 = Label(frame_bottom, width=7, height=4, bg='lightblue', text="4")
label_4.pack(side=LEFT)


top.geometry("140x100")
frame = Frame(top)
frame.pack()

leftframe = Frame(top)
leftframe.pack(side=LEFT)

rightframe = Frame(top)
rightframe.pack(side=RIGHT)

btn1 = Button(frame, text="Submit", fg="red", activebackground="red")
btn1.pack(side=LEFT)

btn2 = Button(frame, text="Remove", fg="brown", activebackground="brown")
btn2.pack(side=RIGHT)

btn3 = Button(rightframe, text="Add", fg="blue", activebackground="blue")
btn3.pack(side=LEFT)

btn4 = Button(leftframe, text="Modify", fg="black", activebackground="white")
btn4.pack(side=RIGHT)

top.mainloop()


root.mainloop()