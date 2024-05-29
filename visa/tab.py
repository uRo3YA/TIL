import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt Tab Example')
        self.setGeometry(100, 100, 400, 300)

        # 탭 위젯 생성
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # 첫 번째 탭 생성
        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout()
        self.tab1_button = QPushButton('Tab 1 Button')
        self.tab1_button.clicked.connect(self.on_tab1_button_click)
        self.tab1_layout.addWidget(self.tab1_button)
        self.tab1.setLayout(self.tab1_layout)

        # 두 번째 탭 생성
        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout()
        self.tab2_button = QPushButton('Tab 2 Button')
        self.tab2_button.clicked.connect(self.on_tab2_button_click)
        self.tab2_layout.addWidget(self.tab2_button)
        self.tab2.setLayout(self.tab2_layout)

        # 탭 위젯에 탭 추가
        self.tabs.addTab(self.tab1, 'Tab 1')
        self.tabs.addTab(self.tab2, 'Tab 2')

    def on_tab1_button_click(self):
        QMessageBox.information(self, 'Tab 1', 'Tab 1 Button Clicked')

    def on_tab2_button_click(self):
        QMessageBox.information(self, 'Tab 2', 'Tab 2 Button Clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
