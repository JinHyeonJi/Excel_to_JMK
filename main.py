import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("untitled_ui.ui")[0]


class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addbutton.clicked.connect(self.add_clicked)

    def add_clicked(self):
        file_names = QFileDialog.getOpenFileNames(self)

        for file in file_names[0]:
            exist = self.textEdit.toPlainText()
            self.textEdit.setText(exist + file + '\n')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()