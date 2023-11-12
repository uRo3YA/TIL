import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from PyQt5.QtCore import Qt
from qt_material import apply_stylesheet

class MaterialDesignApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Material Design Example')
        self.setGeometry(100, 100, 400, 300)

        # 스타일 시트를 적용
        apply_stylesheet(self, theme='dark_black.xml')  # 검은색 테마 적용

        # 툴바 생성
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # 툴바에 액션 추가
        action = QAction('Material Design Action', self)
        toolbar.addAction(action)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MaterialDesignApp()
    window.show()
    sys.exit(app.exec_())
