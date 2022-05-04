from tkinter import *


class Calc:
    def __init__(self, master):
        self.master = master
        self.ent1  = Entry(master, width=20)
        self.ent2  = Entry(master, width=20)
        self.sin  = Button(master, text="sin")
        self.x2  = Button(master, text="x^2")
        self.fact  = Button(master, text="n!")
        self.n7  = Button(master, text="7")
        self.n8  = Button(master, text="8")
        self.n9  = Button(master, text="9")
        self.dec  = Button(master, text="/")
        self.proc  = Button(master, text="%")





        self.plus  = Button(master, text="+")
        self.minus = Button(master, text="-")
        self.mult  = Button(master, text="*")
        self.dev   = Button(master, text="/")
        self.per   = Button(master, text="%")
        self.lab   = Label(master, width=20, bg='black', fg='white')

        self.plus['command'] = self.fun_plus
        self.minus['command'] = self.fun_minus
        self.mult['command'] = self.fun_mult
        self.dev['command'] = self.fun_dev
        self.per['command'] = self.fun_per

        opts = {'ipadx': 5, 'ipady': 5, 'sticky': 'nswe'}
        self.lab.grid(row=0, column=1,columnspan=8, **opts)
        self.ent1.grid(row=1, column=1,columnspan=4, **opts)
        self.ent2.grid(row=1, column=5,columnspan=4, **opts)
        self.plus.grid(row=2, column=1, **opts)
        self.minus.grid(row=2, column=2, **opts)
        self.mult.grid(row=2, column=3, **opts)
        self.dev.grid(row=2, column=4, **opts)
        self.per.grid(row=2, column=5, **opts)
        self.ent1.bind("<Button-1>", self.focus_ent1)
        self.ent2.bind("<Button-1>", self.focus_ent2)

    def focus_ent1(self, event):
        self.ent1["fg"] = "#c8c3bc"
        self.ent1["bg"] = "#0305bc"
        self.ent2["fg"] = "#000000"
        self.ent2["bg"] = "#ffffff"

    def focus_ent2(self, event):
        self.ent2["fg"] = "#c8c3bc"
        self.ent2["bg"] = "#0305bc"
        self.ent1["fg"] = "#000000"
        self.ent1["bg"] = "#ffffff"
        # self.master.itemconfig(, fill="blue", outline="blue")

    def fun_plus(self):
        try:
            self.lab['text'] = str(int(self.ent1.get()) + int(self.ent2.get()))
        except :
            self.lab['text'] = "error"
    def fun_minus(self):
        try:
            self.lab['text'] = str(int(self.ent1.get()) - int(self.ent2.get()))
        except :
            self.lab['text'] = "error"
    def fun_mult(self):
        try:
            self.lab['text'] = str(int(self.ent1.get()) * int(self.ent2.get()))
        except :
            self.lab['text'] = "error"
    def fun_dev(self):
        try:
            self.lab['text'] = str(int(self.ent1.get()) / int(self.ent2.get()))
        except :
            self.lab['text'] = "error"
    def fun_per(self):
        try:
            self.lab['text'] = str(int(self.ent1.get()) * int(self.ent2.get())/100)
        except :
            self.lab['text'] = "error"




root = Tk()

calc = Calc(root)

root.mainloop()