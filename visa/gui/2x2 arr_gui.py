import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QButtonGroup, QLineEdit, QGroupBox,QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 전체 레이아웃
        main_layout = QVBoxLayout()

        # 첫 번째 그룹 레이아웃
        group1_box = QGroupBox('Group 1')
        group1_layout = QVBoxLayout(group1_box)
        radio_button1 = QRadioButton('Radio 1')
        radio_button2 = QRadioButton('Radio 2')

        # 라디오 버튼들을 그룹으로 묶어 서로 토글되게 함
        radio_group = QButtonGroup(self)
        radio_group.addButton(radio_button1)
        radio_group.addButton(radio_button2)

        group1_layout.addWidget(radio_button1)
        group1_layout.addWidget(radio_button2)

        # Connect 푸시 버튼 추가
        connect_button = QPushButton('Connect',self)
        connect_button.clicked.connect(self.on_connect_button_click)
        text_input1 = QLineEdit()
        

        group1_layout.addWidget(text_input1)
        group1_layout.addWidget(connect_button)
        

        # 두 번째 그룹 레이아웃
        group2_box = QGroupBox('Group 2')
        group2_layout = QVBoxLayout(group2_box)
        button3 = QPushButton('Button 3')
        button4 = QPushButton('Button 4')
        button5 = QPushButton('Button 5')

        group2_layout.addWidget(button3)
        # group2_layout.addWidget(button4)
        # group2_layout.addWidget(button5)
        perv_and_next_button_layout = QHBoxLayout()
        perv_and_next_button_layout.addWidget(button4)
        perv_and_next_button_layout.addWidget(button5)
        group2_layout.addLayout(perv_and_next_button_layout)
        # 세 번째 그룹 레이아웃
        group3_box = QGroupBox('Group 3')
        group3_layout = QVBoxLayout(group3_box)  # 수정된 부분
        feq_label=QLabel("주파수 : ")
        text_input3 = QLineEdit()
        text_input3.setFixedWidth(100)  # text_input3의 폭을 100으로 설정
        button6 = QPushButton('set')
        button6.setFixedWidth(40)  # button6의 폭을 100으로 설정

        # 텍스트 입력과 버튼을 양쪽 끝으로 정렬하는 수평 레이아웃
        text_input_and_button_layout = QHBoxLayout()
        text_input_and_button_layout.addWidget(feq_label)
        text_input_and_button_layout.addWidget(text_input3)
        text_input_and_button_layout.addStretch(2)  # 왼쪽에 빈 공간 추가
        text_input_and_button_layout.addWidget(button6)


        group3_layout.addLayout(text_input_and_button_layout)

        # 버튼7과 텍스트 입력7을 수평으로 배치
        amp_label=QLabel("Amp   :")
        text_input5 = QLineEdit()
        text_input5.setFixedWidth(100)
        button7 = QPushButton('set')
        button7.setFixedWidth(40)
        group3_and_button7_layout = QHBoxLayout()
        group3_and_button7_layout.addWidget(amp_label)
        group3_and_button7_layout.addWidget(text_input5)
        group3_and_button7_layout.addStretch(2)
        group3_and_button7_layout.addWidget(button7)

        group3_layout.addLayout(group3_and_button7_layout)

        # 버튼8과 텍스트 입력8을 수평으로 배치
        offset_label=QLabel("Offset : ")
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
                print(f'{radio_button.text()}이 선택되었습니다.')
                   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
