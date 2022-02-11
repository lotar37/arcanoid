#!/usr/bin/python
# -*- coding: utf-8 -*-



from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Кнопка выхода из приложения")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Закрыть окно", command=self.quit)
        quitButton.place(x=50, y=50)


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()