import sys
import PyQt5
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QLineEdit,QVBoxLayout,QGroupBox
from PyQt5.QtGui import QPixmap
import pyvisa
import tkinter
import tkinter.filedialog as fd
import datetime
from PIL import Image, ImageOps
import os
import qdarkstyle
global flag
flag=True

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

    # def query_binary_values(self):
    #     try:
    #         self.instr.write("*CLS")
    #         result = self.instr.query_binary_values(":WAVeform:DATA?", 
    #                                         datatype='H', 
    #                                         is_big_endian=False,
    #                                         expect_termination=True)
    #         self.instr.write("*CLS")
    #         return result
    #     except Exception as ex:
    #         self.safe_close()
    #         raise FatalInternalSpectrumanalyzer from ex
        
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
        self.instr = self.rm.open_resource(resource_string,chunk_size=8000,timeout=20000)
        self.instr.timeout = 100000
        self.instr.write("*CLS")
        self.instr.write("*IDN?")
    
    def get_identity(self):
        return self.query("*IDN?")

    def is_connected(self):
        return not self.instr is None

    def set_center_frequency(self):
    # def set_center_frequency(self,cf):
        self.instr.write("*CLS")
        self.instr.write(":SENS:FREQ:CENT 3.4e8")
        # self.instr.write(f":SENS:FREQ:CENT {cf}")



    def screenshot(self):
        # self.instr.timeout = 100000
        self.instr.write(":MMEM:STOR:SCR 'R:PICTURE.GIF'")
        # self.instr.write(":MMEM:DATA? 'R:PICTURE.GIF'")
        # data = self.instr.read_raw()
        #capture = self.instr.query_binary_values(message=":MMEM:DATA? 'R:PICTURE.GIF'", container=list, datatype='c')
        capture = self.instr.query_binary_values(message=":MMEM:DATA? 'R:PICTURE.GIF'",datatype='B',container=bytearray
                                                 ,is_big_endian=False, expect_termination=True)
        root = tkinter.Tk()
        root.withdraw()
        today = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = fd.asksaveasfilename(filetypes=[("GIF", ".gif")], initialfile=today, defaultextension="gif")
        # with open(filename, 'wb') as fp:
        #     for byte in capture:
        #         fp.write(byte)
        with open(filename, 'wb') as fp:
            fp.write(capture)
        snapshot=Image.open(filename)
        snapshot.save(filename, 'gif')
        self.instr.write(":MMEM:DEL 'R:PICTURE.GIF'")
        self.instr.write("*CLS")
        return snapshot
        

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
        # default_img=QPixmap('visa\gui\images\default_img.jpg')
        
        self.setWindowTitle('SCREEN SHOT')
        self.resize(1280,720)

        main_layout = QVBoxLayout()
        groupbox_1 = QGroupBox("group_1")
        layout_1 = QVBoxLayout()
        
        self.IP_address_input = QLineEdit(self)
        self.IP_address_input.move(75,75)

        self.IP_label = QLabel(self)
        self.IP_label.move(75, 105)
        self.IP_label.setText('IP addr:')
        layout_1.addWidget(self.IP_address_input)
        layout_1.addWidget(self.IP_label)

        self.Device_Label=QLabel(self)
        self.Device_Label.move(75, 120)
        self.Device_Label.setText('Device Info:')

        self.Freq_Label=QLabel(self)
        self.Freq_Label.move(75, 135)
        self.Freq_Label.setText('Center Freq:')
        
        self.Freq_input=QLineEdit(self)
        self.Freq_input.move(75, 150)
        
        self.screenshot_button = QPushButton(self)
        self.screenshot_button.move(75, 175)
        self.screenshot_button.setText('screenshot')
        self.screenshot_button.clicked.connect(self.screenshot_button_event)

        self.connect_button = QPushButton(self)
        self.connect_button.move(240, 73)
        self.connect_button.setText('Connect')
        self.connect_button.clicked.connect(self.connect_button_event)

        self.set_Freq_button = QPushButton(self)
        self.set_Freq_button.move(240, 148)
        self.set_Freq_button.setText('set_Freq')
        self.set_Freq_button.clicked.connect(self.set_Freq_button_event)

        self.snapshot_label = QLabel(self)
        # self.snapshot_label.setPixmap(default_img) # 이미지 세팅
        # self.snapshot_label.setText("HERE")
        self.snapshot_label.move( 810,360)
        # self.snapshot_label.setContentsMargins(10, 10, 10, 10)
        

        # self.img_button=QPushButton(self)
        # self.img_button.move(810,340)
        # self.img_button.setText('image change')
        
        # self.img_button.clicked.connect(self.img_button_event)
        self.show()

    def connect_button_event(self):
        text = self.IP_address_input.text() 
        add=f"TCPIP::{text}::INSTR"
        if self.sa.is_connected():
            self.disconnect()
            self.connect_button.setText("Connect")
        else:
            self.sa.device_connect(add)
            device_info=self.sa.get_identity()
            self.connect_button.setText("Disconnect")
            self.IP_label.setText("IP addr: "+add)
            self.IP_label.adjustSize()
            self.Device_Label.setText("Device Info: "+device_info)
            self.Device_Label.adjustSize()

    def screenshot_button_event(self):
        snap_img=self.sa.screenshot()
        # self.snapshot_label.setPixmap(snap_img)

    def set_Freq_button_event(self):
        text = self.Freq_input.text() 
        self.sa.set_center_frequency()
        #self.sa.set_center_frequency(text)
        self.Freq_Label.setText("Center Freq:"+text)
   
  
if __name__=="__main__":
    app = QApplication(sys.argv)
    
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
