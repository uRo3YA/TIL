import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyPDF2 import PdfMerger

class PDFMergerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Merger")
        self.setGeometry(100, 100, 400, 200)

        self.init_ui()

    def init_ui(self):
        self.btn_merge = QPushButton("Merge PDFs", self)
        self.btn_merge.setGeometry(150, 80, 100, 40)
        self.btn_merge.clicked.connect(self.merge_pdfs)

    def merge_pdfs(self):
        # 파일 선택 다이얼로그 열기
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("PDF files (*.pdf)")
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()

            # PDF 파일 병합
            merger = PdfMerger()
            for file_path in file_paths:
                merger.append(file_path)

            # 병합된 파일 저장 다이얼로그 열기
            save_dialog = QFileDialog()
            save_dialog.setAcceptMode(QFileDialog.AcceptSave)
            save_dialog.setDefaultSuffix("pdf")
            save_dialog.setNameFilter("PDF files (*.pdf)")
            if save_dialog.exec_():
                save_path = save_dialog.selectedFiles()[0]

                # 병합된 파일 저장
                merger.write(save_path)

                merger.close()

                print(f"PDFs merged successfully. Saved to: {save_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFMergerApp()
    window.show()
    sys.exit(app.exec_())