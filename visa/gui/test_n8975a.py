import sys
import pyvisa
import tkinter
import tkinter.filedialog as fd
import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QPushButton, QHBoxLayout, QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class FatalInternalPNA(EnvironmentError):
    pass

class PNA:
    def __init__(self):
        self.rm = pyvisa.ResourceManager('@py')
        self.instr = None
        resources = self.rm.list_resources('?*')
        print(resources)
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
            raise FatalInternalPNA from ex
       
    def write(self, command):
        try:
            self.instr.write("*CLS")
            self.instr.write(command)
            self.instr.write("*CLS")
        except Exception as ex:
            self.safe_close()
            raise FatalInternalPNA from ex
        
    def device_connect(self, resource_string):
        self.safe_close()
        self.safe_close()
        self.instr = self.rm.open_resource(resource_string)
        self.instr.baud_rate = 9600  # 통신 속도
        self.instr.data_bits = 8    # 데이터 비트
        self.instr.parity = pyvisa.constants.Parity.none  # 패리티 비트 (없음)
        self.instr.stop_bits = pyvisa.constants.StopBits.one  # 정지 비트
        idn=self.query("*IDN?")
        idn=list(idn.split(","))
        # idn=self.instr.read()
        return None
    
    def get_identity(self):
        idn=self.query("*IDN?")
        idn=list(idn.split(","))
        return idn[1] 

    def is_connected(self):
        return not self.instr is None

    def screenshot(self):
        self.instr.write(":MMEM:STOR:SCR 'R:PICTURE.GIF'")
        capture = self.instr.query_binary_values(message=":MMEM:DATA? 'R:PICTURE.GIF'",datatype='B',container=bytearray)
        # self.instr.write(f"HCOPy:SDUMp:DATA:FORMat PNG") # screenshot file format : PNG
        # self.instr.write('HCOPy:SDUMp:DATA?') # PNA screenshot
        # img = self.instr.read_raw() # 캡쳐된 바이너리 이미지 데이터 받기

        root = tkinter.Tk()
        root.withdraw()
        today = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = fd.asksaveasfilename(filetypes=[("GIF", ".gif")], initialfile=today, defaultextension="gif")

        header_index = capture.find(b'GIF')
        if (header_index > 0): # find PNG header
            img = img[header_index:]
        # 화면 캡쳐 파일 저장하기
        with open(filename, 'wb') as f:
            f.write(img)
    
        return filename

  


class MyGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PNA capture")
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()
        self.sa = PNA()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        group_box1 = QGroupBox("Group 1")
        layout.addWidget(group_box1)
        self.IP_address_input = QLineEdit()
        self.IP_address_input.setText("ASRL3")
        self.button1_3 = QPushButton("연결")
        self.button1_3.clicked.connect(self.connect_button_event)
        group_layout1 = QVBoxLayout()
        layout1_3 = QHBoxLayout()
        layout1_3.addWidget(self.IP_address_input)
        layout1_3.addWidget(self.button1_3)
        layout1_4 = QHBoxLayout()
        self.IP_label = QLabel(self)
        self.IP_label.setText('연결 정보:')
        layout1_4.addWidget(self.IP_label)

        layout1_5 = QHBoxLayout()
        self.Device_Label = QLabel(self)
        self.Device_Label.setText('기기 정보:')
        layout1_5.addWidget(self.Device_Label)
        group_layout1.addLayout(layout1_3)
        group_layout1.addLayout(layout1_4)
        group_layout1.addLayout(layout1_5)
        group_box1.setLayout(group_layout1)


        group_box2 = QGroupBox("Group 2")
        layout.addWidget(group_box2)

        self.button2_1 = QPushButton("이미지 저장")
        self.button2_1.clicked.connect(self.screenshot_button_event) 

        group_layout2 = QVBoxLayout()
        group_layout2.addWidget(self.button2_1)
        group_box2.setLayout(group_layout2)



        group_box3 = QGroupBox("Group 3")
        layout.addWidget(group_box3)


        
        group_layout3 = QVBoxLayout()
        group_box3.setLayout(group_layout3)

    def connect_button_event(self):
        text = self.IP_address_input.text() 
        add=f"{text}::INSTR"
        if self.sa.is_connected():
            self.disconnect()
            self.button1_3.setText("Connect")
        else:
            self.sa.device_connect(add)
            # device_info=self.sa.get_identity()
            self.button1_3.setText("Disconnect")
            self.button1_3.adjustSize()
            self.IP_label.setText("연결 정보: "+add)
            self.IP_label.adjustSize()
            # self.Device_Label.setText("기기 정보: "+device_info)
            self.Device_Label.adjustSize()  
    
    def screenshot_button_event(self):
        snap_img=self.sa.screenshot()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MyGUI()
    gui.show()
    sys.exit(app.exec_())