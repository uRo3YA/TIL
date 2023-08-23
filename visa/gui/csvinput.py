import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog

class CSVReaderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.data = []  # List to store the data from the CSV file
        self.current_row = 0  # Index of the currently displayed row

        self.init_ui()

    def load_csv_data(self, filename):
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 2:  # Ensure there are at least two columns
                    self.data.append((row[0], row[1]))

    def init_ui(self):
        self.setWindowTitle("CSV Reader")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.label_a = QLabel()
        self.label_b = QLabel()

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_row)

        self.open_button = QPushButton("Open CSV")
        self.open_button.clicked.connect(self.open_csv)

        layout = QVBoxLayout()
        layout.addWidget(self.label_a)
        layout.addWidget(self.label_b)
        layout.addWidget(self.next_button)
        layout.addWidget(self.open_button)

        self.central_widget.setLayout(layout)

    def display_row(self, row_idx):
        if 0 <= row_idx < len(self.data):
            self.label_a.setText("Acol: " + self.data[row_idx][0])
            self.label_b.setText("Bcol: " + self.data[row_idx][1])

    def next_row(self):
        if self.current_row < len(self.data) - 1:
            self.current_row += 1
            self.display_row(self.current_row)

    def open_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        
        if file_name:
            self.data = []
            self.load_csv_data(file_name)
            self.current_row = 0
            self.display_row(self.current_row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CSVReaderApp()
    window.show()
    sys.exit(app.exec_())
