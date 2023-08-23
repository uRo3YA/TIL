import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog, QHBoxLayout, QFormLayout, QGroupBox, QGridLayout, QTextEdit, QScrollArea
from PyQt5.QtGui import QPixmap
import pyvisa as visa

class SpectrumAnalyzerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Keysight Spectrum Analyzer Control')
        self.setGeometry(100, 100, 1000, 600)

        layout = QGridLayout()

        # Input box for TCP/IP connection
        self.ip_address_label = QLabel('Enter Spectrum Analyzer IP Address:')
        self.ip_address_input = QLineEdit(self)
        self.ip_address_input.setPlaceholderText('e.g., 192.168.1.100')
        layout.addWidget(self.ip_address_label, 0, 0)
        layout.addWidget(self.ip_address_input, 0, 1)

        # Connect button
        self.connect_button = QPushButton('Connect', self)
        self.connect_button.clicked.connect(self.connect_to_analyzer)
        layout.addWidget(self.connect_button, 0, 2)

        # Screenshot display area
        self.screenshot_label = QLabel(self)
        self.screenshot_label.setMinimumSize(400, 300)
        layout.addWidget(self.screenshot_label, 1, 0, 3, 1)

        # Create a group box for the marker settings
        marker_group_box = QGroupBox('Marker Settings')
        marker_layout = QFormLayout()

        # Center frequency input box
        self.center_frequency_input = QLineEdit(self)
        self.center_frequency_input.setPlaceholderText('Enter Center Frequency (Hz)')
        marker_layout.addRow('Center Frequency:', self.center_frequency_input)

        # Set Marker button
        self.marker_button = QPushButton('Set Marker', self)
        self.marker_button.clicked.connect(self.set_marker)
        marker_layout.addWidget(self.marker_button)

        # Frequency offset input box
        self.offset_input = QLineEdit(self)
        self.offset_input.setPlaceholderText('Enter Frequency Offset (Hz)')
        marker_layout.addRow('Frequency Offset:', self.offset_input)

        # Span input box
        self.span_input = QLineEdit(self)
        self.span_input.setPlaceholderText('Enter Span (Hz)')
        marker_layout.addRow('Span:', self.span_input)

        # Set Delta Marker button
        self.delta_marker_button = QPushButton('Set Delta Marker', self)
        self.delta_marker_button.clicked.connect(self.set_delta_marker)
        layout.addWidget(self.delta_marker_button, 1, 2)

        # Add marker layout to the marker group box
        marker_group_box.setLayout(marker_layout)
        layout.addWidget(marker_group_box, 1, 1)

        # Capture Screenshot button
        self.image_button = QPushButton('Capture Screenshot', self)
        self.image_button.clicked.connect(self.save_screenshot)
        layout.addWidget(self.image_button, 4, 0, 1, 3)

        # Log area
        self.log_text_edit = QTextEdit(self)
        self.log_text_edit.setReadOnly(True)
        scroll_area = QScrollArea(self)
        scroll_area.setWidget(self.log_text_edit)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area, 5, 0, 1, 3)

        self.setLayout(layout)

        self.spectrum_analyzer = None

    def connect_to_analyzer(self):
        try:
            rm = visa.ResourceManager()
            ip_address = self.ip_address_input.text()
            self.spectrum_analyzer = rm.open_resource(f'TCPIP::{ip_address}::INSTR')
            self.log('Connected to the Spectrum Analyzer.')
        except visa.VisaIOError as e:
            self.log(f"Error connecting to the Spectrum Analyzer: {e}")
            self.spectrum_analyzer = None

    def log(self, message):
        self.log_text_edit.append(message)

    def save_screenshot(self):
        if self.spectrum_analyzer:
            file_path, _ = QFileDialog.getSaveFileName(self, 'Save Screenshot', '', 'PNG Images (*.png);;All Files (*)')
            if file_path:
                screenshot_data = self.spectrum_analyzer.query_binary_values(':DISP:DATA:SDAT?', datatype='B', container=bytes)
                with open(file_path, 'wb') as file:
                    file.write(screenshot_data)
                self.log(f"Screenshot saved to {file_path}")
                pixmap = QPixmap(file_path)
                self.screenshot_label.setPixmap(pixmap.scaled(400, 300))

    def set_marker(self):
        if self.spectrum_analyzer:
            try:
                frequency = float(self.center_frequency_input.text())
                marker_value = self._set_marker(frequency)
                if marker_value is not None:
                    self.log(f"Marker frequency: {frequency} Hz, Amplitude: {marker_value} dBm")
            except ValueError:
                self.log("Invalid input for center frequency.")
        
    def _set_marker(self, frequency):
        try:
            self.spectrum_analyzer.write(f':CALCulate:MARKer:X {frequency}Hz')
            marker_value = self.spectrum_analyzer.query(':CALCulate:MARKer:Y?')
            return float(marker_value)
        except visa.VisaIOError as e:
            self.log(f"Error setting marker: {e}")
            return None

    def set_delta_marker(self):
        if self.spectrum_analyzer:
            try:
                center_frequency = float(self.center_frequency_input.text())
                offset = float(self.offset_input.text())
                span = float(self.span_input.text())
                marker_value = self._set_delta_marker(center_frequency, offset)
                if marker_value is not None:
                    self.log(f"Delta Marker at Frequency: {center_frequency + offset} Hz, Amplitude: {marker_value} dBm")
            except ValueError:
                self.log("Invalid input for center frequency, offset, or span.")
        
    def _set_delta_marker(self, center_frequency, offset):
        try:
            self.spectrum_analyzer.write(f':FREQuency:CENTer {center_frequency}Hz')
            self.spectrum_analyzer.write(f':DISP:WIND:TRAC:X:OFFS {offset}Hz')
            marker_value = self.spectrum_analyzer.query(':CALCulate:MARKer:Y?')
            return float(marker_value)
        except visa.VisaIOError as e:
            self.log(f"Error setting delta marker: {e}")
            return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpectrumAnalyzerGUI()
    window.show()
    sys.exit(app.exec_())
