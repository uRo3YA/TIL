import sys
import PyQt5
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QLineEdit
import pyvisa
import tkinter
import tkinter.filedialog as fd
import datetime
from PIL import Image, ImageOps
import os

#rm = pyvisa.ResourceManager()
class FatalInternalSpectrumanalyzer(EnvironmentError):
    pass

class Spectrumanalyzer:
    def __init__(self):
        self.rm = pyvisa.ResourceManager('@py')
        self.instr = None
        
    def safe_close(self):
        if not self.instr is None:
            try:
                self.instr.close()
            finally:
                self.instr = None
    def query(self, command):
        try:
            self.instr.write("*CLS")
            result = self.instr.query(command)[:-1]
            self.instr.write("*CLS")
            return result
        except Exception as ex:
            self.safe_close()
            raise FatalInternalSpectrumanalyzer from ex
        
    def write(self, command):
        try:
            self.instr.write("*CLS")
            self.instr.write(command)
            self.instr.write("*CLS")
        except Exception as ex:
            self.safe_close()
            raise FatalInternalSpectrumanalyzer from ex
    def device_connect(self, resource_string):
        self.safe_close()
        self.instr = self.rm.open_resource(resource_string)
        self.instr.timeout = 1000
        self.instr.write("*CLS")
        self.instr.write("*IDN?")
    
    def get_identity(self):
        return self.query("*IDN?")

    def is_connected(self):
        return not self.instr is None

    def screenshot(self):
        self.instr.timeout = 100000 
        self.instr.write(":MMEM:STOR:SCR 'R:PICTURE.GIF'")
        capture = self.query_binary_values(message=":MMEM:DATA? 'R:PICTURE.GIF'", container=list, datatype='c')
        root = tkinter.Tk()
        root.withdraw()
        today = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = fd.asksaveasfilename(filetypes=[("GIF", ".gif")], initialfile=today, defaultextension="gif")
        with open(filename, 'wb') as fp:
            for byte in capture:
                fp.write(byte)
        snapshot=Image.open(filename)
        snapshot.save(filename, 'gif')
        self.instr.write(":MMEM:DEL 'R:PICTURE.GIF'")
        self.instr.close()
        

# def con_device(add):
#     inst_1 = rm.open_resource(add) 
#     state=inst_1.query('*IDN?')
#     return state


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.sa = Spectrumanalyzer()

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

    # def con_button_event(self):
    #     text = self.line_edit.text() # line_edit text 값 가져오기
    #     add=f"TCPIP::{text}::INSTR"
    #     con_msg=con_device(add)
    #     try:
    #        self.text_label.setText(con_msg)
    #     except:
    #         self.text_label.setText("COM ERR")
    #     # inst_1 = rm.open_resource(add)            
    #     # self.text_label.setText(add) # label에 text 설정하기
    #     self.text_label.adjustSize()
    def con_button_event(self):
        text = self.line_edit.text() # line_edit text 값 가져오기
        add=f"TCPIP::{text}::INSTR"
        if self.sa.is_connected():
            self.disconnect()
        else:
            self.sa.device_connect(add)
            data=self.sa.get_identity()
            print(data)
            self.text_label.setText(add)
            self.text_label.adjustSize()

    def save_button_event(self):
        data=self.sa.get_identity()
        print(data)
        self.sa.screenshot()


if __name__=="__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()

    sys.exit(app.exec_())
