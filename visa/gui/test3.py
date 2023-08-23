import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog, QHBoxLayout, QFormLayout, QGroupBox, QGridLayout, QTextEdit, QScrollArea, QTabWidget, QComboBox
from PyQt5.QtGui import QPixmap
import pyvisa as visa

class SpectrumAnalyzerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Keysight Spectrum Analyzer and Signal Generator Control')
        self.setGeometry(100, 100, 1000, 600)

        main_layout = QVBoxLayout()

        # Create a tab widget
        self.tab_widget = QTabWidget(self)
        main_layout.addWidget(self.tab_widget)

        # Create tabs
        spectrum_analyzer_tab = SpectrumAnalyzerTab()
        signal_generator_tab = SignalGeneratorTab()

        # Add tabs to the tab widget
        self.tab_widget.addTab(spectrum_analyzer_tab, "Spectrum Analyzer")
        self.tab_widget.addTab(signal_generator_tab, "Signal Generator")

        self.setLayout(main_layout)

class SpectrumAnalyzerTab(QWidget):
    def __init__(self):
        super().__init__()
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

        # ... (Add the rest of the Spectrum Analyzer GUI components and functionalities here)

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

class SignalGeneratorTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()

        # Input box for TCP/IP connection
        self.signal_generator_ip_label = QLabel('Enter Signal Generator IP Address:')
        self.signal_generator_ip_input = QLineEdit(self)
        self.signal_generator_ip_input.setPlaceholderText('e.g., 192.168.1.101')
        layout.addRow(self.signal_generator_ip_label, self.signal_generator_ip_input)

        # Connect button
        self.connect_signal_generator_button = QPushButton('Connect Signal Generator', self)
        self.connect_signal_generator_button.clicked.connect(self.connect_to_signal_generator)
        layout.addWidget(self.connect_signal_generator_button)

        # Frequency input box
        self.frequency_input = QLineEdit(self)
        self.frequency_input.setPlaceholderText('Enter Frequency (Hz)')
        layout.addRow('Frequency:', self.frequency_input)

        # Amplitude input box
        self.amplitude_input = QLineEdit(self)
        self.amplitude_input.setPlaceholderText('Enter Amplitude (dBm)')
        layout.addRow('Amplitude:', self.amplitude_input)

        # Waveform selection
        self.waveform_label = QLabel('Select Waveform:')
        self.waveform_combo_box = QComboBox(self)
        self.waveform_combo_box.addItems(['Sine', 'Square', 'Triangle', 'Ramp'])
        layout.addRow(self.waveform_label, self.waveform_combo_box)

        # Apply settings button
        self.apply_settings_button = QPushButton('Apply Settings', self)
        self.apply_settings_button.clicked.connect(self.apply_signal_generator_settings)
        layout.addWidget(self.apply_settings_button)

        # ... (Add the rest of the Signal Generator GUI components and functionalities here)

        self.signal_generator = None

    def connect_to_signal_generator(self):
        try:
            ip_address = self.signal_generator_ip_input.text()
            # Add code to connect to the Signal Generator using pyvisa
            # self.signal_generator = visa.ResourceManager().open_resource(f'TCPIP::{ip_address}::INSTR')
            print(f"Connected to Signal Generator at IP: {ip_address}")
        except Exception as e:
            print(f"Error connecting to Signal Generator: {e}")
            self.signal_generator = None

    def apply_signal_generator_settings(self):
        if self.signal_generator:
            try:
                frequency = float(self.frequency_input.text())
                amplitude = float(self.amplitude_input.text())
                waveform = self.waveform_combo_box.currentText()
                # Add code to apply Signal Generator settings
                # Example: self.signal_generator.write(f'SOURce:FUNCtion {waveform}')
                # Example: self.signal_generator.write(f'SOURce:FREQuency {frequency}')
                # Example: self.signal_generator.write(f'SOURce:POWer {amplitude}')
                print(f"Settings applied: Frequency={frequency} Hz, Amplitude={amplitude} dBm, Waveform={waveform}")
            except ValueError:
                print("Invalid input for frequency or amplitude.")
            except Exception as e:
                print(f"Error applying Signal Generator settings: {e}")

    # ... (Add the rest of the Signal Generator functionalities here)

# ... (Rest of the code remains the same)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpectrumAnalyzerGUI()
    window.show()
    sys.exit(app.exec_())
