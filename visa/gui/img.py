import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.resize(400,400)   # 이미지를 보여주기 위해 출력될 label의 크기를 400×400으로 설정
        pixmap = QPixmap("images\default_img.jpg")
        self.lbl.setPixmap(QPixmap(pixmap))

        self.resize(400,400)   # 이미지를 보여주기 위해 출력될 창의 크기를 400×400으로 설정
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = test()
    sys.exit(app.exec_())