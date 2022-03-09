from PyQt5 import QtWidgets
from less6_window2 import Ui_MainWindow  # импорт нашего сгенерированного файла

import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.verticalLayout.setObjectName(u"verticalLayout")

        # # Меняем текст
        # self.ui.lineEdit.setText("Добро пожаловать на PythonScripts")
        #
        # # указать максимальную длину
        # self.ui.lineEdit_2.setMaxLength(10)
        #
        # # ввод пароля
        # self.ui.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        # # только чтение без изменения содержимого.
        # self.ui.lineEdit_4.setReadOnly(True)
        #
        # # меняем цвет вводимого текста
        # self.ui.lineEdit_5.setStyleSheet("color: rgb(28, 43, 255);")
        #
        # # изменение цвета фона QLineEdit
        # self.ui.lineEdit_6.setStyleSheet("background-color: rgb(28, 43, 255);")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())





# import sys
#
#
# class mywindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(mywindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#
# app = QtWidgets.QApplication([])
# application = mywindow()
# application.show()
#
# sys.exit(app.exec())