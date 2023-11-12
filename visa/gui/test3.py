import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QPushButton, QHBoxLayout, QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint

class MyGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 GroupBox Example")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        group_box1 = QGroupBox("Group 1")
        layout.addWidget(group_box1)

        button1_1 = QPushButton("Button 1")
        button1_2 = QPushButton("Button 2")
        button1_3 = QPushButton("Button 3")

        group_layout1 = QVBoxLayout()
        group_layout1.addWidget(button1_1)
        group_layout1.addWidget(button1_2)
        group_layout1.addWidget(button1_3)
        group_box1.setLayout(group_layout1)

        group_box2 = QGroupBox("Group 2")
        layout.addWidget(group_box2)

        # Create QLineEdit widgets and QPushButton widgets for each button in Group 2
        input2_1 = QLineEdit()
        button2_1 = QPushButton("Button 1")
        input2_2 = QLineEdit()
        button2_2 = QPushButton("Button 2")
        input2_3 = QLineEdit()
        button2_3 = QPushButton("Button 3")

        group_layout2 = QVBoxLayout()
        layout2_1 = QHBoxLayout()
        layout2_1.addWidget(input2_1)
        layout2_1.addWidget(button2_1)
        layout2_2 = QHBoxLayout()
        layout2_2.addWidget(input2_2)
        layout2_2.addWidget(button2_2)
        layout2_3 = QHBoxLayout()
        layout2_3.addWidget(input2_3)
        layout2_3.addWidget(button2_3)
        group_layout2.addLayout(layout2_1)
        group_layout2.addLayout(layout2_2)
        group_layout2.addLayout(layout2_3)
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
