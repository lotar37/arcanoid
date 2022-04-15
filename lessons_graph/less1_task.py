from tkinter import *


class Calc:
    def __init__(self, master):
        self.ent1  = Entry(master, width=20)
        self.ent2  = Entry(master, width=20)
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
        self.lab.grid(row=0, column=1,columnspan=5, **opts)
        self.ent1.grid(row=1, column=1,columnspan=2, **opts)
        self.ent2.grid(row=1, column=3,columnspan=3, **opts)
        self.plus.grid(row=2, column=1, **opts)
        self.minus.grid(row=2, column=2, **opts)
        self.mult.grid(row=2, column=3, **opts)
        self.dev.grid(row=2, column=4, **opts)
        self.per.grid(row=2, column=5, **opts)

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