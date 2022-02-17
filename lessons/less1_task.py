from tkinter import *


class Calc:
    def __init__(self, master):
        self.ent1  = Entry(master, width=20)
        self.ent2  = Entry(master, width=20)
        self.plus  = Button(master, text="+")
        self.minus = Button(master, text="-")
        self.mult  = Button(master, text="*")
        self.dev   = Button(master, text="/")
        self.lab   = Label(master, width=20,
                         bg='black', fg='white')

        self.plus['command'] = self.fun_plus
        self.minus['command'] = self.fun_minus
        self.mult['command'] = self.fun_mult
        self.dev['command'] = self.fun_dev

        self.ent1.pack()
        self.ent2.pack()
        self.plus.pack()
        self.minus.pack()
        self.mult.pack()
        self.dev.pack()
        self.lab.pack()

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




root = Tk()

calc = Calc(root)

root.mainloop()