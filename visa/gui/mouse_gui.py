import time
import pyautogui
import pytesseract
from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap

# 좌표 리스트
click_coordinates = [(100, 100), (200, 200), (300, 300), (400, 400)]

class ClickTracker(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 300, 100)
        self.setWindowTitle('Click Coordinate Tracker')

        self.position_label = QLabel(self)
        self.position_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(self.position_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_click_position)
        self.timer.start(1000)

    def update_click_position(self):
        cursor_position = pyautogui.position()
        position_text = f'Last Clicked Position: X={cursor_position.x()}, Y={cursor_position.y()}'
        self.position_label.setText(position_text)

def perform_clicks(coordinates):
    for coord in coordinates:
        pyautogui.click(coord[0], coord[1])
        time.sleep(5)

def perform_ocr():
    screenshot = ImageGrab.grab()
    text = pytesseract.image_to_string(screenshot)
    return text

if __name__ == "__main__":
    app = QApplication([])
    tracker = ClickTracker()
    tracker.show()

    perform_clicks(click_coordinates)
    time.sleep(5)

    recognized_text = perform_ocr()

    print("Recognized Text:")
    print(recognized_text)

    app.exec_()
