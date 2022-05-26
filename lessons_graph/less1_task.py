from tkinter import *


class Calc:
    def __init__(self, master):
        self.master = master
        numFrame = Frame(master)
        allFrame = Frame(master)
        simpleFrame = Frame(master)
        frFrame = Frame(master)
        # .grid(row=0, column=1, columnspan=8
        allFrame.grid(row=1, column=1, columnspan=2)
        frFrame.grid(row=2, column=1, columnspan=2)
        numFrame.grid(row=3, column=1)
        simpleFrame.grid(row=3, column=2)

        self.lab   = Label(allFrame, width=20, bg='black', fg='white')
        self.ent1  = Entry(allFrame, width=20)
        self.ent2  = Entry(allFrame, width=20)
        self.sin  = Button(allFrame, text="sin")
        self.x2  = Button(allFrame, text="x^2")
        self.fact  = Button(allFrame, text="n!")
        self.n7  = Button(numFrame, text="7")
        self.n8  = Button(numFrame, text="8")
        self.n9  = Button(numFrame, text="9")
        self.n4  = Button(numFrame, text="4")
        self.n5  = Button(numFrame, text="5")
        self.n6  = Button(numFrame, text="6")
        self.n1  = Button(numFrame, text="1")
        self.n2  = Button(numFrame, text="2")
        self.n3  = Button(numFrame, text="3")
        self.n0  = Button(numFrame, text="0")
        self.dec  = Button(allFrame, text="/")
        self.proc  = Button(allFrame, text="%")
        self.C  = Button(frFrame, text="C")
        self.delete  = Button(frFrame, text="<-")
        self.active = self.ent1




        self.plus  = Button(simpleFrame, text="+")
        self.minus = Button(simpleFrame, text="-")
        self.mult  = Button(simpleFrame, text="*")
        self.dev   = Button(simpleFrame, text="/")
        self.per   = Button(allFrame, text="%")

        self.plus['command'] = self.fun_plus
        self.minus['command'] = self.fun_minus
        self.mult['command'] = self.fun_mult
        self.dev['command'] = self.fun_dev
        self.per['command'] = self.fun_per
        self.n9['command'] = self.fun_n9
        self.n8['command'] = self.fun_n8
        self.n7['command'] = self.fun_n7
        self.n6['command'] = self.fun_n6
        self.C['command'] = self.fun_delete_all
        self.delete['command'] = self.fun_delete_last

        opts = {'ipadx': 15, 'ipady': 5, 'sticky': 'nswe'}
        self.C.grid(row=1, column=1, **opts)
        self.delete.grid(row=1, column=2, **opts)
        self.lab.grid(row=0, column=1,columnspan=8, **opts)
        self.ent1.grid(row=1, column=1,columnspan=4, **opts)
        self.ent2.grid(row=1, column=5,columnspan=4, **opts)

        self.plus.grid(row=1, column=1, **opts)
        self.minus.grid(row=2, column=1, **opts)
        self.mult.grid(row=3, column=1, **opts)
        self.dev.grid(row=4, column=1, **opts)


        # self.per.grid(row=2, column=5, **opts)


        opts = {'ipadx': 5, 'ipady': 9, 'sticky': 'nswe'}

        self.n9.grid(row=1, column=3, **opts)
        self.n8.grid(row=1, column=2, **opts)
        self.n7.grid(row=1, column=1, **opts)
        self.n4.grid(row=2, column=1, **opts)
        self.n5.grid(row=2, column=2, **opts)
        self.n6.grid(row=2, column=3, **opts)
        self.n1.grid(row=3, column=1, **opts)
        self.n2.grid(row=3, column=2, **opts)
        self.n3.grid(row=3, column=3, **opts)
        self.n0.grid(row=4, column=1, columnspan=3, **opts)


        self.ent1.bind("<Button-1>", self.focus_ent1)
        self.ent2.bind("<Button-1>", self.focus_ent2)

    def focus_ent1(self, event):
        self.ent1["fg"] = "#000000"
        self.ent1["bg"] = "#aaaabc"
        self.ent2["fg"] = "#000000"
        self.ent2["bg"] = "#ffffff"
        self.active = self.ent1

    def focus_ent2(self, event):
        self.ent2["fg"] = "#000000"
        self.ent2["bg"] = "#aaaabc"
        self.ent1["fg"] = "#000000"
        self.ent1["bg"] = "#ffffff"
        self.active = self.ent2

        # self.master.itemconfig(, fill="blue", outline="blue")

    def fun_delete_all(self):
        self.ent1.delete(0,END)
        self.ent2.delete(0,END)


    def fun_delete_last(self):
        self.active.delete(END)

    def fun_n9(self):
        self.active.insert(END,"9")
    def fun_n8(self):
        self.active.insert(END,"8")
    def fun_n7(self):
        self.active.insert(END,"7")
    def fun_n6(self):
        self.active.insert(END,"6")



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