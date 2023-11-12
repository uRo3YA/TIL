# import pyvisa

# _host = '169.254.52.212'
# _port = 5000

# rm = pyvisa.ResourceManager('@py') # visa 객체를 생성합니다.
# print(rm.list_resources())
# # 지정한 HOST와 PORT를 사용하여 계측기에 접속합니다. 
# pna_client = rm.open_resource("TCPIP::192.168.110.22::INSTR")

# print (pna_client.query('*IDN?')) # 계측기 정보를 출력합니다.

# pna_client.write(f"HCOPy:SDUMp:DATA:FORMat PNG") # screenshot file format : PNG
# pna_client.write('HCOPy:SDUMp:DATA?') # PNA screenshot
# img = pna_client.read_raw() # 캡쳐된 바이너리 이미지 데이터 받기

# header_index = img.find(b'\x89PNG')
# if (header_index > 0): # find PNG header
#     img = img[header_index:]

# # 화면 캡쳐 파일 저장하기
# with open('pna.png', 'wb') as f:
#     f.write(img)
# pna_client.close()
# rm.close()
import sys
import PyQt5
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QLineEdit
from PyQt5.QtGui import QPixmap, QMovie
import pyvisa
import tkinter
import tkinter.filedialog as fd
import datetime
from PIL import Image, ImageOps
from os import environ 
import qdarkstyle
from PIL import ImageQt as PQ
from time import sleep
global flag
flag=True

def suppress_qt_warning():
    environ["QT_DEVICE_PIXEL_RATIO"]="0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"]="1"
    # environ["QT_SCREEN_SCALE_FACTORS"]="1"
    # environ["QT_SCALE_FACTOR"]="1"



#rm = pyvisa.ResourceManager()
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
        self.instr = self.rm.open_resource(resource_string,chunk_size=8000,timeout=20000)
        self.instr.timeout = 100000
        self.instr.write("*CLS")
        
    
    def get_identity(self):
        return self.query("*IDN?")

    def is_connected(self):
        return not self.instr is None

    def screenshot(self):
        self.instr.write(f"HCOPy:SDUMp:DATA:FORMat PNG") # screenshot file format : PNG
        self.instr.write('HCOPy:SDUMp:DATA?') # PNA screenshot
        img = self.instr.read_raw() # 캡쳐된 바이너리 이미지 데이터 받기

        root = tkinter.Tk()
        root.withdraw()
        today = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = fd.asksaveasfilename(filetypes=[("PNG", ".png")], initialfile=today, defaultextension="png")

        header_index = img.find(b'\x89PNG')
        if (header_index > 0): # find PNG header
            img = img[header_index:]
        # 화면 캡쳐 파일 저장하기
        with open(filename, 'wb') as f:
            f.write(img)
    
        print(filename)



class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.sa = PNA()

    def setupUi(self):
        
        #default_img=QPixmap('C:/Users/PC/Desktop/20231026_102158.gif')
        self.setWindowTitle('SCREEN SHOT')
        self.resize(640,480)

        self.IP_address_input = QLineEdit(self)
        self.IP_address_input.move(75,75)

        self.IP_label = QLabel(self)
        self.IP_label.move(75, 105)
        self.IP_label.setText('IP addr:')

        self.Device_Label=QLabel(self)
        self.Device_Label.move(75, 120)
        self.Device_Label.setText('Device Info:')

        # self.Freq_Label=QLabel(self)
        # self.Freq_Label.move(75, 135)
        # self.Freq_Label.setText('Center Freq:')
        
        # self.Freq_input=QLineEdit(self)
        # self.Freq_input.move(75, 150)
        
        self.screenshot_button = QPushButton(self)
        self.screenshot_button.move(75, 175)
        self.screenshot_button.setText('screenshot')
        self.screenshot_button.clicked.connect(self.screenshot_button_event)

        self.connect_button = QPushButton(self)
        self.connect_button.move(240, 78)
        self.connect_button.setText('Connect')
        self.connect_button.clicked.connect(self.connect_button_event)

        # self.set_Freq_button = QPushButton(self)
        # self.set_Freq_button.move(240, 155)
        # self.set_Freq_button.setText('set_Freq')
        # self.set_Freq_button.clicked.connect(self.set_Freq_button_event)

        self.snapshot_label = QLabel(self)
        #self.snapshot_label.setPixmap(default_img) # 이미지 세팅
        # self.snapshot_label.setText("HERE")
        self.snapshot_label.move(810,360)
        # # self.snapshot_label.setContentsMargins(10, 10, 10, 10)
        # self.marker_button = QPushButton(self)
        # # self.marker_label=QLabel(self)
        # self.marker_button.move(240, 175)
        # self.marker_button.setText('Marker')
        # self.marker_button.clicked.connect(self.marker_button_event)
       
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
            self.connect_button.adjustSize()
            self.IP_label.setText("IP addr: "+add)
            self.IP_label.adjustSize()
            self.Device_Label.setText("Device Info: "+device_info)
            self.Device_Label.adjustSize()

    def screenshot_button_event(self):
        snap_img=self.sa.screenshot()
        # pixmap = PQ.toqpixmap(snap_img)
        print(type(snap_img))
        qp = QPixmap()
        qp.loadFromData(snap_img)

    #     image = QPixmap(f'{snap_img}')
        
    #     # pixmap = QPixmap(image)    
    #     # print(type(snap_img))
        
        self.snapshot_label.setPixmap(qp)

    def marker_button_event(self):   
        out=self.sa.marker_search()
        print("마커 아웃2:",out)

    def set_Freq_button_event(self):
        text = self.Freq_input.text() 
        #self.sa.set_center_frequency()
        self.sa.set_center_frequency(text)
        self.Freq_Label.setText("Center Freq:"+text)
   
  
if __name__=="__main__":
    suppress_qt_warning()
    app = QApplication(sys.argv)
    
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
