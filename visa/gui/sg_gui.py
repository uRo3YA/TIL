import sys
import pyvisa
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class SignalGeneratorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signal Generator Control")
        self.setGeometry(100, 100, 400, 200)
        
        self.init_ui()
        
        self.rm = pyvisa.ResourceManager()
        self.signal_generator = None
        self.data = []  # List to store frequency and amplitude data
        self.index = 0  # Index to track current data
        
    def init_ui(self):
        self.connect_btn = QPushButton("Connect", self)
        self.connect_btn.clicked.connect(self.connect_signal_generator)
        
        self.read_btn = QPushButton("Read Frequency and Amplitude", self)
        self.read_btn.clicked.connect(self.read_frequency_amplitude)
        self.read_btn.setEnabled(False)
        
        self.next_btn = QPushButton("Next", self)
        self.next_btn.clicked.connect(self.display_next)
        self.next_btn.setEnabled(False)
        
        self.frequency_label = QLabel("Frequency:")
        self.amplitude_label = QLabel("Amplitude:")
        
        layout = QVBoxLayout()
        layout.addWidget(self.connect_btn)
        layout.addWidget(self.read_btn)
        layout.addWidget(self.next_btn)
        layout.addWidget(self.frequency_label)
        layout.addWidget(self.amplitude_label)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
    def connect_signal_generator(self):
        try:
            resource_name = "YOUR_DEVICE_ADDRESS"  # Change this to your actual device address
            self.signal_generator = self.rm.open_resource(resource_name)
            self.read_btn.setEnabled(True)
            self.next_btn.setEnabled(True)
            print("Connected to the Signal Generator.")
        except Exception as e:
            print("Connection failed:", e)
    
    def read_frequency_amplitude(self):
        if self.signal_generator is not None:
            frequency = self.signal_generator.query(":FREQuency:CW?").strip()
            amplitude = self.signal_generator.query(":POWer:AMPLitude?").strip()
            
            self.data.append((frequency, amplitude))
            self.index = 0
            
            self.frequency_label.setText(f"Frequency: {frequency}")
            self.amplitude_label.setText(f"Amplitude: {amplitude}")
        else:
            print("Signal Generator not connected.")
            
    def display_next(self):
        if self.data and self.index < len(self.data):
            frequency, amplitude = self.data[self.index]
            self.frequency_label.setText(f"Frequency: {frequency}")
            self.amplitude_label.setText(f"Amplitude: {amplitude}")
            self.index += 1
        else:
            print("No more data to display.")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = SignalGeneratorGUI()
    gui.show()
    sys.exit(app.exec_())