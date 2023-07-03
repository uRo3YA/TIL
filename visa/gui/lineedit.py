import sys
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QLineEdit
import pyvisa
import tkinter
import tkinter.filedialog as fd
import datetime
from PIL import Image, ImageOps

rm = pyvisa.ResourceManager()




class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('LineEdit')
        self.resize(1280,720)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(75,75)

        self.text_label = QLabel(self)
        self.text_label.move(75, 105)
        self.text_label.setText('hello. world')

        self.con_button = QPushButton(self)
        self.con_button.move(75, 175)
        self.con_button.setText('save')
        self.con_button.clicked.connect(self.save_button_event)

        self.save_button = QPushButton(self)
        self.save_button.move(240, 73)
        self.save_button.setText('connet')
        self.save_button.clicked.connect(self.con_button_event)

        self.show()

    def con_button_event(self):
        text = self.line_edit.text() # line_edit text 값 가져오기
        add=f"TCPIP::{text}::INSTR"
        # inst_1 = rm.open_resource(add)            
        self.text_label.setText(add) # label에 text 설정하기
        self.text_label.adjustSize()

    # def save_button_event(self):
    #     inst_1.write(":MMEM:STOR:SCR 'R:PICTURE.GIF'")
    #     capture = inst_1.query_binary_values(message=":MMEM:DATA? 'R:PICTURE.GIF'", container=list, datatype='c')

if __name__=="__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()

    sys.exit(app.exec_())