import sys
import pyvisa
import tkinter
import tkinter.filedialog as fd
import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QPushButton, QHBoxLayout, QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint

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



class MyGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PNA screen capture")
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()
        self.sa = PNA()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        group_box1 = QGroupBox("Group 1")
        layout.addWidget(group_box1)
        IP_address_input = QLineEdit()
        button1_3 = QPushButton("연결")
        group_layout1 = QVBoxLayout()
        layout1_3 = QHBoxLayout()
        layout1_3.addWidget(IP_address_input)
        layout1_3.addWidget(button1_3)
        layout1_4 = QHBoxLayout()
        IP_label = QLabel(self)
        IP_label.setText('연결 정보:')
        layout1_4.addWidget(IP_label)

        layout1_5 = QHBoxLayout()
        Device_Label = QLabel(self)
        Device_Label.setText('기기 정보:')
        layout1_5.addWidget(Device_Label)
        group_layout1.addLayout(layout1_3)
        group_layout1.addLayout(layout1_4)
        group_layout1.addLayout(layout1_5)
        group_box1.setLayout(group_layout1)


        group_box2 = QGroupBox("Group 2")
        layout.addWidget(group_box2)

        button2_1 = QPushButton("이미지 저장")

        group_layout2 = QVBoxLayout()
        group_layout2.addWidget(button2_1)
        group_box2.setLayout(group_layout2)



        group_box3 = QGroupBox("Group 3")
        layout.addWidget(group_box3)

        # Create a QPixmap with an arrow image
        pixmap = self.create_arrow_image(120, 120)

        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        
        group_layout3 = QVBoxLayout()
        group_layout3.addWidget(label)
        group_box3.setLayout(group_layout3)

    def create_arrow_image(self, width, height):
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.white)
        painter = QPainter(pixmap)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

        # Draw a simple arrow
        arrow_width = 20
        arrow_height = 40
        top_point = QPoint(width // 2, 10)
        bottom_point = QPoint(width // 2, height - 10)
        left_point = QPoint(width // 2 - arrow_width // 2, height - 10 - arrow_height)
        right_point = QPoint(width // 2 + arrow_width // 2, height - 10 - arrow_height)

        # Draw arrow lines
        painter.drawLine(top_point, bottom_point)
        painter.drawLine(left_point, bottom_point)
        painter.drawLine(right_point, bottom_point)

        painter.end()
        return pixmap

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MyGUI()
    gui.show()
    sys.exit(app.exec_())
