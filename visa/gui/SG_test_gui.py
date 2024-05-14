import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QButtonGroup, QLineEdit, QGroupBox, QLabel,QFileDialog
import pyvisa


class FatalInternalSignalGenerator(EnvironmentError):
    pass


class SignalGenerator:
    def __init__(self) :
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
            raise FatalInternalSignalGenerator from ex

    def write(self, command):
        try:
            self.instr.write("*CLS")
            self.instr.write(command)
            self.instr.write("*CLS")
        except Exception as ex:
            self.safe_close()
            raise FatalInternalSignalGenerator from ex
        
    def device_connect(self, resource_string,com_type):
        try:
            if com_type=="lan":
                self.safe_close()
                self.instr = self.rm.open_resource(resource_string,chunk_size=8000,timeout=20000)
                self.instr.timeout = 100000
                self.instr.write("*CLS")
            elif com_type=="serial":
                self.safe_close()
                self.instr = self.rm.open_resource(resource_string,chunk_size=8000,timeout=20000)
                self.instr.baud_rate = 9600  # 통신 속도
                self.instr.data_bits = 8    # 데이터 비트
                self.instr.parity = pyvisa.constants.Parity.none  # 패리티 비트 (없음)
                self.instr.stop_bits = pyvisa.constants.StopBits.one  # 정지 비트

            print( self.instr.write("*IDN?"))
        except Exception as ex:
            self.safe_close()
            raise FatalInternalSignalGenerator from ex

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.data = []
        self.current_row = 0

        self.initUI()
        self.SG=SignalGenerator()
    
    def load_csv_data(self, filename):
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 2:  # Ensure there are at least two columns
                    self.data.append((row[0], row[1]))


    def initUI(self):
        # 전체 레이아웃
        main_layout = QVBoxLayout()

        # 첫 번째 그룹 레이아웃
        group1_box = QGroupBox('Group 1')
        group1_layout = QVBoxLayout(group1_box)
        radio_button1 = QRadioButton('LAN')
        radio_button2 = QRadioButton('Serial')

        # 라디오 버튼들을 그룹으로 묶어 서로 토글되게 함
        radio_group = QButtonGroup(self)
        radio_group.addButton(radio_button1)
        radio_group.addButton(radio_button2)

        group1_layout.addWidget(radio_button1)
        group1_layout.addWidget(radio_button2)

        # Connect 푸시 버튼 추가
        connect_button = QPushButton('Connect',self)
        connect_button.clicked.connect(self.on_connect_button_click)
        self.text_input1 = QLineEdit()
        

        group1_layout.addWidget(self.text_input1)
        group1_layout.addWidget(connect_button)
        

        # 두 번째 그룹 레이아웃
        group2_box = QGroupBox('Group 2')
        group2_layout = QVBoxLayout(group2_box)
        button3 = QPushButton('Button 3',self)
        button4 = QPushButton('Button 4')
        button5 = QPushButton('Button 5')
        button3.clicked.connect(self.open_csv)
        button4.clicked.connect(self.prev_row)
        button5.clicked.connect(self.next_row)
        # group2_layout.addWidget(button4)
        # group2_layout.addWidget(button5)
        group2_label=QHBoxLayout()
        self.label_a = QLabel("hello")
        self.label_b = QLabel("olleh")
        group2_label.addWidget(self.label_a) 
        group2_label.addWidget(self.label_b)
        group2_layout.addLayout(group2_label)
        group2_layout.addWidget(button3)
        prev_and_next_button_layout = QHBoxLayout()
        prev_and_next_button_layout.addWidget(button4)
        prev_and_next_button_layout.addWidget(button5)
        group2_layout.addLayout(prev_and_next_button_layout)
        # 세 번째 그룹 레이아웃
        group3_box = QGroupBox('Group 3')
        group3_layout = QVBoxLayout(group3_box)  # 수정된 부분
        feq_label=QLabel("Freq    :")
        self.text_input3 = QLineEdit()
        self.text_input3.setFixedWidth(100)  # text_input3의 폭을 100으로 설정
        button6 = QPushButton('set')
        button6.setFixedWidth(40)  # button6의 폭을 100으로 설정

        # 텍스트 입력과 버튼을 양쪽 끝으로 정렬하는 수평 레이아웃
        text_input_and_button_layout = QHBoxLayout()
        text_input_and_button_layout.addWidget(feq_label)
        text_input_and_button_layout.addWidget(self.text_input3)
        text_input_and_button_layout.addStretch(2)  # 왼쪽에 빈 공간 추가
        text_input_and_button_layout.addWidget(button6)


        group3_layout.addLayout(text_input_and_button_layout)

        # 버튼7과 텍스트 입력7을 수평으로 배치
        amp_label=QLabel("Amp    :")
        self.text_input5 = QLineEdit()
        self.text_input5.setFixedWidth(100)
        button7 = QPushButton('set')
        button7.setFixedWidth(40)
        group3_and_button7_layout = QHBoxLayout()
        group3_and_button7_layout.addWidget(amp_label)
        group3_and_button7_layout.addWidget(self.text_input5)
        group3_and_button7_layout.addStretch(2)
        group3_and_button7_layout.addWidget(button7)

        group3_layout.addLayout(group3_and_button7_layout)

        # 버튼8과 텍스트 입력8을 수평으로 배치
        offset_label=QLabel("Offset  :")
        text_input6 = QLineEdit()
        text_input6.setFixedWidth(100)
        button8 = QPushButton('set')
        button8.setFixedWidth(40)
        group3_and_button8_layout = QHBoxLayout()
        group3_and_button8_layout.addWidget(offset_label)
        group3_and_button8_layout.addWidget(text_input6)
        group3_and_button8_layout.addStretch(2)
        group3_and_button8_layout.addWidget(button8)

        group3_layout.addLayout(group3_and_button8_layout)

        # 네 번째 그룹 레이아웃
        group4_box = QGroupBox('Group 4')
        group4_layout = QVBoxLayout(group4_box)  # 수정된 부분
        button9 = QPushButton('Button 9')
        button10 = QPushButton('Button 10')
        button11 = QPushButton('Button 11')

        group4_layout.addWidget(button9)
        group4_layout.addWidget(button10)
        group4_layout.addWidget(button11)

        # 그룹3_layout과 그룹4_layout을 수평으로 결합
        group3_and_group4_layout = QHBoxLayout()
        group3_and_group4_layout.addWidget(group3_box, stretch=1)  # group3_box가 늘어날 수 있도록 stretch 추가
        group3_and_group4_layout.addWidget(group4_box, stretch=1)  # group4_box가 늘어날 수 있도록 stretch 추가

        # 그룹1_box와 그룹2_box를 수평으로 결합
        group1_and_group2_layout = QHBoxLayout()
        group1_and_group2_layout.addWidget(group1_box, stretch=1)  # group1_box가 늘어날 수 있도록 stretch 추가
        group1_and_group2_layout.addWidget(group2_box, stretch=1)  # group2_box가 늘어날 수 있도록 stretch 추가

        # 그룹 레이아웃들을 전체 레이아웃에 추가
        main_layout.addLayout(group1_and_group2_layout)
        main_layout.addLayout(group3_and_group4_layout)  # 수정된 부분

        self.setLayout(main_layout)

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('2x2 Group Layout')
        self.show()

    def on_connect_button_click(self):

        for radio_button in self.findChildren(QRadioButton):
            if radio_button.isChecked():
                
                if radio_button.text()=="LAN":
                    com_tpye="lan"
                    add=self.text_input1.text()
                    add=f"TCPIP::{add}::INSTR"
                    # print(add)
                    self.SG.device_connect(add,com_tpye)

                elif radio_button.text()=="Serial":
                    com_tpye="serial"
                    add=self.text_input1.text()
                    add=f"{add}::INSTR"
                    # print(add)
                    self.SG.device_connect(add,com_tpye)
                else : 
                    None



    def open_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        
        if file_name:
            self.data = []
            self.load_csv_data(file_name)
            self.current_row = 0
            self.display_row(self.current_row)

    def display_row(self, row_idx):
        if 0 <= row_idx < len(self.data):
            self.text_input3.setText(self.data[row_idx][0])
            self.text_input5.setText(self.data[row_idx][1])


    def prev_row(self):
        if self.current_row <= len(self.data) - 1:
            self.current_row -= 1
            self.display_row(self.current_row)
    
    def next_row(self):
        if self.current_row < len(self.data) - 1:
            self.current_row += 1
            self.display_row(self.current_row)
#######################################################################################
    def frequency_set(self):
        return None
    def amplitude_set(self):
        return None
    def offset_set(self):
        return None 
########################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
