import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.AddButton = QPushButton("File Open")
        self.AddButton.clicked.connect(self.AddButtonClicked)
        self.label = QLabel()

        ConvertButton = QPushButton('Convert')

        width_layout = QVBoxLayout()
        width_layout.addStretch(20)
        width_layout.addWidget(self.AddButton)
        width_layout.addStretch(20)
        width_layout.addWidget(ConvertButton)
        width_layout.addStretch(1)

        height_layout = QHBoxLayout()
        height_layout.addWidget(self.label)
        height_layout.addStretch(50)
        height_layout.addLayout(width_layout)
        height_layout.addStretch(1)

        self.setLayout(height_layout)


        self.setWindowTitle('쎈놈')
        self.setWindowIcon(QIcon('web.png'))
        self.resize(500, 200)
        self.center()
        self.show()

    def AddButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())